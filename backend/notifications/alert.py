from .notification import Notification
from typing import Tuple

class AlertNotification(Notification):
    def __init__(self, title: str, message: str, level: str = "CRITICAL", channel=None):
        super().__init__(title, message, channel)
        self.level = level

    def prepare_content(self) -> Tuple[str, str]:
        prepared_title = f"[ALERT - {self.level}] {self.title}"
        prepared_message = f"{self.message}\n\n-- Priority: {self.level} --"
        return prepared_title, prepared_message
