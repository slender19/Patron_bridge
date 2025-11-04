from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

from channels.email import EmailChannel
from channels.sms import SmsChannel
from channels.push import PushChannel
from channels.whatsapp import WhatsAppChannel

from notifications.alert import AlertNotification
from notifications.reminder import ReminderNotification
from notifications.newsletter import NewsletterNotification

app = FastAPI(title="NotiCorp Bridge Demo")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NotificationRequest(BaseModel):
    type: str
    primary: str
    fallback: Optional[str] = None
    title: str
    message: str

@app.post("/send")
def send_notification(data: NotificationRequest):
    logs: List[str] = []

    def log(msg):
        print(msg)
        logs.append(msg)

    channels = {
        "email": EmailChannel("smtp.noticorp.local"),
        "sms": SmsChannel(provider_name="UnstableSMS", force_result=False),
        "push": PushChannel(),
        "whatsapp": WhatsAppChannel("https://whatsapp.api.local")
    }

    primary = channels.get(data.primary)
    fallback = channels.get(data.fallback) if data.fallback else None

    notif_types = {
        "alert": AlertNotification,
        "reminder": ReminderNotification,
        "newsletter": NewsletterNotification,
    }

    NotificationClass = notif_types.get(data.type)
    if not NotificationClass:
        return {"success": False, "log": ["Tipo de notificación no válido"]}

    notif = NotificationClass(data.title, data.message, channel=primary)
    log(f"-> Sending {data.type.title()} (primary: {data.primary.upper()})")

    success = notif.send(fallback_channels=[fallback] if fallback else None)
    result = "Delivered" if success else "Failed"
    log(f"Result: {result}")

    return {"success": success, "log": logs}