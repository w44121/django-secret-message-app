from secret_message.models import SecretMessage
from secret_message.tasks import dellete_secret_message


class SecretMessageHandler:
    def __init__(self, message: SecretMessage):
        self.message = message
        self.time_to_destroy = self.message.time_to_destroy
    
    def is_read_limit_over(self):
        return self.message.amount_to_read < 0
    
    def set_dellet_task(self):
        dellete_secret_message.apply_async(
                args=[self.message.id],
                countdown=self.message.time_to_destroy,
            )
