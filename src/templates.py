def get_template():
    return {
        "text": "CRITICAL: Issue encountered during snapshot creation",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": ":man-biking: new loading :man-biking:",
                    "emoji": True,
                },
            }
        ],
    }


def get_blocks():
    return [
        {"type": "header", "text": {"type": "plain_text", "text": "[배송 신청]"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "신청일: 2022-03-23 10:00:00"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "경품 : 갤럭시탭"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "가맹점명: 홍길동 매장"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "수령인: 홍길동"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "배송지: 서울시 강남구 대치동 세풍빌딩"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "핸드폰 번호: 010-4121-6147"}},
    ]


def get_secondary_attachments():
    return [{
        "color": "#2eb886",
        'author_name': "신청일: 2022-03-23 10:00:00",
        'title': "경품 : 갤럭시탭",
        'text': "가맹점명: 홍길동 매장\n수령인: 홍길동\n배송지: 서울시 강남구 대치동 세풍빌딩 XXX\n핸드폰 번호: 010-4121-6147",
    }]
