#!/usr/bin/env bash
# Verify every image/SVG referenced in posts.js exists and SVGs are valid XML.
# Run before pushing article or asset changes: ./scripts/check-post-assets.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

POSTS="$ROOT/posts.js"
failures=0

fail() {
  echo "FAIL: $1" >&2
  failures=$((failures + 1))
}

pass() {
  echo "OK:   $1"
}

if [[ ! -f "$POSTS" ]]; then
  echo "posts.js not found" >&2
  exit 1
fi

mapfile -t assets < <(python3 - <<'PY'
import re
from pathlib import Path
text = Path("posts.js").read_text(encoding="utf-8")
paths = set()
paths.update(re.findall(r'image:\s*"([^"]+)"', text))
paths.update(re.findall(r'src="([^"]+)"', text))
for p in sorted(paths):
    if p.startswith("data:"):
        continue
    p = p.split("?", 1)[0]
    print(p)
PY
)

echo "Checking ${#assets[@]} post assets..."
echo

for asset in "${assets[@]}"; do
  path="$ROOT/$asset"
  if [[ ! -f "$path" ]]; then
    fail "missing asset: $asset"
    continue
  fi
  if [[ "$asset" == *.svg ]]; then
    if python3 -c "import xml.etree.ElementTree as ET; ET.parse('$path')" 2>/dev/null; then
      pass "valid SVG: $asset"
    else
      fail "invalid SVG XML: $asset"
    fi
  else
    pass "found: $asset"
  fi
done

echo
if [[ "$failures" -gt 0 ]]; then
  echo "${failures} post asset check(s) failed."
  exit 1
fi

echo "All post asset checks passed."
