#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title title
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🥪
# @raycast.argument1 { "type": "text", "placeholder": "placeholder", "optional": false }
# @raycast.packageName packageName

# Documentation:
# @raycast.description description
# @raycast.author Tunapanini
# @raycast.authorURL https://github.com/tunapanini

if [ -f .env.local ]; then
  export $(echo $(cat .env.local | sed 's/#.*//g'| xargs) | envsubst)
fi

# ...=${...:=nop}
