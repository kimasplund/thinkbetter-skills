#!/usr/bin/env python3
"""Score the regression round against PRE-REGISTRATION.md.

Usage: score.py <run_dir> <rows.json>
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

R = Path(sys.argv[1])
rows = json.load(open(sys.argv[2]))
fx = json.load(open(R / "fixtures/fixtures.json"))
arms = json.load(open(R / "SEALED.json"))  # {"m1": "old"|"new", "m2": ...}
code = {v: k for k, v in arms.items()}      # "old" -> "m1"
MODELS = ["haiku", "sonnet"]

# G1 triggering
print("== G1 triggering (correct / 40)")
trig = {}
for arm in ("old", "new"):
    for m in MODELS:
        f = R / f"raw/trigger-{code[arm]}-{m}.json"
        picks = json.load(open(f)) if f.exists() else {}
        miss = [q["id"] for q in fx["trigger"] if picks.get(q["id"], "MISSING") not in q["expect"]]
        trig[(arm, m)] = (40 - len(miss), miss)
for m in MODELS:
    (o, om), (n, nm) = trig[("old", m)], trig[("new", m)]
    print(f"  {m:6} old {o:2}  new {n:2}  {'PASS' if n >= o - 1 else 'FAIL'}   new misses: {nm}   old misses: {om}")
g1 = all(trig[("new", m)][0] >= trig[("old", m)][0] - 1 for m in MODELS)

# mechanical leak scan
NAMES = ["integrated-reasoning", "tree-of-thoughts", "tree of thoughts", "breadth-of-thought", "breadth of thought",
         "self-reflecting-chain", "self-reflecting chain", "hypothesis-elimination", "hypothesis elimination",
         "adversarial-reasoning", "dialectical-reasoning", "dialectical reasoning", "analogical-transfer",
         "rapid-triage-reasoning", "rapid triage", "negotiated-decision-framework", "parallel-execution",
         "reasoning-handover-protocol", "premortem-evolved", "skill-gauntlet", "option-synthesis"]
ACR = r"\b(ToT|BoT|SRC|HE|AR|DR|AT|RTR|NDF|IR)\b"  # exactly the pre-registered list
LEAK_RES = [re.compile("|".join(re.escape(n) for n in NAMES), re.I), re.compile(ACR),
            re.compile(r"(?i)confidence[^\n]{0,20}\d{1,3}\s?%"),
            re.compile(r"(?im)^#+\s*(stage|phase|step|level)\s*\d")]

def mech(path):
    t = path.read_text() if path.exists() else ""
    return sum(len(r.findall(t)) for r in LEAK_RES), len(t.split())

mech_tot = defaultdict(int)
words = {}
for b in fx["behavior"]:
    for m in MODELS:
        for arm in ("old", "new"):
            n, w = mech(R / f"raw/{b['id']}--{m}--{code[arm]}.md")
            mech_tot[arm] += n
            words[(b["id"], m, arm)] = w

# unblind judge rows
J = []
for r in rows:
    if r.get("error"):
        J.append(r); continue
    u = {"id": r["id"], "model": r["model"], "note": r["note"]}
    for arm in ("old", "new"):
        c = code[arm]
        u[f"q_{arm}"], u[f"p_{arm}"], u[f"l_{arm}"] = r[f"q_{c}"], r[f"p_{c}"], r[f"l_{c}"]
    u["pref"] = "tie" if r["pref"] == "tie" else arms[r["pref"]]
    J.append(u)
ok = [r for r in J if not r.get("error")]

print(f"\n== Behavior ({len(ok)}/28 judged)")
print(f"  {'fixture':14} {'model':6}  qual o/n  prop o/n  leak o/n  words o/n   pref   note")
for r in ok:
    wo, wn = words[(r["id"], r["model"], "old")], words[(r["id"], r["model"], "new")]
    print(f"  {r['id']:14} {r['model']:6}  {r['q_old']:2}/{r['q_new']:<2}     {r['p_old']:2}/{r['p_new']:<2}     "
          f"{r['l_old']:2}/{r['l_new']:<2}    {wo:5}/{wn:<5}  {r['pref']:5}  {r['note'][:70]}")
for r in J:
    if r.get("error"):
        print(f"  {r['id']:14} {r['model']:6}  ERROR {r['error']}")

old_pref = [r for r in ok if r["pref"] == "old"]
by_skill = defaultdict(list)
for r in old_pref:
    by_skill[r["id"]].append(r["model"])
g2 = len(old_pref) <= 9 and not any(len(v) == 2 for v in by_skill.values())
jl_old, jl_new = sum(r["l_old"] for r in ok), sum(r["l_new"] for r in ok)
g3 = mech_tot["new"] <= mech_tot["old"] and jl_new <= jl_old
g4 = True
for m in MODELS:
    if words[("b-ir-trivial", m, "new")] > 1.25 * max(1, words[("b-ir-trivial", m, "old")]):
        g4 = False
    urg = [r for r in ok if r["id"] == "b-ir-urgent" and r["model"] == m]
    if not urg or urg[0]["p_new"] < urg[0]["p_old"] - 1:
        g4 = False
drops = [(r["id"], r["model"], r["q_old"], r["q_new"]) for r in ok if r["q_old"] - r["q_new"] >= 3]
g5 = not drops
complete = len(ok) == 28 and all((R / f"raw/trigger-{code[a]}-{m}.json").exists() for a in ("old", "new") for m in MODELS)

prefs = defaultdict(int)
for r in ok:
    prefs[r["pref"]] += 1
print(f"\n  preference: new {prefs['new']}, old {prefs['old']}, tie {prefs['tie']}")
print(f"  mean quality old {sum(r['q_old'] for r in ok)/max(1,len(ok)):.2f}  new {sum(r['q_new'] for r in ok)/max(1,len(ok)):.2f}")
print(f"  mean proportion old {sum(r['p_old'] for r in ok)/max(1,len(ok)):.2f}  new {sum(r['p_new'] for r in ok)/max(1,len(ok)):.2f}")
print("\n== Gate")
print(f"  G1 triggering            {'PASS' if g1 else 'FAIL'}")
print(f"  G2 preference            {'PASS' if g2 else 'FAIL'}  (old preferred {len(old_pref)}/28; both-model losses: {[k for k, v in by_skill.items() if len(v) == 2]})")
print(f"  G3 leakage               {'PASS' if g3 else 'FAIL'}  (mechanical old {mech_tot['old']} / new {mech_tot['new']}; judged old {jl_old} / new {jl_new})")
print(f"  G4 restraint             {'PASS' if g4 else 'FAIL'}  (trivial words haiku {words[('b-ir-trivial','haiku','old')]}/{words[('b-ir-trivial','haiku','new')]}, sonnet {words[('b-ir-trivial','sonnet','old')]}/{words[('b-ir-trivial','sonnet','new')]})")
print(f"  G5 no 3-pt quality drop  {'PASS' if g5 else 'FAIL'}  {drops}")
verdict = "INCONCLUSIVE (missing cells)" if not complete else ("ADOPT" if all([g1, g2, g3, g4, g5]) else "NO ADOPTION")
print(f"\n  VERDICT: {verdict}")
