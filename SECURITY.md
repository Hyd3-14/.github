# Security Policy

## 脆弱性の報告

脆弱性や秘密情報の漏えいにつながる内容は、公開 Issue には書かないでください。

対象リポジトリで private vulnerability reporting が有効な場合は、GitHub の private vulnerability reporting から報告してください。有効でない場合は、公開 Issue には再現に必要な秘密情報を含めず、最小限の概要だけを共有してください。

## 公開 Issue に書かない情報

- token、API key、password、secret
- 個人メールアドレスや個人情報
- セッション情報、端末固有の秘匿パス
- 未公開の脆弱性を悪用できる具体的な手順

## 誤って秘密情報をコミットした場合

秘密情報を削除するだけで済ませず、履歴・ローテーション・影響範囲を確認してください。必要に応じて該当 token や key を失効し、再発防止のため push protection や secret scanning の設定を見直します。
