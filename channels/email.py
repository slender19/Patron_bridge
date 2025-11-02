from .delivery_channel import DeliveryChannel
from typing import Tuple
import time

class EmailChannel(DeliveryChannel):
    def __init__(self, smtp_server: str = "smtp.example.com"):
        self.smtp_server = smtp_server

    def deliver(self, title: str, message: str) -> Tuple[bool, str]:
        time.sleep(0.1)
        details = f"Email sent via {self.smtp_server}: {title}"
        print(f"[EmailChannel] {details}")
        return True, details
