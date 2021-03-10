from app.celery import app
from secret_message.models import SecrteMessage


@app.task(
    retry_kwargs={'countdown': 10}
)
def dellete_secret_massage(message_id):
    message = SecrteMessage.objects.get(id=message_id)
    message.delete()
