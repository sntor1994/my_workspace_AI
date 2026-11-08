#!/usr/bin/env python3
"""
トリアージ・ヘルパー
Bitbucket / Teams / Outlook の情報を統合し、優先度順のタスク候補辞書を作成するユーティリティ。
"""

def summarize_triage(prs=None, emails=None, chats=None):
    tasks = []
    
    # 1. PRレビュー依頼
    if prs:
        for pr in prs:
            if pr.get("status") == "NEEDS_REVIEW":
                tasks.append({
                    "priority": "HIGH",
                    "source": "Bitbucket",
                    "title": f"PRレビュー対応: #{pr.get('id')} {pr.get('title')}",
                    "detail": f"リポジトリ: {pr.get('repository')} / 作成者: {pr.get('author')}"
                })

    # 2. 緊急メール
    if emails:
        for mail in emails:
            if mail.get("importance") == "high":
                tasks.append({
                    "priority": "HIGH",
                    "source": "Outlook",
                    "title": f"重要メール対応: {mail.get('subject')}",
                    "detail": f"差出人: {mail.get('sender')}"
                })

    # 3. Teamsメンション
    if chats:
        for chat in chats:
            if chat.get("is_mention"):
                tasks.append({
                    "priority": "MEDIUM",
                    "source": "Teams",
                    "title": f"Teamsメンション確認: {chat.get('channel')}",
                    "detail": f"発言者: {chat.get('sender')}「{chat.get('content')[:40]}...」"
                })

    return tasks
