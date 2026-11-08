# My Workspace (AI Cockpit)

このリポジトリは、日々のエンジニアリング業務における**タスク管理・外部情報トリアージ・日報作成・個人思考メモ**を集約する「業務司令塔（コックピット）」です。

## ディレクトリ構成

```text
my_workspace_AI/
├── AGENTS.md               # AIの役割と基本ルール（自律トリアージ・日報支援）
├── TODO.md                 # リアルタイムToDoリスト
├── .env.example            # 外部APIトークン等の設定サンプル
├── daily/                  # 日次作業ログ・日報アーカイブ
├── scripts/                # Outlook / Teams / Bitbucket 連携用スクリプト
├── notes/                  # ミーティング議事録・技術アイデア・使い捨てメモ
└── .agents/                # Antigravity用カスタムルール・スキル
    ├── rules/              # タスク優先度判定ルールなど
    └── skills/             # /morning-triage, /evening-report などの自動化手順
```

## 日常の運用フロー

1. **朝（始業時）**:
   - `agy` で「朝のタスク確認をして」「`/morning-triage`」と指示。
   - スクリプトが実行され、BitbucketやTeamsの通知から `TODO.md` が自動更新される。
2. **日中（業務中）**:
   - `TODO.md` を見ながらタスクを消化。
   - 製品A/製品Bの設計・コード作業時は、該当リポジトリ（ナレッジ）を同時に開いて作業。
3. **夕方（終業時）**:
   - `agy` で「今日の日報を作って」「`/evening-report`」と指示。
   - `TODO.md` の完了実績と作業内容をもとに、`daily/` 配下に日報ファイルが生成される。
