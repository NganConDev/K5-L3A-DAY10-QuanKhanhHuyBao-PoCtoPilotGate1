#!/usr/bin/env python3
"""
Tự động tạo các Issue trên GitHub repository cho nhóm 4 người (Quân, Khánh, Huy, Bảo)
phụ trách Khối 1 và Khối 2 trong LAB 10 (From PoC to Pilot - Gate 1).

Cách sử dụng:
    python3 scripts/create_github_issues.py <GITHUB_PERSONAL_ACCESS_TOKEN>
    hoặc:
    export GITHUB_TOKEN="ghp_xxxx..."
    python3 scripts/create_github_issues.py
"""

import sys
import os
import json
import urllib.request
import urllib.error
import getpass

REPO_OWNER = "NganConDev"
REPO_NAME = "K5-L3A-DAY10-QuanKhanhHuyBao-PoCtoPilotGate1"

ISSUES = [
    {
        "file": "docs/issues/00-epic-block1-2-overview.md",
        "labels": ["epic", "block-1", "block-2"],
    },
    {
        "file": "docs/issues/01-khanh-gate-engineer-1.md",
        "labels": ["block-1", "block-2", "gate-engineer"],
    },
    {
        "file": "docs/issues/02-quan-gate-engineer-2.md",
        "labels": ["block-1", "block-2", "gate-engineer"],
    },
    {
        "file": "docs/issues/03-huy-product-business.md",
        "labels": ["block-1", "block-2", "product-business"],
    },
    {
        "file": "docs/issues/04-bao-operations-legal.md",
        "labels": ["block-1", "block-2", "operations-legal"],
    },
]

LABELS = [
    {"name": "epic", "color": "3E4B9E", "description": "Theo dõi tiến độ tổng thể"},
    {"name": "block-1", "color": "0E8A16", "description": "Khối 1: Tiêu chí & Ký tiêu chí (phút 15-65)"},
    {"name": "block-2", "color": "FBCA04", "description": "Khối 2: Đo, rủi ro, cổng vòng 1, quyết định v1 (phút 65-115)"},
    {"name": "gate-engineer", "color": "1D76DB", "description": "Vai trò Kỹ sư cổng"},
    {"name": "product-business", "color": "5319E7", "description": "Vai trò Sản phẩm và kinh doanh"},
    {"name": "operations-legal", "color": "D93F0B", "description": "Vai trò Vận hành và pháp lý"},
]

def make_request(url, token, data=None, method="GET"):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "Lab10-Issue-Creator",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    encoded_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def ensure_labels(token):
    print("🏷️  Đang kiểm tra và tạo nhãn (labels)...")
    base_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/labels"
    for label in LABELS:
        try:
            make_request(base_url, token, data=label, method="POST")
            print(f"  + Đã tạo label: {label['name']}")
        except urllib.error.HTTPError as e:
            if e.code == 422: # Đã tồn tại
                print(f"  = Label đã có sẵn: {label['name']}")
            else:
                print(f"  ! Không tạo được label {label['name']}: {e.code}")

def create_issues(token):
    ensure_labels(token)
    print("\n🚀 Đang tạo các issues...")
    created = []
    
    for item in ISSUES:
        filepath = item["file"]
        if not os.path.exists(filepath):
            print(f"❌ Không tìm thấy file: {filepath}")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        lines = content.strip().split("\n")
        title = lines[0].lstrip("# ").strip()
        body = "\n".join(lines[1:]).strip()
        
        issue_data = {
            "title": title,
            "body": body,
            "labels": item["labels"]
        }
        
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
        try:
            resp = make_request(url, token, data=issue_data, method="POST")
            print(f"✅ Đã tạo Issue #{resp['number']}: {title}")
            print(f"   URL: {resp['html_url']}")
            created.append((resp['number'], title, resp['html_url']))
        except urllib.error.HTTPError as e:
            print(f"❌ Lỗi khi tạo issue '{title}': HTTP {e.code} - {e.read().decode('utf-8')}")
            
    print(f"\n🎉 Đã hoàn thành! Tổng cộng tạo được {len(created)} issues.")
    for num, t, link in created:
        print(f" - #{num}: {t} -> {link}")

def main():
    token = None
    if len(sys.argv) > 1:
        token = sys.argv[1].strip()
    elif os.environ.get("GITHUB_TOKEN"):
        token = os.environ.get("GITHUB_TOKEN").strip()
    elif os.environ.get("GH_TOKEN"):
        token = os.environ.get("GH_TOKEN").strip()
    else:
        print(f"Repo mục tiêu: https://github.com/{REPO_OWNER}/{REPO_NAME}")
        token = getpass.getpass("Nhập GitHub Personal Access Token (classic hoặc fine-grained có quyền repo): ").strip()
        
    if not token:
        print("Lỗi: Cần cung cấp GitHub token!")
        sys.exit(1)
        
    create_issues(token)

if __name__ == "__main__":
    main()
