# WhatsApp Biz - User Manual

Welcome to the **WhatsApp Biz** User Manual. This guide provides detailed instructions on how to install, configure, and use the `waclient` package to integrate WhatsApp Business Cloud API into your Python applications.

## Table of Contents
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Quick Start](#quick-start)
4. [Sending Messages](#sending-messages)
    - [Text Messages](#text-messages)
    - [Media Messages](#media-messages)
    - [Interactive Messages](#interactive-messages)
    - [Template Messages](#template-messages)
    - [Location & Contacts](#location--contacts)
5. [Media Management](#media-management)
6. [Error Handling](#error-handling)

## Installation

Install the package via pip:

```bash
pip install waclient
```

## Configuration

You need a Meta for Developers account and a WhatsApp Business App set up. You will need:
- **Phone Number ID**
- **Business Account ID**
- **Access Token** (System User Token recommended for production)

### Environment Variables (Recommended)
Store your credentials securely. You can use a `.env` file or export them in your shell.

```python
import os

WHATSAPP_PHONE_ID = os.getenv("WHATSAPP_PHONE_ID")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
```

## Quick Start

Initialize the client and send a simple text message.

```python
from waclient import WhatsAppClient

# Initialize Client
client = WhatsAppClient(
    phone_number_id="YOUR_PHONE_NUMBER_ID",
    access_token="YOUR_ACCESS_TOKEN"
)

# Send 'Hello World'
response = client.messages.send_text(
    to="PHONE_NUMBER_WITH_COUNTRY_CODE", # e.g., "15551234567"
    body="Hello World from WhatsApp Biz!"
)

print(response)
```

## Sending Messages

### Text Messages
Send simple text messages with preview url support.

```python
client.messages.send_text(
    to="15551234567",
    body="Check out this link: https://www.google.com",
    preview_url=True
)
```

### Media Messages
Send images, documents, audio, videos, or stickers. You can send via **Media ID** (uploaded previously) or **Link**.

**Using a Link:**
```python
# Send Image
client.messages.send_image(
    to="15551234567",
    link="https://example.com/image.jpg",
    caption="Here is an image!"
)

# Send Document
client.messages.send_document(
    to="15551234567",
    link="https://example.com/brochure.pdf",
    caption="Project Brochure",
    filename="brochure.pdf"
)
```

### Interactive Messages
Send buttons or list messages for better user engagement.

**Reply Buttons (Quick Replies):**
```python
from waclient.models import Button

buttons = [
    Button(id="yes_btn", title="Yes"),
    Button(id="no_btn", title="No")
]

client.messages.send_reply_buttons(
    to="15551234567",
    body="Do you accept the terms?",
    buttons=buttons
)
```

**List Messages:**
```python
from waclient.models import Section, Row

rows = [
    Row(id="opt1", title="Option 1", description="Description 1"),
    Row(id="opt2", title="Option 2", description="Description 2")
]
section = Section(title="Main Menu", rows=rows)

client.messages.send_list(
    to="15551234567",
    body="Please select an option",
    button_text="Menu",
    sections=[section]
)
```

### Template Messages
Send approved templates (required for initiating conversations).

```python
from waclient.models import Component, Parameter

# Example: sending a template 'hello_world'
client.messages.send_template(
    to="15551234567",
    name="hello_world",
    language="en_US"
)
```

### Location & Contacts

**Send Location:**
```python
client.messages.send_location(
    to="15551234567",
    latitude=37.7749,
    longitude=-122.4194,
    name="San Francisco",
    address="CA, USA"
)
```

## Media Management

Upload media to WhatsApp servers to get a Media ID. This is useful for reuse.

```python
# Upload Media
file_path = "/path/to/image.jpg"
with open(file_path, "rb") as f:
    media_id = client.media.upload_media(
        file=f,
        type="image/jpeg",
        messaging_product="whatsapp"
    )
print(f"Uploaded Media ID: {media_id}")

# Send using Media ID
client.messages.send_image(
    to="15551234567",
    media_id=media_id,
    caption="Sent via Media ID"
)
```

## Error Handling

The library raises exceptions for API errors.

```python
from waclient.exceptions import WhatsAppError

try:
    client.messages.send_text(to="123", body="test")
except WhatsAppError as e:
    print(f"Error: {e}")
```

For more details, please refer to the [Developer Guide](DEVELOPER_GUIDE.md).
