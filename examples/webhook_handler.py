from waclient.webhooks import WebhookHandler
from flask import Flask, request

app = Flask(__name__)
# Note: You need to configure these with your actual App Secret and Verify Token
webhook = WebhookHandler(
    app_secret="YOUR_APP_SECRET",
    verify_token="YOUR_VERIFY_TOKEN"
)

@app.route("/webhook", methods=["GET", "POST"])
def handle_webhook():
    if request.method == "GET":
        # Webhook verification
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        verified = webhook.verify_token(mode, token, challenge)
        return (challenge, 200) if verified else ("Forbidden", 403)
    
    # Handle incoming message
    signature = request.headers.get("X-Hub-Signature-256")
    try:
        webhook.verify_signature(signature, request.data)
    except Exception as e:
        print(f"Signature verification failed: {e}")
        return "Invalid Signature", 403
    
    message = webhook.parse_message(request.json)
    if message:
        print(f"From: {message['from']}")
        print(f"Text: {message.get('text')}")
    
    status = webhook.parse_status(request.json)
    if status:
        print(f"Status Update: {status['status']} for {status['recipient_id']}")
        if status.get('conversation'):
            print(f"Conversation ID: {status['conversation'].get('id')}")
    
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
