from .notification import Notification
from typing import Tuple

class ReminderNotification(Notification):
    def prepare_content(self) -> Tuple[str, str]:
        prepared_title = f"[Reminder] {self.title}"
        prepared_message = f"Don't forget: {self.message}"
        return prepared_title, prepared_message
