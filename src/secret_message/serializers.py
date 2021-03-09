from rest_framework import serializers
from secret_message.models import SecrteMessage


class SecrteMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecrteMessage
        fields = "__all__"
