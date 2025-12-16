import os
import time
from waclient import WhatsAppClient
from waclient.media import MediaHandler
from datetime import datetime

# Use the credentials provided by the user (using same credentials as verify_delivery.py)
client = WhatsAppClient(
    phone_number_id="461166093735990",
    access_token="EAAfLlnmBVq4BO75McWDhNHgL1DW9LKmdOCmLmlQbtjZBdEZCt65ub7z35gBW9gFiRjJpZC3LZA9cSTZC5Uw9lpxz3xGSyDai1FoKZAdqtRZA2huRNHrv3ymxfUljrQZAZCMs7zGEf7vzJLktSoLsZA83BHZBt9H3M06sl5ETgz4YZC7ToCBZASwnwAUC8gxGndieOSv5Y16oxhqTWPStgseH6"
)

recipient_number = "919342585854"

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def test_media_upload():
    log("--- Testing Media Upload ---")
    
    # Create a dummy image file (using text content disguised as .txt for simplicity, 
    # but let's try to be proper and use a real small text file first)
    filename = "test_upload_sample.txt"
    with open(filename, "w") as f:
        f.write("This is a test file for WhatsApp Business API Media Upload.")
    
    try:
        log(f"Uploading {filename}...")
        handler = MediaHandler(client)
        media_id = handler.upload(filename, "text/plain")
        log(f"Upload Successful! Media ID: {media_id}")
        
        log("Getting Media URL...")
        url = handler.get_url(media_id)
        log(f"Media URL Retrieved: {url[:50]}...") # Truncate for display
        
        return media_id
    except Exception as e:
        log(f"Media Upload Failed: {e}")
        return None
    finally:
        if os.path.exists(filename):
            os.remove(filename)

def test_text_message():
    log("\n--- Testing Text Message ---")
    try:
        response = client.send_text(
            to=recipient_number,
            message="Hello! This is an automated feature test from verify_features.py"
        )
        log(f"Text Message Sent! ID: {response['messages'][0]['id']}")
    except Exception as e:
        log(f"Text Message Failed: {e}")

def test_document_message(media_id):
    log("\n--- Testing Document Message (using uploaded media) ---")
    if not media_id:
        log("Skipping Document Message test (No Media ID)")
        return

    try:
        response = client.send_document(
            to=recipient_number,
            document_id=media_id,
            caption="Here is the test document you uploaded",
            filename="test_upload_sample.txt"
        )
        log(f"Document Message Sent! ID: {response['messages'][0]['id']}")
    except Exception as e:
        log(f"Document Message Failed: {e}")

def test_interactive_message():
    log("\n--- Testing Interactive Message (Buttons) ---")
    try:
        buttons = [
            {"id": "btn_yes", "title": "Yes"},
            {"id": "btn_no", "title": "No"}
        ]
        
    
        response = client.send_interactive(
            to=recipient_number,
            interactive_type="button",
            body_text="Do you like this test?",
            buttons=buttons,
            header="Feature Test",
            footer="Automated Verification"
        )
        log(f"Interactive Message Sent! ID: {response['messages'][0]['id']}")
    except Exception as e:
        log(f"Interactive Message Failed: {e}")

def test_video_message():
    log("\n--- Testing Video Message ---")
    try:
        # Using a public sample video URL
        video_url = "https://download.samplelib.com/mp4/sample-5s.mp4" 
        response = client.send_video(
            to=recipient_number,
            video_url=video_url,
            caption="This is a test video message"
        )
        log(f"Video Message Sent! ID: {response['messages'][0]['id']}")
    except Exception as e:
        log(f"Video Message Failed: {e}")

def test_audio_message():
    log("\n--- Testing Audio Message ---")
    try:
        # Using a public sample audio URL
        audio_url = "https://www.w3schools.com/lib/sound.mp3"
        response = client.send_audio(
            to=recipient_number,
            audio_url=audio_url
        )
        log(f"Audio Message Sent! ID: {response['messages'][0]['id']}")
    except Exception as e:
        log(f"Audio Message Failed: {e}")

def test_location_message():
    log("\n--- Testing Location Message ---")
    try:
        response = client.send_location(
            to=recipient_number,
            latitude=37.4847,
            longitude=-122.1477,
            name="Meta Headquarters",
            address="1 Hacker Way, Menlo Park, CA 94025"
        )
        log(f"Location Message Sent! ID: {response['messages'][0]['id']}")
    except Exception as e:
        log(f"Location Message Failed: {e}")

def test_contacts_message():
    log("\n--- Testing Contacts Message ---")
    try:
        contacts = [{
            "name": {
                "formatted_name": "Test Contact",
                "first_name": "Test",
                "last_name": "Contact"
            },
            "phones": [{
                "phone": "+1234567890",
                "type": "WORK"
            }]
        }]
        response = client.send_contacts(
            to=recipient_number,
            contacts=contacts
        )
        log(f"Contacts Message Sent! ID: {response['messages'][0]['id']}")
    except Exception as e:
        log(f"Contacts Message Failed: {e}")

def main():
    log("Starting Feature Verification...")
    
    # 1. Media Test
    media_id = test_media_upload()
    
    # 2. Text Message
    test_text_message()
    
    # 3. Document Message (reusing media)
    test_document_message(media_id)
    
    # 4. Interactive Message
    test_interactive_message()
    
    # 5. Video Message
    test_video_message()
    
    # 6. Audio Message
    test_audio_message()
    
    # 7. Location Message
    test_location_message()
    
    # 8. Contacts Message
    test_contacts_message()
    
    log("\nVerification Complete.")

if __name__ == "__main__":
    main()
