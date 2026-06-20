#!/usr/bin/env bash
# Full site rebuild and verification. Run before pushing content or asset changes.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> Rebuild DNA comparison figure"
python3 scripts/build-topview-compare.py

echo "==> Rebuild social preview meta and post pages"
python3 scripts/build-social-preview.py

echo "==> Sync cache-bust versions"
python3 scripts/sync-cache.py

echo "==> Verify post assets"
./scripts/check-post-assets.sh

echo "==> Verify theme"
./scripts/check-theme.sh

echo "==> Deploy checks passed"
