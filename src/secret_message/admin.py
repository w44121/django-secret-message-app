from django.contrib import admin
from secret_message.models import SecretMessage


admin.site.register([SecretMessage])
