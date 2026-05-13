# Hyd3-14 default community health files

このリポジトリは、Hyd3-14 個人リポジトリ向けの default community health files を管理する。

## 役割

- 各リポジトリに個別ファイルがない場合の Issue / Pull Request / Security / Support 導線を提供する
- ラベル標準の参照元を置く
- 新規リポジトリの初期設定で迷う項目を減らす

## 注意

- この仕組みを有効にするには、このリポジトリが public である必要がある
- 対象リポジトリ側に同名の community health file がある場合は、対象リポジトリ側が優先される
- `.github/labels.yml` は GitHub が自動適用する設定ではなく、同期スクリプトや人間向けの標準参照元として扱う
- workflow、Dependabot 設定、Rulesets は各リポジトリ側で管理する
