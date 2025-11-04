from .delivery_channel import DeliveryChannel
from typing import Tuple, Optional
import time
import random

class SmsChannel(DeliveryChannel):
    def __init__(self, provider_name: str = "FastSMS", force_result: Optional[bool] = None, fail_rate: float = 0.66):
   
        self.provider_name = provider_name
        self.force_result = force_result
        self.fail_rate = float(fail_rate)

    def deliver(self, title: str, message: str) -> Tuple[bool, str]:
        time.sleep(0.05)
        if self.force_result is True:
            ok = True
        elif self.force_result is False:
            ok = False
        else:
            ok = random.random() > self.fail_rate  

        if ok:
            details = f"SMS sent via {self.provider_name}: {title}"
            print(f"[SmsChannel] {details}")
            return True, details
        else:
            details = f"SMS provider {self.provider_name} failed"
            print(f"[SmsChannel] ERROR: {details}")
            return False, details
