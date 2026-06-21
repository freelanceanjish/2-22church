#!/usr/bin/env bash
# Full site rebuild and verification. Run before pushing content or asset changes.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> Rebuild DNA comparison figure"
python3 scripts/build-topview-compare.py

echo "==> Rebuild DNA quantum tabernacle compare + square icon"
python3 scripts/build-dna-quantum-tabernacle-compare.py

echo "==> Capture live logo and hero tagline crops"
node scripts/capture-og-crops.mjs

echo "==> Rebuild social preview meta and post pages"
python3 scripts/build-social-preview.py

echo "==> Sync cache-bust versions"
python3 scripts/sync-cache.py

echo "==> Verify post assets"
./scripts/check-post-assets.sh

echo "==> Verify theme"
./scripts/check-theme.sh

echo "==> Deploy checks passed"
