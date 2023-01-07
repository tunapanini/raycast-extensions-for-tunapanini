#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Google Keep
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ./google-keep.png
# @raycast.argument1 { "type": "text", "placeholder": "Add note" }
# @raycast.packageName Google Keep

# Documentation:
# @raycast.author Tunapanini
# @raycast.authorURL https://github.com/tunapanini

# pip install python-dotenv==0.21.0 gkeepapi==0.14.2

import os
import sys
import gkeepapi
from dotenv import dotenv_values

config = {
    **os.environ,
    **dotenv_values(".env.local"),
}

email = config["GOOGLE_KEEP_EMAIL"]
xxxxxxxx = config["GOOGLE_KEEP_XXXXXXXX"]

try:
    keep = gkeepapi.Keep()
    print("로그인")
    success = keep.login(email, xxxxxxxx)
    print(f"노트 생성: {sys.argv[1]}")
    note = keep.createNote("", sys.argv[1])
    keep.sync()
    print(f"💫 추가 했어요! 💫: {sys.argv[1]}")
except Exception as e:
    print(e)
    print(f"⛔ 실패 했어요 ⛔: {sys.argv[1]}")
