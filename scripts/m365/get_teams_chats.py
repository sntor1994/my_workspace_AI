#!/usr/bin/env python3
"""
Microsoft Teams メンション・新着メッセージ取得スクリプト (雛形)
自分宛てのメンションまたは重要チャンネルの未読メッセージを取得します。
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

def get_teams_mentions():
    client_id = os.getenv("M365_CLIENT_ID")

    if not client_id:
        return [
            {
                "id": "teams_001",
                "channel": "製品A開発PJ / 回路設計",
                "sender": "佐藤 健一",
                "created_at": "2026-11-08T09:10:00Z",
                "content": "@佐藤(自分) Rev.A基板のプルアップ変更の件、既知の課題メモに反映しておきました！",
                "is_mention": True
            }
        ]

    # 実装例: MS Graph API `/v1.0/me/chats` または `/teams/.../messages`
    return []

if __name__ == "__main__":
    chats = get_teams_mentions()
    print(json.dumps(chats, ensure_ascii=False, indent=2))
