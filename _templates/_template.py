#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title title
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🥪
# @raycast.argument1 { "type": "text", "placeholder": "placeholder" }
# @raycast.packageName packageName

# Documentation:
# @raycast.description description
# @raycast.author Tunapanini
# @raycast.authorURL https://github.com/tunapanini

# pip install python-dotenv==0.21.0

import os
from dotenv import dotenv_values

config = {
    **os.environ,
    **dotenv_values(".env.local"),
}

# ... = config["..."]
