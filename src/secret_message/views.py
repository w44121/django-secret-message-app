from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from secret_message.models import SecrteMessage
from secret_message.serializers import SecrteMessageSerializer
from secret_message.tasks import dellete_secret_massage


class SecrteMessageCreateView(APIView):
    def post(self, request):
        serializer = SecrteMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            dellete_secret_massage.apply_async(
                args=[serializer.data["id"]],
                countdown=serializer.data["time_to_destroy"],
            )
            return Response(serializer.data)
        return Response(serializer.errors)


class SecrteMessageDetailView(APIView):
    def get(self, request, pk):
        try:
            secret_massage = SecrteMessage.objects.get(pk=pk)
        except SecrteMessage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SecrteMessageSerializer(secret_massage)
        return Response(serializer.data)
