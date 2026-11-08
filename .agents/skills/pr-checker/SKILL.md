---
name: pr-checker
description: Bitbucket上のPull Request状況（未レビュー、承認待ち、マージ可能）を素早く確認するスキル。
---

# Pull Request Checker Routine

Bitbucket上のPRの最新状況を確認・要約するための手順書です。

## 実行手順

1. **PR一覧の取得**:
   - `scripts/bitbucket/get_prs.py` を実行してPRのJSONデータを取得する。

2. **ステータス分析**:
   - **自分がレビュアーで未承認のPR**: レビュー優先度と更新日時を表示。
   - **自分が作成して承認待ちのPR**: レビュアーの状況（Approve済みか、コメントが付いているか）を確認。

3. **回答の提示**:
   - 表形式でPR番号、タイトル、リポジトリ、ステータス、URLを整理してユーザーに報告する。
   - 「PR #xxx のレビューを今すぐ開始しますか？」と問いかける。
