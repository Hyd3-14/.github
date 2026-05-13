# Contributing

このアカウント配下のリポジトリでは、小さく可逆な変更を優先します。

## Issue

- 実装や修正は、原則として Issue を起点にします
- Issue title には `[Bug]:` や `[Chore]:` のような prefix を付けず、内容が分かる自然なタイトルにします
- 種別は title ではなく `type: *` ラベルで表します

## Pull Request

- PR には対応 Issue への `closes #<issue>` を入れます
- 変更範囲に応じた確認手順を PR に残します
- 少なくとも 1 つの `type: *` ラベルを付けます
- workflow 追加・更新時は action の SHA pinning と最小権限を確認します

## ラベル

ラベル名は英語、description は日本語を標準にします。

- `type: feature`: 新機能または機能追加
- `type: bug`: 不具合修正
- `type: chore`: 保守、設定、運用改善
- `type: docs`: ドキュメント変更
- `type: question`: 質問、相談、仕様確認

## 秘密情報

token、secret、個人情報、内部情報はコミットしないでください。脆弱性や秘密情報に関わる内容は公開 Issue では扱わず、`SECURITY.md` の方針に従います。
