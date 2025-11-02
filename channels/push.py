from .delivery_channel import DeliveryChannel
from typing import Tuple
import time

class PushChannel(DeliveryChannel):
    def deliver(self, title: str, message: str) -> Tuple[bool, str]:
        time.sleep(0.05)
        details = f"Push notification delivered: {title}"
        print(f"[PushChannel] {details}")
        return True, details
