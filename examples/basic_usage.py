"""
Basic usage examples for whatsapp-biz
"""

from waclient import WhatsAppClient

# Initialize client
client = WhatsAppClient(
    phone_number_id="461166093735990",
    access_token="EAAfLlnmBVq4BO75McWDhNHgL1DW9LKmdOCmLmlQbtjZBdEZCt65ub7z35gBW9gFiRjJpZC3LZA9cSTZC5Uw9lpxz3xGSyDai1FoKZAdqtRZA2huRNHrv3ymxfUljrQZAZCMs7zGEf7vzJLktSoLsZA83BHZBt9H3M06sl5ETgz4YZC7ToCBZASwnwAUC8gxGndieOSv5Y16oxhqTWPStgseH6"
)

# Example 1: Send text message
def send_simple_text():
    response = client.send_text(
        to="919342585854",
        message="Hello from WhatsApp Business API!"
    )
    print(f"Message sent! ID: {response['messages'][0]['id']}")


# Example 2: Send text with URL preview
def send_text_with_preview():
    response = client.send_text(
        to="919342585854",
        message="Check out this link: https://example.com",
        preview_url=True
    )
    print(f"Message sent with preview!")


# Example 3: Send image
def send_image():
    response = client.send_image(
        to="919342585854",
        image_url="https://example.com/image.jpg",
        caption="Check out this image!"
    )
    print(f"Image sent!")


# Example 4: Upload and send media
def upload_and_send():
    # Upload file first
    media_id = client.upload_media(
        file_path="/path/to/document.pdf",
        mime_type="application/pdf"
    )
    
    # Send using media ID
    response = client.send_document(
        to="919342585854",
        document_id=media_id,
        caption="Here's your document",
        filename="report.pdf"
    )
    print(f"Document sent!")


# Example 5: Send location
def send_location():
    response = client.send_location(
        to="919342585854",
        latitude=12.9716,
        longitude=77.5946,
        name="Bangalore",
        address="Bangalore, Karnataka, India"
    )
    print(f"Location sent!")


# Example 6: Send interactive buttons
def send_buttons():
    response = client.send_interactive(
        to="919342585854",
        interactive_type="button",
        body_text="What would you like to do?",
        buttons=[
            {"id": "option_1", "title": "View Products"},
            {"id": "option_2", "title": "Contact Support"},
            {"id": "option_3", "title": "Track Order"}
        ],
        header="Welcome!",
        footer="We're here to help"
    )
    print(f"Interactive message sent!")


# Example 7: Send list message
def send_list():
    response = client.send_interactive(
        to="919342585854",
        interactive_type="list",
        body_text="Choose a category:",
        button_text="View Categories",
        sections=[
            {
                "title": "Electronics",
                "rows": [
                    {"id": "phone", "title": "Phones"},
                    {"id": "laptop", "title": "Laptops"}
                ]
            },
            {
                "title": "Fashion",
                "rows": [
                    {"id": "men", "title": "Men's Wear"},
                    {"id": "women", "title": "Women's Wear"}
                ]
            }
        ]
    )
    print(f"List message sent!")


if __name__ == "__main__":
    # Run examples
    send_simple_text()
