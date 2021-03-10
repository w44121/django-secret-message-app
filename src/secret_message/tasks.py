from app.celery import app
from secret_message.models import SecretMessage


@app.task(
    retry_kwargs={'countdown': 10}
)
def dellete_secret_message(message_id):
    message = SecretMessage.objects.get(id=message_id)
    message.delete()
