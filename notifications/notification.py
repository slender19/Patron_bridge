from abc import ABC, abstractmethod
from typing import Optional, List, Tuple
from channels.delivery_channel import DeliveryChannel

class Notification(ABC):

    def __init__(self, title: str, message: str, channel: Optional[DeliveryChannel] = None):
        self.title = title
        self.message = message
        self._channel = channel

    def set_channel(self, channel: DeliveryChannel) -> None:
        self._channel = channel

    @abstractmethod
    def prepare_content(self) -> Tuple[str, str]:
        raise NotImplementedError

    def send(self, fallback_channels: Optional[List[DeliveryChannel]] = None) -> bool:
    
        if self._channel is None:
            raise ValueError("No delivery channel configured for this notification.")

        title, message = self.prepare_content()
        success, details = self._channel.deliver(title, message)
        if success:
            return True

        if fallback_channels:
            for ch in fallback_channels:
                success, details = ch.deliver(title, message)
                if success:
                    return True

        return False
