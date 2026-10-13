#!/usr/bin/env bash
# Symlink this repo's skills into an agent's skills directory so edits here are live.
#
# Usage: link_local.sh [target_dir] [skill ...]
#   target_dir defaults to ~/.claude/skills; skills default to every skills/<name>.
# Anything already at target/<name> that is not the right link moves to
# $LINK_BACKUP_DIR (default ~/.claude/skills-backup-YYYYMMDD), which sits outside the
# skills directory so backups never load as skills. Safe to re-run.
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target="${1:-$HOME/.claude/skills}"
shift || true
backup="${LINK_BACKUP_DIR:-$HOME/.claude/skills-backup-$(date +%Y%m%d)}"

if [ "$#" -gt 0 ]; then
  names=("$@")
else
  names=()
  for d in "$repo"/skills/*/; do names+=("$(basename "$d")"); done
fi

mkdir -p "$target"
for name in "${names[@]}"; do
  src="$repo/skills/$name"
  dest="$target/$name"
  [ -d "$src" ] || { echo "no such skill: $name" >&2; exit 1; }
  if [ -L "$dest" ] && [ "$(readlink "$dest")" = "$src" ]; then
    echo "ok $name"
    continue
  fi
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    mkdir -p "$backup"
    [ -e "$backup/$name" ] && { echo "backup already holds $name: $backup/$name" >&2; exit 1; }
    mv "$dest" "$backup/$name"
    echo "backup $name"
  fi
  ln -s "$src" "$dest"
  echo "link $name"
done
