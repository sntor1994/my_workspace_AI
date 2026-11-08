---
name: morning-triage
description: 始業時にOutlook、Teams、Bitbucketの状況を確認し、優先度順のタスクリストを作成してTODO.mdを更新するスキル。
---

# Morning Triage Routine

このスキルは、毎朝の業務開始時にやるべきことを外部ツールから自動収集し、トリアージを行うための手順書です。

## 実行手順

1. **外部情報の取得**:
   - `scripts/bitbucket/get_prs.py` を実行してPRの状況を取得する。
   - `scripts/m365/get_emails.py` を実行して未読・重要メールを取得する。
   - `scripts/m365/get_teams_chats.py` を実行してTeamsのメンションを取得する。

2. **優先度判定**:
   - `.agents/rules/task-priority.md` の基準に沿って、取得した情報を「High」「Medium」「Low」に分類する。

3. **TODO.md の更新**:
   - 既存の `TODO.md` の「今日の最優先タスク」「通常タスク」に新規項目を追加・再構成する。
   - 完了済みのタスク（前日分）は保持するかアーカイブを確認する。

4. **ユーザーへのブリーフィング**:
   - 今日のToDoの要約（特に至急対応が必要なもの）をチャットで簡潔に提示し、「どこから着手しますか？」と促す。
