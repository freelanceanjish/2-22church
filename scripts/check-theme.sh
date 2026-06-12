#!/usr/bin/env bash
# Guard against accidental rollback to the old dark homepage theme.
# Run before pushing: ./scripts/check-theme.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

failures=0

fail() {
  echo "FAIL: $1" >&2
  failures=$((failures + 1))
}

pass() {
  echo "OK:   $1"
}

check_file() {
  local label="$1"
  local file="$2"
  if [[ ! -f "$file" ]]; then
    fail "$label — missing file: $file"
    return
  fi
  echo "$3" "$file"
}

must_contain() {
  local label="$1"
  local file="$2"
  local pattern="$3"
  if rg -F -q -- "$pattern" "$file"; then
    pass "$label"
  else
    fail "$label — expected pattern not found in $file: $pattern"
  fi
}

must_not_contain() {
  local label="$1"
  local file="$2"
  local pattern="$3"
  if rg -F -q -- "$pattern" "$file"; then
    fail "$label — forbidden pattern found in $file: $pattern"
  else
    pass "$label"
  fi
}

echo "Checking light theme guardrails..."
echo

# Shared stylesheet (source of truth for inner pages)
must_contain "style.css uses Poppins" style.css "family=Poppins"
must_contain "style.css accent #172A36" style.css "--gold:#172A36"
must_contain "style.css light background" style.css "--deep:#FFFFFF"
must_not_contain "style.css has no dark #060C18" style.css "#060C18"

# Homepage — most fragile file; inline styles override style.css
index_lines=$(wc -l < index.html | tr -d ' ')
if [[ "$index_lines" -lt 1000 ]]; then
  fail "index.html line count ($index_lines) — likely old dark homepage copy (expect >= 1000)"
else
  pass "index.html line count ($index_lines)"
fi

must_contain "index.html links Poppins" index.html "family=Poppins"
must_contain "index.html inline accent #172A36" index.html "--gold:#172A36"
must_contain "index.html light inline background" index.html "--deep:#FFFFFF"
must_contain "index.html uses home-hero layout" index.html "home-hero"
must_not_contain "index.html has no Cormorant font link" index.html "Cormorant+Garamond"
must_not_contain "index.html has no dark #060C18" index.html "#060C18"
must_not_contain "index.html has no legacy blue #5B8DB8 accent" index.html "#5B8DB8"

# Post page — also had inline theme overrides
must_contain "post.html links Poppins" post.html "family=Poppins"
must_contain "post.html inline accent #172A36" post.html "--gold:#172A36"
must_not_contain "post.html has no dark #060C18" post.html "#060C18"
must_not_contain "post.html has no Cormorant font link" post.html "Cormorant+Garamond"

# Critical SVG assets must be well-formed XML (broken SVGs 500 on GitHub Pages)
if python3 -c "import xml.etree.ElementTree as ET; ET.parse('temple-three-rooms-topview.svg')" 2>/dev/null; then
  pass "temple-three-rooms-topview.svg is valid XML"
else
  fail "temple-three-rooms-topview.svg is not valid XML"
fi

echo
if [[ "$failures" -gt 0 ]]; then
  echo "${failures} check(s) failed."
  echo
  echo "If you only changed copy or images, restore index.html from main and re-apply edits."
  echo "Do not replace index.html with an older file from before the light theme redesign."
  exit 1
fi

echo "All theme checks passed."
