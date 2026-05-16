# Repository profiles

Rulesets は repo の性質に合わせて選びます。強い保護を全 repo にかけるのではなく、履歴品質、復旧コスト、作業速度のバランスを取ります。

| profile | 用途 | main直push | PR必須 | CI必須 | 推奨rulesets |
|---|---|---:|---:|---:|---|
| durable | 長期保守、公開、研究、卒研、他人が見る可能性がある repo | 原則なし | はい | はい | `branch-main-base`, 必要に応じて `push-hygiene-common`, Unity なら `push-hygiene-unity`, release 運用があれば `branch-release-strict` |
| utility | dotfiles、個人用スクリプト、小規模 CLI、設定管理 | 許容 | repo ごと | 任意 | `branch-main-light`, 必要に応じて `push-hygiene-common` |
| scratch | 検証、実験、一時作業、throwaway demo | 許容 | いいえ | いいえ | 原則なし。必要なら `branch-main-light` の一部 |

## durable repo

長期的に残す、公開する、研究や卒研で使う、または将来ポートフォリオに載せる可能性がある repo です。

例:

- `unity-scene-review`
- `UnitySceneReviewSample`
- 研究支援ツール
- 公開予定の Web アプリ
- 将来ポートフォリオに載せる可能性がある repo

基本方針:

- `main` は PR 経由にする。
- solo repo では approval は原則 `0` にする。
- CI required checks は必要に応じて有効にする。ただし標準 JSON には固定せず、check 名は repo ごとに合わせる。
- force push と branch deletion は禁止する。
- linear history と squash merge を推奨する。

## utility repo

壊れると困るが、毎回 PR を切るほどではない repo です。

例:

- dotfiles
- 小さい自動化スクリプト集
- 個人用の設定管理 repo
- 軽量なメモ・テンプレ repo

基本方針:

- `main` 直 push は許容してよい。
- force push と branch deletion は禁止する。
- CI は任意。
- PR 必須化は repo ごとに判断する。
- durable repo に育ってきたら `branch-main-base` へ移行する。

## scratch repo

検証、実験、一時作業用の repo です。壊れてもよく、履歴品質より速度を優先します。

例:

- throwaway demo
- 技術検証
- sandbox
- 一時的な学習 repo

基本方針:

- 過剰に守らない。
- PR や CI を必須にしない。
- public repo では `.env` や巨大ファイル混入には注意する。
