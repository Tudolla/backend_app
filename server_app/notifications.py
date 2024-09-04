# tasks.py
from celery import shared_task
from firebase_admin import messaging

@shared_task
def send_notification_to_user(message_title, message_body, topic='global'):
    message = messaging.Message(
        notification=messaging.Notification(
            title=message_title,
            body=message_body,
        ),
        topic=topic,
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)
