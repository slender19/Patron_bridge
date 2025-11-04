
from channels.email import EmailChannel
from channels.sms import SmsChannel
from channels.push import PushChannel
from channels.whatsapp import WhatsAppChannel

from notifications.alert import AlertNotification
from notifications.reminder import ReminderNotification
from notifications.newsletter import NewsletterNotification

import random
import sys
import os

def run_demo():
    print("=== Demo: NotiCorp Bridge Pattern ===\n")

    email = EmailChannel(smtp_server="smtp.noticorp.local")
    sms = SmsChannel(provider_name="UnstableSMS")  
    push = PushChannel()
    whatsapp = WhatsAppChannel(api_url="https://whatsapp.api.local")

    # 1) AlertNotification sent via SMS with fallback to Email
    alert = AlertNotification("Server down", "The production server is unreachable.", level="CRITICAL", channel=sms)
    print("-> Sending Alert (primary: SMS, fallback: Email)")
    success = alert.send(fallback_channels=[email])
    print(f"Result: {'Delivered' if success else 'Failed'}\n")

    # 2) Newsletter sent via Email (no fallback)
    newsletter = NewsletterNotification("Weekly news", "This week: new features and improvements.", channel=email)
    print("-> Sending Newsletter (primary: Email)")
    success = newsletter.send()
    print(f"Result: {'Delivered' if success else 'Failed'}\n")

    # 3) Reminder sent via Push
    reminder = ReminderNotification("Payment due", "Your subscription payment is due tomorrow.", channel=push)
    print("-> Sending Reminder (primary: Push)")
    success = reminder.send()
    print(f"Result: {'Delivered' if success else 'Failed'}\n")

    # 4) Demonstrate switching channel at runtime
    reminder.set_channel(whatsapp)
    print("-> Sending Reminder (switched to WhatsApp at runtime)")
    success = reminder.send()
    print(f"Result: {'Delivered' if success else 'Failed'}\n")

if __name__ == "__main__":
    run_demo()
