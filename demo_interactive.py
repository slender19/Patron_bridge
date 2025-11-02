from channels.email import EmailChannel
from channels.sms import SmsChannel
from channels.push import PushChannel
from channels.whatsapp import WhatsAppChannel

from notifications.alert import AlertNotification
from notifications.reminder import ReminderNotification
from notifications.newsletter import NewsletterNotification

def pause():
    input("\nPresiona Enter para continuar al siguiente escenario...")

def run_interactive_demo():
    print("=== Demo Interactivo: NotiCorp Bridge Pattern ===\n")

    email = EmailChannel(smtp_server="smtp.noticorp.local")
    sms = SmsChannel(provider_name="UnstableSMS", force_result=False)
    push = PushChannel()
    whatsapp = WhatsAppChannel(api_url="https://whatsapp.api.local")

    # Escenario 1
    print("Escenario 1: Alert (primary: SMS, fallback: Email)")
    alert = AlertNotification("Server down", "The production server is unreachable.", level="CRITICAL", channel=sms)
    success = alert.send(fallback_channels=[email])
    print(f"Resultado: {'Delivered' if success else 'Failed'}")
    pause()

    # Escenario 2
    print("Escenario 2: Newsletter (primary: Email)")
    newsletter = NewsletterNotification("Weekly news", "This week: new features and improvements.", channel=email)
    success = newsletter.send()
    print(f"Resultado: {'Delivered' if success else 'Failed'}")
    pause()

    # Escenario 3
    print("Escenario 3: Reminder (primary: Push)")
    reminder = ReminderNotification("Payment due", "Your subscription payment is due tomorrow.", channel=push)
    success = reminder.send()
    print(f"Resultado: {'Delivered' if success else 'Failed'}")
    pause()

    # Escenario 4
    print("Escenario 4: Reminder (cambio de canal a WhatsApp en tiempo de ejecución)")
    reminder.set_channel(whatsapp)
    success = reminder.send()
    print(f"Resultado: {'Delivered' if success else 'Failed'}")
    print("\nDemo finalizado.")

if __name__ == "__main__":
    run_interactive_demo()
