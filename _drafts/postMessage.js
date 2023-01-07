#!/usr/bin/env node

// Required parameters:
// @raycast.schemaVersion 1
// @raycast.title 이슈등록 v2
// @raycast.mode fullOutput

// Optional parameters:
// @raycast.icon 🥪
// @raycast.argument1 { "type": "text", "placeholder": "placeholder" }

// Documentation:
// @raycast.author Tunapanini
// @raycast.authorURL https://github.com/tunapanini

// yarn global add dotenv @slack/web-api

const dotenv = require("dotenv");
const { WebClient } = require("@slack/web-api");

dotenv.config();


const SLACK_BOT_TOKEN = process.env.SLACK_BOT_TOKEN;
const SLACK_CHANNEL_ID = process.env.SLACK_CHANNEL_ID;
const SLACK_USER_ID = process.env.SLACK_USER_ID;
let [arg1] = process.argv.slice(0);

const text = `!이슈등록 ${arg1} /component:"Internal Builder" <@${SLACK_USER_ID}>`;


const web = new WebClient(SLACK_BOT_TOKEN);

(async () => {
    // https://api.slack.com/methods/chat.postMessage
    const result = await web.chat.postMessage({
      text,
      channel: SLACK_CHANNEL_ID,
    });
  
    console.log(`Successfully send message ${result.ts} in conversation ${SLACK_CHANNEL_ID}`);
  })();