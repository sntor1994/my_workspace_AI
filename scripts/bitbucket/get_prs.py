#!/usr/bin/env python3
"""
Bitbucket PR取得スクリプト (雛形)
自分がレビュアーに指定されている未承認PR、および自分が作成した未マージPRを取得します。
"""

import os
import sys
import json
from pathlib import Path

# .env の読み込み
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parents[2] / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

def get_pull_requests():
    workspace = os.getenv("BITBUCKET_WORKSPACE")
    username = os.getenv("BITBUCKET_USERNAME")
    app_password = os.getenv("BITBUCKET_APP_PASSWORD")

    if not all([workspace, username, app_password]):
        # 設定がまだない場合はサンプル（モック）データを返却
        return [
            {
                "id": "102",
                "title": "fix: I2C通信時のタイムアウト処理とバスリカバリ機能の追加",
                "repository": "firmware-product-a",
                "author": "yamada-taro",
                "status": "NEEDS_REVIEW",
                "url": "https://bitbucket.org/example/product-a/pull-requests/102",
                "updated_on": "2026-11-08T09:30:00Z"
            },
            {
                "id": "45",
                "title": "feat: BLEアドバタイズパケット構造の定義更新",
                "repository": "firmware-product-b",
                "author": username or "my-self",
                "status": "WAITING_APPROVAL",
                "url": "https://bitbucket.org/example/product-b/pull-requests/45",
                "updated_on": "2026-11-07T16:00:00Z"
            }
        ]

    # 実装例: Bitbucket REST API 2.0 呼び出し
    # import requests
    # url = f"https://api.bitbucket.org/2.0/repositories/{workspace}?q=..."
    # r = requests.get(url, auth=(username, app_password))
    # return r.json()
    return []

if __name__ == "__main__":
    prs = get_pull_requests()
    # agy等のエージェントがパースしやすいようJSONで標準出力
    print(json.dumps(prs, ensure_ascii=False, indent=2))
