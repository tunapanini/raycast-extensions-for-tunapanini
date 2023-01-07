#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title 랜덤 문자열 생성하기
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.author Tunapanini
# @raycast.authorURL https://github.com/tunapanini

import random
import subprocess

string_length = 8
elements = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

result = "".join([random.choice(elements) for i in range(string_length)])

subprocess.run("pbcopy", text=True, input=result)

print(f"클립보드에 복사함! {result}")
