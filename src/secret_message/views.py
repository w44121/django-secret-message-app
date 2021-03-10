from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from secret_message.models import SecretMessage
from secret_message.serializers import SecretMessageSerializer
from secret_message.tasks import dellete_secret_message
from secret_message.secretMassegeHandler import SecretMessageHandler


class SecretMessageCreateView(APIView):
    def post(self, request):
        serializer = SecretMessageSerializer(data=request.data)
        if serializer.is_valid():
            secret_massage = serializer.save()
            # dellete_secret_massage.apply_async(
            #     args=[serializer.data["id"]],
            #     countdown=serializer.data["time_to_destroy"],
            # )
            SecretMessageHandler(secret_massage).set_dellet_task()
            return Response(serializer.data)
        return Response(serializer.errors)


class SecretMessageDetailView(APIView):
    def get(self, request, pk):
        try:
            secret_massage = SecretMessage.objects.get(pk=pk)
        except SecretMessage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SecretMessageSerializer(secret_massage)
        return Response(serializer.data)
