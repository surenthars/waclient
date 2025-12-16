from waclient import WhatsAppClient
from waclient.messages import TemplateBuilder

client = WhatsAppClient(
    phone_number_id="461166093735990",
    access_token="EAAfLlnmBVq4BO75McWDhNHgL1DW9LKmdOCmLmlQbtjZBdEZCt65ub7z35gBW9gFiRjJpZC3LZA9cSTZC5Uw9lpxz3xGSyDai1FoKZAdqtRZA2huRNHrv3ymxfUljrQZAZCMs7zGEf7vzJLktSoLsZA83BHZBt9H3M06sl5ETgz4YZC7ToCBZASwnwAUC8gxGndieOSv5Y16oxhqTWPStgseH6"
)

# Example 1: Simple template with body parameters
def send_order_confirmation():
    response = client.send_template(
        to="919342585854",
        template_name="order_confirmation",
        language="en",
        components=[
            TemplateBuilder.body_parameters(
                "ORD12345",  # Order number
                "₹2,499"     # Amount
            )
        ]
    )
    print("Order confirmation sent!")


# Example 2: Template with header image
def send_promo_with_image():
    response = client.send_template(
        to="919342585854",
        template_name="sale_promotion",
        language="en",
        components=[
            TemplateBuilder.header_image(
                image_url="https://example.com/sale-banner.jpg"
            ),
            TemplateBuilder.body_parameters(
                "50% OFF",
                "Weekend Sale"
            )
        ]
    )
    print("Promo sent!")


# Example 3: Template with button URL
def send_invoice_with_link():
    response = client.send_template(
        to="919342585854",
        template_name="invoice_ready",
        language="en",
        components=[
            TemplateBuilder.body_parameters("INV-2024-001"),
            TemplateBuilder.button_url(0, "INV-2024-001")  # URL suffix
        ]
    )
    print("Invoice notification sent!")

