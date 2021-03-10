from rest_framework import serializers
from secret_message.models import SecretMessage


class SecretMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretMessage
        fields = "__all__"
