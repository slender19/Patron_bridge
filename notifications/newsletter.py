from .notification import Notification
from typing import Tuple

class NewsletterNotification(Notification):
    def prepare_content(self) -> Tuple[str, str]:
        prepared_title = f"[Newsletter] {self.title}"
        prepared_message = f"{self.message}\n\nManage preferences at our site."
        return prepared_title, prepared_message
