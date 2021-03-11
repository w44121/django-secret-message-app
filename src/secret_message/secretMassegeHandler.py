from secret_message.models import SecretMessage
from secret_message.tasks import dellete_secret_message


class SecretMessageHandler:
    def __init__(self, message: SecretMessage):
        self.message = message
        self.time_to_destroy = self.message.time_to_destroy
    
    def set_dellet_task(self):
        dellete_secret_message.apply_async(
                args=[self.message.id],
                countdown=self.message.time_to_destroy,
            )
