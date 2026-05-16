#!/usr/bin/env python3
"""Sync a GitHub repository ruleset.

This is a conservative template. Use --dry-run first. Standard example
rulesets are disabled by default; switch enforcement to active only after
repository-specific checks and bypass actors are correct.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


API_ROOT = "https://api.github.com"


def request(method: str, path: str, token: str, body: dict | None = None) -> dict | list:
    data = None
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(
        f"{API_ROOT}{path}",
        data=data,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(req) as response:
            payload = response.read().decode("utf-8")
            return json.loads(payload) if payload else {}
    except urllib.error.HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API failed: {exc.code} {message}") from exc


def load_ruleset(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        ruleset = json.load(f)
    if not isinstance(ruleset, dict):
        raise ValueError("ruleset JSON must be an object")
    if not ruleset.get("name"):
        raise ValueError("ruleset JSON must contain a name")
    return ruleset


def sync_repo(owner: str, repo: str, ruleset: dict, token: str, dry_run: bool) -> None:
    path = f"/repos/{owner}/{repo}/rulesets"
    name = ruleset["name"]

    if dry_run:
        print(f"[dry-run] would list rulesets for {owner}/{repo}")
        print(f"[dry-run] would create or update ruleset: {name}")
        return

    existing = request("GET", f"{path}?includes_parents=false", token)
    if not isinstance(existing, list):
        raise RuntimeError("unexpected GitHub API response for ruleset list")

    match = next((item for item in existing if item.get("name") == name), None)
    if match:
        ruleset_id = match["id"]
        print(f"Updating {owner}/{repo}: {name} (id: {ruleset_id})")
        request("PUT", f"{path}/{ruleset_id}", token, ruleset)
    else:
        print(f"Creating {owner}/{repo}: {name}")
        request("POST", path, token, ruleset)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync a GitHub repository ruleset.")
    parser.add_argument("--owner", required=True)
    parser.add_argument(
        "--repo",
        action="append",
        required=True,
        help="Repository name. Repeat for multiple repositories.",
    )
    parser.add_argument("--ruleset", required=True, type=Path)
    parser.add_argument(
        "--dry-run",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Show intended action without calling GitHub write APIs. Default: true.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ruleset = load_ruleset(args.ruleset)

    token = os.environ.get("GITHUB_TOKEN")
    if not token and not args.dry_run:
        print("GITHUB_TOKEN is required when --no-dry-run is used.", file=sys.stderr)
        return 1

    for repo in args.repo:
        sync_repo(args.owner, repo, ruleset, token or "", args.dry_run)

    # This script intentionally avoids delete calls and legacy branch protection edits.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
