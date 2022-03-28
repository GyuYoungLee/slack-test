"""
slack-sdk 를 이용 메시지 보내기

Permissions
  0. bot token 발급
  1. scopes 추가 => channels:read, channels:history, chat:write
"""

import os
from dotenv import load_dotenv
from slack_sdk import WebClient

load_dotenv(verbose=True)


class SlackBot:
    def __init__(self) -> None:
        self.client = WebClient(os.environ["SLACK_BOT_TOKEN"])

    def get_channel_id(self, channel_name: str) -> str:
        # conversations_list: channels:read
        result = self.client.conversations_list(limit=200)  # default: 100

        channels = result.data['channels']
        channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
        channel_id = channel["id"]
        return channel_id

    def get_message_id(self, channel_id: str, query: str) -> str:
        # conversations_history: channels:history, 앱을 채널을 추가
        result = self.client.conversations_history(channel=channel_id)

        messages = result.data['messages']
        message = list(filter(lambda m: query in m["text"], messages))[0]
        message_id = message["ts"]
        return message_id

    def post_message(self, channel_id: str, text: str) -> None:
        # chat_postMessage: chat:write
        self.client.chat_postMessage(channel=channel_id, text=text)

    def post_message_in_thread(self, channel_id: str, message_id: str, text: str) -> None:
        self.client.chat_postMessage(channel=channel_id, thread_ts=message_id, text=text)


if __name__ == '__main__':
    myBot = SlackBot()

    c_id = myBot.get_channel_id(channel_name="test_gylee_2")  # C037S1C1TBR
    myBot.post_message(channel_id=c_id, text="안녕")

    msg_id = myBot.get_message_id(c_id, query="여기")
    myBot.post_message_in_thread(c_id, msg_id, text="화이팅")
