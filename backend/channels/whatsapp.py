from .delivery_channel import DeliveryChannel
from typing import Tuple
import time

class WhatsAppChannel(DeliveryChannel):
    def __init__(self, api_url: str = "https://whatsapp.example.api"):
        self.api_url = api_url

    def deliver(self, title: str, message: str) -> Tuple[bool, str]:
        time.sleep(0.1)
        details = f"WhatsApp message sent via {self.api_url}: {title}"
        print(f"[WhatsAppChannel] {details}")
        return True, details
