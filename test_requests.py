import os
from dotenv import load_dotenv

import requests

load_dotenv(verbose=True)


def notice_message(token, channel, text, attachments):
    r = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + token},
        json={"channel": channel,
              "text": text,
              "attachments": attachments})
    print(r.json())


secondary_attachments = [{
    "color": "#2eb886",
    'author_name': "신청일: 2022-03-23 10:00:00",
    'title': "경품 : 갤럭시",
    'text': "가맹점명: 홍길동 매장\n수령인: 홍길동\n배송지: 서울시 강남구"
}]

notice_message(
    token=os.environ["SLACK_BOT_TOKEN"],
    channel="C037S1C1TBR",
    text="[배송 신청]",
    attachments=secondary_attachments
)
