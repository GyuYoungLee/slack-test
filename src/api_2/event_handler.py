"""
slack-bolt 이용 이벤트 답변 메시지 보내기

Socket Mode
  1. scopes 추가 => commands
"""

import os
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from src.templates import get_template

load_dotenv(verbose=True)

app = App(token=os.environ["SLACK_BOT_TOKEN"])


# hello 메시지 응답
@app.message("hello")
def message_handler(message, say):
    # say(f"Hello... by slack-bolt 1.13.0")
    say(get_template())


if __name__ == "__main__":
    SocketModeHandler(app, app_token=os.environ["SLACK_APP_TOKEN"]).start()
