from flask import Flask, request, make_response
import os
import json
import requests

app = Flask(__name__)
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_URL = "https://slack.com/api/chat.postMessage"

@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json

    # 初回URL確認用
    if data.get("type") == "url_verification":
        return make_response(data.get("challenge"), 200, {"content_type": "text/plain"})

    # イベント受信処理
    if data.get("type") == "event_callback":
        event = data.get("event", {})
        if event.get("type") == "message" and "bot_id" not in event:
            channel = event["channel"]
            text = event["text"]

            # # オウム返しメッセージ送信
            # response = requests.post(SLACK_URL, headers={
            #     "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            #     "Content-Type": "application/json"
            # }, json={
            #     "channel": channel,
            #     "text": f"🦜 {text}"
            # })

    return make_response("OK", 200)

if __name__ == "__main__":
    # ポートとホストを指定してアプリを起動
    app.run(host='0.0.0.0', port=5000)
