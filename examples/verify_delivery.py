from waclient import WhatsAppClient

# Use the credentials provided by the user
client = WhatsAppClient(
    phone_number_id="",
    access_token=""
)

# Try sending the standard 'hello_world' template which is pre-approved for all test accounts
print("Sending hello_world template...")
try:
    response = client.send_template(
        to="919342585854",
        template_name="hello_world",
        language="en_US"  # Standard test template often uses en_US
    )
    print(f"Template sent! ID: {response['messages'][0]['id']}")
except Exception as e:
    print(f"Failed to send template: {e}")


# Try sending the standard 'hello_world' template which is pre-approved for all test accounts
# print("Sending hello_world template...")
# try:
#     response = client.send_template(
#                 to="919342585854",
#                 template_name="order_confirmation",
#                 language="en",
#                 components=[{
#                     "type": "body",
#                     "parameters": [
#                         {"type": "text", "text": "Order123"},
#                         {"type": "text", "text": "₹499"}
#                     ]
#                 }]
#             )
#     print(f"Template sent! ID: {response['messages'][0]['id']}")
# except Exception as e:
#     print(f"Failed to send template: {e}")
