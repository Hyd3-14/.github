# Ruleset policy

このドキュメントは、Hyd3-14 配下で GitHub Rulesets を使うときの判断基準です。

## main 直 push

`main` 直 push は完全否定しません。utility repo や scratch repo では、PR 必須化が摩擦になる場合があります。

一方で durable repo では、`main` への変更を PR 単位で残すことを推奨します。後から変更意図を追いやすくし、CI が落ちた変更を `main` に入れにくくするためです。

## solo repo の approval

solo repo では required approval `1` を標準にしません。自分しか reviewer がいない repo で approval を必須にすると、形式的な自己承認になりやすく、運用コストだけが増えます。

標準は approval `0` です。PR は変更単位、CI、会話解決、履歴のために使い、他者レビューがある repo だけ approval を増やします。

## Required checks

required checks は repo ごとに名前が異なります。`lint`、`test`、`build`、`security-scan` は候補ですが、標準 JSON には固定しません。

適用前に対象 repo の Actions check 名を確認し、存在しない check を required にしないでください。required checks が必要な repo では、GitHub UI または repo 固有の export JSON で追加します。

`Require branches to be up to date` は安全性を上げますが、CI 再実行が増えます。標準では off 寄りにし、release branch など必要な場所だけ有効にします。

## Enforcement

標準 example JSON は `enforcement: disabled` を既定にします。これは初回適用時に repository の push や merge を急に止めないためです。

内容を確認したあと、GitHub UI または API で `active` に切り替えます。`evaluate` は Enterprise で使える場合だけ選択肢にし、通常の fallback は `disabled` です。

## Bypass actor

bypass actor は最小限にします。owner / admin だけを想定し、通常作業の回避経路として使いません。

archive freeze のように更新を止める ruleset では、緊急修正や設定変更のために owner / admin の bypass を残すことがあります。

## Push hygiene

push hygiene は `.env`、巨大ファイル、生成物、不要なバイナリの混入を抑えるための補助です。`.gitignore`、secret scanning、Git LFS の代替ではありません。

注意点:

- `.env.example` は許可する。
- `dist/` や `build/` を commit する repo では path block を調整する。
- Git LFS を使う repo では、拡張子制限と LFS 対象を衝突させない。
- file size 制限は例として 25MB を置くが、repo ごとに調整する。

## Unity repo

Unity repo では `Library/`、`Temp/`、`Obj/`、`Logs/`、`UserSettings/`、build artifact の混入を防ぎます。

一方で、`Assets/`、`ProjectSettings/`、`.meta` ファイルは通常コミット対象です。特に `.meta` を禁止しないでください。

大きなアセットを扱う場合は、ruleset だけでなく Git LFS 方針と `.gitignore` を合わせて整えます。

## Archive freeze

完了・休眠 repo では、`branch-archive-freeze` によって誤更新を防げます。

使う前に README に archived / maintenance status を明記し、Dependabot、deployment、CI の扱いも確認します。凍結は「更新しない」という意思表示なので、まだ活発に直す repo には使いません。

## Scratch repo

scratch repo を過剰に守ると、実験速度が落ちます。履歴品質より検証速度が重要な repo では、ruleset を原則なしにします。

ただし public repo の場合は、secret や巨大ファイルの混入だけは別途注意します。
