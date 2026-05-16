# Scripts

このディレクトリの script は GitHub Rulesets 適用の雛形です。初回は dry-run で確認し、1 repo で検証してから使います。

## 前提

- GitHub API を叩くには `gh auth login` または `GITHUB_TOKEN` が必要です。
- 対象 owner と repo を明示します。
- 同名 ruleset が既にある場合は create ではなく update します。
- 既存 ruleset や branch protection を削除しません。
- `rulesets/*.example.json` は初期状態 `disabled` の標準雛形です。確認後に GitHub UI または API で `active` に切り替えます。
- token や secret をファイルに書きません。

## Files

- `sync-ruleset.sh`: `gh api` を使う shell script の雛形。
- `sync-ruleset.py`: 標準ライブラリ中心の Python script の雛形。既定は `--dry-run` 推奨。

## Safety

script は destructive な操作をしない方針です。ただし GitHub API の ruleset update は repository の挙動を変えます。実行前に対象 repo、ruleset 名、enforcement、required checks、bypass actor を確認してください。
