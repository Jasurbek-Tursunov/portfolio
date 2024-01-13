from utils.helpers import send_message_telegram
# from core.celery import app


# @app.task
def admin_send_feedback(data):
    """ Sends feedback to Telegram admins """
    message = (
        f"🗒 %23feedback\n"
        f"\n<b>Name:</b> {data['name']}"
        f"\n<b>Email:</b> {data['email'].replace('@', '%40')}"
        f"\n<b>Text:</b> {data['text']}"
    )
    send_message_telegram(message=message)

