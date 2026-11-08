#!/usr/bin/env python3
"""
Outlook (Microsoft 365) 重要メール取得スクリプト (雛形)
未読かつ重要度が高いメール、または自分宛ての直接メールを抽出します。
"""

import os
import sys
import json
from pathlib import Path

try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parents[2] / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

def get_important_emails():
    client_id = os.getenv("M365_CLIENT_ID")

    if not client_id:
        # 認証情報未設定時のサンプルデータ
        return [
            {
                "id": "msg_001",
                "subject": "【緊急】基板試作ロット納期の件（ご確認のお願い）",
                "sender": "tanaka@pcb-vendor.co.jp",
                "importance": "high",
                "received_at": "2026-11-08T08:45:00Z",
                "snippet": "先日ご注文いただきました製品Aの基板試作について、特定部品の入手遅延が発生しており..."
            },
            {
                "id": "msg_002",
                "subject": "第3四半期 組み込み開発部会 アジェンダ共有",
                "sender": "suzuki@company.com",
                "importance": "normal",
                "received_at": "2026-11-08T09:15:00Z",
                "snippet": "来週水曜日の定例会アジェンダです。各製品の進捗報告をお願いします。"
            }
        ]

    # 実装例: Microsoft Graph API `/v1.0/me/messages?$filter=isRead eq false`
    return []

if __name__ == "__main__":
    emails = get_important_emails()
    print(json.dumps(emails, ensure_ascii=False, indent=2))
