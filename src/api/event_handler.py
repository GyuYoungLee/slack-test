"""
slack-sdk 이용 이벤트 답변 메시지 보내기

Event Subscriptions
  0. app token 발급
  1. uvicorn src.api.event_handler:app --reload
  2. ngrok http 8000 --region ap
  3. Request URL 등록
  4. 구독 이벤트 추가 => message.channels
  (유의 사항) 소켓 모드 활성화 시 동작하지 않는다
"""

from fastapi import FastAPI
from pydantic import BaseModel
from src.api.message_sender import SlackBot

app = FastAPI()
myBot = SlackBot()


class SlackRequest(BaseModel):
    token: str
    type: str
    challenge: str = None
    event: dict = None


@app.post("/slack")
async def hears(payload: SlackRequest) -> SlackRequest | None:
    if payload.challenge:
        return payload
    else:
        return event_handler(payload.event)


# hello 메시지 응답
def event_handler(event: dict) -> None:
    bot_user = "U037V772ZBQ"
    if event.get("user") == bot_user:
        return

    monitoring_words = ["hello", 'hi']
    if event.get("text").lower() in monitoring_words:
        myBot.post_message(channel_id=event.get("channel"), text="Hello... by slack-sdk 3.15.2")
