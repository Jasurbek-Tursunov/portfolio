from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.helpers import send_message_telegram
from ..models import Message


@receiver(post_save, sender=Message)
def admin_send_feedback(sender, instance, **kwargs):
    """ Sends feedback to Telegram admins """
    message = (
        f"🗒 %23feedback\n"
        f"\n<b>Name:</b> {instance.name}"
        f"\n<b>Email:</b> {str(instance.email).replace('@', '%40')}"
        f"\n<b>Text:</b> {instance.text}"
    )
    send_message_telegram(message=message)
