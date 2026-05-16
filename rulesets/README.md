# Rulesets

このディレクトリは GitHub Rulesets の標準雛形を置く場所です。

`*.example.json` は、GitHub REST API の repository rulesets body として読める形を目指した確定済みの標準雛形です。初期状態は安全側の `enforcement: disabled` にしています。実 repo に適用したあと、required checks や bypass actor を確認してから GitHub UI または API で `active` に切り替えます。

GitHub Rulesets の schema は変わる可能性があります。判断に迷う場合は [GitHub REST API docs](https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28) と GitHub UI の表示を優先します。`evaluate` は Enterprise で使える場合だけ選択肢にし、通常の fallback は `disabled` です。

## 一覧

| file | 対象 | 目的 |
|---|---|---|
| `branch-main-base.example.json` | durable repo | `main` を PR 単位の変更履歴で守る |
| `branch-main-light.example.json` | utility repo | `main` 直 push を許容しつつ破壊的操作を防ぐ |
| `branch-release-strict.example.json` | release / hotfix branch | リリース直前の変更を慎重に扱う |
| `push-hygiene-common.example.json` | 必要な repo 全般 | `.env`、巨大ファイル、生成物の混入を抑える |
| `push-hygiene-unity.example.json` | Unity repo | Unity 生成物や配布物の混入を抑える |
| `branch-archive-freeze.example.json` | 完了・休眠 repo | 誤更新を防ぐ |

## 適用順

1. repository profile を決める。
2. branch ruleset を 1 つ選ぶ。
3. 必要な場合だけ push hygiene ruleset を追加する。
4. release / hotfix 運用がある repo だけ `branch-release-strict` を追加する。
5. 完了または休眠 repo だけ `branch-archive-freeze` を検討する。

## Required checks

`branch-main-base` と `branch-release-strict` の JSON には required status checks を固定で入れません。check 名は repo ごとに異なるためです。

候補:

- `lint`
- `test`
- `build`
- `security-scan`

対象 repo の Actions check 名を確認し、必要な check だけを GitHub UI または export JSON で追加します。

## GitHub UI import / export

GitHub UI では、対象 repository の Settings から Rulesets を開き、ruleset の作成、編集、import、export を行います。

このディレクトリの example JSON は標準雛形です。実適用時に UI が異なる形式を出す場合は、UI export と公式 docs を優先して雛形を更新します。

## 注意

- example JSON は `disabled` なので、適用後に明示的に `active` へ切り替える。
- required checks の名前は repo ごとに確認してから追加する。
- `.env.example`、Git LFS 対象ファイル、コミットが必要な `dist/` などを誤って禁止しない。
- いきなり複数 repo へ一括適用しない。最初は 1 repo で試す。
