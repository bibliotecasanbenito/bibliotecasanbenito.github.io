#!/usr/bin/env bash
# Serve docs/ locally and open it in the browser.
# Usage: ./preview.sh [port]   (default 9000; Ctrl-C to stop)
set -euo pipefail

PORT="${1:-9000}"
ROOT="$(cd "$(dirname "$0")" && pwd)/docs"
URL="http://localhost:$PORT/"

if lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "Port $PORT is already in use. Try: ./preview.sh <other port>" >&2
  exit 1
fi

echo "Serving $ROOT at $URL (Ctrl-C to stop)"
(sleep 1 && open "$URL") &
exec python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$ROOT"
