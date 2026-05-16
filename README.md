# Hyd3-14 default community health files and GitHub standards

このリポジトリは、Hyd3-14 個人リポジトリ向けの default community health files と GitHub 運用標準を管理する場所です。

`.github` というリポジトリ名でも、ここに置いた ruleset JSON、運用ドキュメント、適用スクリプトが自動的に全リポジトリへ適用されるわけではありません。自動適用されるのは GitHub が公式に認識する community health file や workflow template などに限られます。

## 役割

- 各リポジトリに個別ファイルがない場合の Issue / Pull Request / Security / Support 導線を提供する
- ラベル標準の参照元を置く
- GitHub Rulesets、branch protection、push hygiene の標準案を置く
- 新規リポジトリの初期設定で迷う項目を減らす

## 置くもの

- GitHub の共通 issue / PR template
- GitHub REST API に渡せる ruleset example JSON
- GitHub Rulesets の運用方針
- ruleset 適用手順のメモ
- `gh api` や GitHub API を使うための安全側の雛形スクリプト

## 置かないもの

- personal access token や secret
- repo ごとの live settings のミラー
- 既存リポジトリへ即時適用するための一括実行状態
- private な作業メモや外部に出せない判断材料

## 自動適用されるものとされないもの

自動適用される可能性があるもの:

- 対象リポジトリに個別ファイルがない場合の Issue / Pull Request template
- `SECURITY.md`
- `SUPPORT.md`

自動適用されないもの:

- `.github/labels.yml`
- `rulesets/` 配下の JSON
- `docs/` 配下の運用ドキュメント
- `scripts/` 配下の適用スクリプト
- repository settings、branch protection、Rulesets

## Rulesets 管理方針

GitHub Rulesets の標準雛形は `rulesets/*.example.json` に置きます。これらは GitHub REST API の repository rulesets body として読める形を目指しますが、初期状態は安全側の `enforcement: disabled` です。実 repo に適用するときは、required checks や bypass actor を repo ごとに確認し、必要に応じて GitHub UI または API で `active` に切り替えます。

GitHub Rulesets の schema は GitHub 側で変わる可能性があります。判断に迷う場合は [GitHub REST API docs](https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28) と GitHub UI の表示を優先します。`evaluate` は Enterprise で使える場合だけ選択肢にし、通常の fallback は `disabled` です。

今回は標準を作ることが目的です。既存リポジトリの settings、branch protection、ruleset は変更しません。

## Repository profiles

| profile | 概要 | 基本方針 |
|---|---|---|
| durable | 長期保守、公開、研究、ポートフォリオ候補 | `main` は PR 経由を推奨し、CI と履歴品質を守る |
| utility | dotfiles、個人用スクリプト、小規模 CLI | `main` 直 push を許容しつつ破壊的操作を防ぐ |
| scratch | 検証、実験、一時作業 | 速度を優先し、過剰な保護を避ける |

## 最初に読むもの

1. [Repository profiles](docs/repository-profiles.md)
2. [Ruleset policy](docs/ruleset-policy.md)
3. [Rulesets catalog](rulesets/README.md)
4. [Application guide](docs/ruleset-application-guide.md)
5. [Scripts](scripts/README.md)
