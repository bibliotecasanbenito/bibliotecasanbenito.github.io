#!/usr/bin/env bash
# Mirror ~/sanbenito/conversations/docs into docs/conversations.
# Usage: ./sync-convos.sh [-n]   (-n = dry run, show what would change)
set -euo pipefail

SRC="${CONVOS_SRC:-$HOME/sanbenito/conversations/docs}"
DEST="$(cd "$(dirname "$0")" && pwd)/docs/conversations"

if [[ ! -d "$SRC" ]]; then
  echo "Source not found: $SRC" >&2
  exit 1
fi

DRY=()
if [[ "${1:-}" == "-n" ]]; then
  DRY=(--dry-run)
fi

mkdir -p "$DEST"
rsync -ac --delete --itemize-changes ${DRY[@]+"${DRY[@]}"} "$SRC/" "$DEST/"

if [[ ${#DRY[@]} -eq 0 ]]; then
  diff -rq "$SRC" "$DEST" && echo "Synced: $DEST matches $SRC"
fi
