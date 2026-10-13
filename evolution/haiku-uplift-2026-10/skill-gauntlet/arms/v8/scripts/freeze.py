#!/usr/bin/env python3
"""Verifier freeze — hash the harness's own files into the gate record.

The champion freeze protects the artifact; this protects the verifier. At
pre-registration, `register` hashes every file the verdict depends on (rubric,
key matrix, fixtures, normalize/scoring/audit scripts, harness reference files)
into <state_dir>/verifier-freeze.json — that manifest is the closed freeze set.
At verdict, `verify` must exit 0; with no file arguments it checks the WHOLE
manifest. Mid-round instrument repair is legal only as an amended row: `amend`
appends (never edits) a timestamped, reasoned amendment that must predate any
scoring use of the changed instrument and apply symmetrically to both arms.
Record scoring use with `used`; verify FAILS on any amendment that postdates a
use-event for the same file. A hash mismatch with no covering amendment = silent
verifier change = round void.

Tamper evidence: every saved state carries `state_hash` (md5 of the canonical
record without that field); verify re-checks it, so wholesale edits of the
ledger are caught. This RAISES THE COST of ledger edits — a coordinator with
write access can still rewrite history; the strong anchor is copying state_hash
into the external pre-registration file at registration and at every amendment.

Usage:
  freeze.py register <state_dir> <file> [file ...]
  freeze.py verify   <state_dir> [file ...]   (default: all registered + amended files)
  freeze.py amend    <state_dir> --reason "<rationale>" <file> [file ...]
  freeze.py used     <state_dir> <file>       (record: this instrument's scores consumed)
  freeze.py show     <state_dir>
"""
import hashlib, json, os, sys
from datetime import datetime, timezone

STORE = "verifier-freeze.json"


def md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(rec):
    return json.dumps({k: v for k, v in rec.items() if k != "state_hash"},
                      sort_keys=True)


def finalize(rec):
    rec["state_hash"] = hashlib.md5(canonical(rec).encode()).hexdigest()


def ledger_ok(rec):
    return rec.get("state_hash") == hashlib.md5(canonical(rec).encode()).hexdigest()


def load(state_dir):
    p = os.path.join(state_dir, STORE)
    if not os.path.exists(p):
        sys.exit(f"no freeze record at {p} — register first")
    with open(p) as f:
        return json.load(f)


def save(state_dir, rec):
    finalize(rec)
    os.makedirs(state_dir, exist_ok=True)
    with open(os.path.join(state_dir, STORE), "w") as f:
        json.dump(rec, f, indent=2, sort_keys=True)


def latest_declared(rec, path):
    """The hash `path` is currently declared to have: its latest amendment, else registration."""
    h = rec["files"].get(path)
    for a in rec.get("amendments", []):
        if path in a["files"]:
            h = a["files"][path]
    return h


def all_files(rec):
    s = set(rec["files"])
    for a in rec.get("amendments", []):
        s.update(a["files"])
    return sorted(s)


def cmd_register(state_dir, files):
    p = os.path.join(state_dir, STORE)
    if os.path.exists(p):
        sys.exit(f"freeze record already exists at {p} — refusing to overwrite "
                 f"(append-only; use amend with a reason)")
    rec = {"kind": "verifier-freeze", "registered": now(),
           "files": {f: md5(f) for f in files}, "amendments": [], "uses": []}
    save(state_dir, rec)
    print(f"registered {len(files)} files at {p}")
    for f in files:
        print(f"  {md5(f)}  {f}")
    print(f"state_hash {rec['state_hash']} — copy it into the external "
          f"pre-registration file for tamper-evidence")


def cmd_verify(state_dir, files):
    rec = load(state_dir)
    if not ledger_ok(rec):
        print("VERIFIER INTEGRITY: FAIL — ledger tamper (state_hash mismatch); "
              "the freeze record itself was edited")
        sys.exit(2)
    manifest = all_files(rec)
    checked = files if files else manifest
    bad = []
    for f in checked:
        if f not in rec["files"]:
            bad.append((f, "not in freeze record"))
        elif md5(f) != latest_declared(rec, f):
            bad.append((f, f"hash {md5(f)} != latest declared {latest_declared(rec, f)}"))
    # ordering audit: an amendment must PREDATE every use-event of the same file
    uses = rec.get("uses", [])
    for a in rec.get("amendments", []):
        for f in a["files"]:
            for u in uses:
                if u["file"] == f and u["timestamp"] < a["timestamp"]:
                    bad.append((f, f"amendment {a['timestamp']} postdates use-event "
                                   f"{u['timestamp']} — amendment must predate scoring use"))
    if rec.get("amendments"):
        print("amendments on record (audit surface):")
        for i, a in enumerate(rec["amendments"], 1):
            print(f"  #{i} {a['timestamp']} — {a['reason']}")
            for f, h in sorted(a["files"].items()):
                print(f"      {h}  {f}")
        if not uses:
            print("  note: no use-events recorded — confirm manually that every "
                  "amendment predates any scoring use (freeze.py used)")
    if bad:
        print("VERIFIER INTEGRITY: FAIL")
        for f, why in bad:
            print(f"  {f}: {why}")
        print("round is VOID: discard scores, restore or amend (with rationale), rerun")
        sys.exit(1)
    print(f"VERIFIER INTEGRITY: OK — checked {len(checked)} of {len(manifest)} "
          f"manifest files ({len(rec.get('amendments', []))} amendment(s), "
          f"{len(uses)} use-event(s) on record)")


def cmd_amend(state_dir, reason, files):
    rec = load(state_dir)
    if not ledger_ok(rec):
        sys.exit("ledger tamper (state_hash mismatch) — refusing to amend a "
                 "modified record; investigate first")
    rec.setdefault("amendments", []).append(
        {"timestamp": now(), "reason": reason, "files": {f: md5(f) for f in files}})
    save(state_dir, rec)
    print(f"amendment #{len(rec['amendments'])} recorded — legal only if it predates any "
          f"scoring use of the changed instrument and applies symmetrically to both arms")
    for f in files:
        print(f"  {md5(f)}  {f}")
    print(f"state_hash {rec['state_hash']} — copy it into the external "
          f"pre-registration file")


def cmd_used(state_dir, path):
    rec = load(state_dir)
    if not ledger_ok(rec):
        sys.exit("ledger tamper (state_hash mismatch) — refusing to record use; "
                 "investigate first")
    if path not in all_files(rec):
        sys.exit(f"{path} is not in the freeze manifest — register it (or fix the "
                 f"path) before recording use; use-events only exist for frozen files")
    rec.setdefault("uses", []).append({"timestamp": now(), "file": path})
    save(state_dir, rec)
    print(f"use-event recorded: {path} scores consumed at {rec['uses'][-1]['timestamp']}")


def cmd_show(state_dir):
    rec = load(state_dir)
    print(json.dumps(rec, indent=2, sort_keys=True))
    print(f"ledger integrity: {'OK' if ledger_ok(rec) else 'TAMPERED (state_hash mismatch)'}")


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd, state_dir = sys.argv[1], sys.argv[2]
    if cmd == "register":
        if not sys.argv[3:]:
            sys.exit("register needs at least one file")
        cmd_register(state_dir, sys.argv[3:])
    elif cmd == "verify":
        cmd_verify(state_dir, sys.argv[3:])
    elif cmd == "amend":
        # strict form: amend <state_dir> --reason "<rationale>" <file> [file ...]
        if len(sys.argv) < 6 or sys.argv[3] != "--reason" or not sys.argv[4].strip():
            sys.exit('usage: amend <state_dir> --reason "<rationale>" <file> [file ...]')
        cmd_amend(state_dir, sys.argv[4], sys.argv[5:])
    elif cmd == "used":
        if len(sys.argv) != 4:
            sys.exit("usage: used <state_dir> <file>")
        cmd_used(state_dir, sys.argv[3])
    elif cmd == "show":
        cmd_show(state_dir)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
