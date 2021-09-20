# インポートするライブラリ
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
import os

# 軽量なウェブアプリケーションフレームワーク:Flask
app = Flask(__name__)

# 自分のアクセストークンとシークレットトークンを入れてください
YOUR_CHANNEL_ACCESS_TOKEN = 'N8zN4ZGx / L0pW7ZAp6Yf5WGQd69ge5adfBogY0maX1JmkUl4YsqylVUJBZWZVhaNh5KAbH / pAaci7rL3pauxEi0mr62kuBJli9WBnWQ6DiTSyTqG72rp5Yv'
YOUR_CHANNEL_SECRET = '74265d3b0eba822e91e2b7aa991e915a'

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/")
def hello_world():
    return "hello"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# MessageEvent
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= event.message.text)
  )


if __name__ == "__main__":
    port=os.getenv("PORT",5000)
    app.run(host="0.0.0.0", port=port)