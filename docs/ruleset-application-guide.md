# Ruleset application guide

この手順は GitHub Rulesets を安全に適用するためのガイドです。今回は標準作成が目的なので、既存 repo へ即時適用しません。

参照元: [GitHub REST API docs](https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28)

## GitHub UI から import する

1. 対象 repository を開く。
2. Settings から Rulesets を開く。
3. New ruleset または Import ruleset を選ぶ。
4. この repo の `rulesets/*.example.json` を標準雛形として読み込む。
5. required checks が必要な場合は、対象 repo の実際の check 名を確認して追加する。
6. bypass actor が必要な場合は、対象 repo の権限体系に合わせて最小限だけ設定する。
7. 初期状態は `disabled` のまま保存する。
8. 内容を確認してから `active` に切り替える。Enterprise で `evaluate` が使える場合だけ、先に `evaluate` で影響を確認してよい。
9. 1 repo で試してから、他 repo への展開を検討する。

## GitHub UI で export して反映する

1. GitHub UI で ruleset を作成または編集する。
2. 対象 ruleset を export する。
3. export した JSON とこの repo の `rulesets/*.example.json` の差分を確認する。
4. GitHub UI または公式 docs に合わせる必要がある場合は、example JSON を更新する。
5. 実 repo 固有の check 名、bypass actor、deployment requirement は標準 JSON に固定しない。

## `gh api` で適用する考え方

GitHub API では repository rulesets の一覧を取得し、同名 ruleset があるか確認します。

- 同名 ruleset がある場合: create ではなく update する。
- 同名 ruleset がない場合: create する。
- 既存 ruleset を削除しない。
- 既存 branch protection を勝手に解除しない。
- 初期適用は `disabled` とし、確認後に `active` へ切り替える。

雛形は [scripts](../scripts/README.md) を参照してください。

## 適用前チェックリスト

- 対象 repo の profile は durable / utility / scratch のどれか。
- `main` 直 push を許容するか決めた。
- PR 必須化が必要か決めた。
- required approvals が solo repo に対して重すぎない。
- required checks を追加する場合、正確な check 名を確認した。
- `Require branches to be up to date` の CI コストを確認した。
- `.env.example` や必要な generated artifact を block しない。
- Unity repo では `.meta` を block しない。
- Git LFS 対象ファイルと拡張子 block が衝突しない。
- owner / admin bypass の必要性を確認した。

## 適用後チェックリスト

- ruleset が意図した repository にだけ存在する。
- `disabled` のまま内容確認できている。
- `active` に切り替える前に required checks と bypass actor を確認した。
- `main` への通常 push / PR merge の挙動が想定どおり。
- CI が required check として正しく認識されている。
- 存在しない check 名で merge が詰まっていない。
- `.env.example` など許可したいファイルが push 可能。
- block したい巨大ファイルや生成物が push できない。
- README や運用メモに repo の profile と ruleset 方針が書かれている。

## 展開方針

最初は 1 repo で試します。問題がなければ同じ profile の repo に広げます。全 repo への一括適用は、運用実績ができるまで避けます。
