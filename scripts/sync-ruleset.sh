#!/usr/bin/env bash
set -euo pipefail

# Sync one repository ruleset with gh api.
#
# Usage:
#   scripts/sync-ruleset.sh OWNER REPO rulesets/branch-main-base.example.json
#
# The standard example JSON files are intentionally disabled by default. After
# syncing, inspect the target repository ruleset and switch enforcement to
# active only when the repository-specific settings are correct.

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 OWNER REPO RULESET_JSON" >&2
  exit 2
fi

OWNER="$1"
REPO="$2"
RULESET_FILE="$3"

if ! command -v gh >/dev/null 2>&1; then
  echo "gh is required. Run gh auth login first." >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required to read the local ruleset JSON." >&2
  exit 1
fi

if [ ! -f "$RULESET_FILE" ]; then
  echo "Ruleset file not found: $RULESET_FILE" >&2
  exit 1
fi

RULESET_NAME="$(_RULESET_FILE="$RULESET_FILE" python3 - <<'PY_NAME'
import json
import os
from pathlib import Path

path = Path(os.environ["_RULESET_FILE"])
with path.open("r", encoding="utf-8") as f:
    data = json.load(f)
name = data.get("name")
if not name:
    raise SystemExit(1)
print(name)
PY_NAME
)"

API_BASE="repos/${OWNER}/${REPO}/rulesets"

echo "Fetching existing repository rulesets for ${OWNER}/${REPO}..." >&2
EXISTING_ID="$(
  gh api "${API_BASE}?includes_parents=false" \
    --jq ".[] | select(.name == \"${RULESET_NAME}\") | .id" \
    2>/dev/null || true
)"

if [ -n "$EXISTING_ID" ]; then
  echo "Updating existing repository ruleset '${RULESET_NAME}' (id: ${EXISTING_ID})." >&2
  gh api \
    --method PUT \
    "${API_BASE}/${EXISTING_ID}" \
    --input "$RULESET_FILE"
else
  echo "Creating new repository ruleset '${RULESET_NAME}'." >&2
  gh api \
    --method POST \
    "$API_BASE" \
    --input "$RULESET_FILE"
fi

# This script never deletes rulesets or edits legacy branch protection.
