"""
slack Web API 로 blocks 메시지, secondary_attachments 메시지 보내기
"""

import json
import os
from dotenv import load_dotenv

import requests
from src.templates import get_blocks, get_secondary_attachments

load_dotenv(verbose=True)


def notice_message(token, channel, text, blocks, attachments):
    slack_api_url = "https://slack.com/api/chat.postMessage"
    blocks = json.dumps(blocks)
    attachments = json.dumps(attachments)

    requests.post(
        slack_api_url,
        headers={"Authorization": "Bearer " + token},
        data={"channel": channel, "text": text, "blocks": blocks, "attachments": attachments})


if __name__ == "__main__":
    test_text = "[배송 신청]"
    test_blocks = get_blocks()
    test_secondary_attachments = get_secondary_attachments()

    notice_message(
        token=os.environ["SLACK_BOT_TOKEN"],
        channel="C037S1C1TBR",
        text=test_text,
        blocks=test_blocks,
        attachments=test_secondary_attachments,
    )
