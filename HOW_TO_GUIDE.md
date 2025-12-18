
# 📘 WhatsApp Business API Integration Guide

This guide explains how to use the `waclient` package to send and receive messages using your specific credentials.

---

## 📦 0. Installation (Crucial First Step)

Because you downloaded the code, you need to install it in "editable" mode so Python can find the `waclient` package.

Run this command **once** in your terminal:

```bash
pip install -e .
```

---

## 🚀 1. Setup

Your project is already configured with the following credentials:
- **Phone Number ID:** `YOUR_PHONE_ID`
- **Phone Number:** `919342585854` (MyTestNumber)
- **Access Token:** `EAAfLlnmBVq4...` (configured in your scripts)

---

## 📨 2. Starting a Conversation

**Important:** WhatsApp prevents businesses from sending free-form text messages to users who haven't messaged them in the last 24 hours.

**To start a conversation:**
1. You must send a **Template Message** first.
2. The user must **REPLY** to that message.

### Verified Script
Run the verification script to send the initial "Hello World" template:

```bash
python verify_delivery.py
```

*Action:* Check your WhatsApp and reply "Hi" to the message you receive.

---

## 💬 3. Sending Messages

Once the 24-hour session window is open (after you reply), you can send any type of message.

### Run the Examples
We have prepared a script with multiple examples (Text, Image, Location, Buttons):

```bash
python examples/basic_usage.py
```

This script will:
- Send a text message ("Hello from WhatsApp Business API!")
- Send a link with preview
- Send an image
- Send a location (Bangalore)
- Send interactive buttons

---

## 🔗 4. Receiving Messages (Webhooks)

To receive messages from users, you need to run a webhook server.

### Start the Server
Run the handler script we prepared:

```bash
python examples/webhook_handler.py
```

*Note: This starts a local server at `http://localhost:5000`. To make this accessible to WhatsApp, you will need a tool like `ngrok` to expose it to the internet, or deploy it to a cloud server.*

### Configuration
Update `examples/webhook_handler.py` with your App Secret and Verify Token:

```python
webhook = WebhookHandler(
    app_secret="YOUR_REAL_APP_SECRET",
    verify_token="YOUR_REAL_VERIFY_TOKEN"
)
```

---

## 🛠️ 5. Common Issues

### "Message not delivered"
- **Cause:** 24-hour session window is closed.
- **Fix:** Run `python verify_delivery.py` to send a template, then reply to it on your phone.

### "Authentication failed"
- **Cause:** Access Token expired (temporary tokens last ~24 hours).
- **Fix:** Generate a new token in the Meta App Dashboard and update it in your scripts.

---
