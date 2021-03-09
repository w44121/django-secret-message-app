from django.urls import path
from secret_message.views import SecrteMessageCreateView, SecrteMessageDetailView


urlpatterns = [
    path("message/create/", SecrteMessageCreateView.as_view()),
    path("message/<int:pk>", SecrteMessageDetailView.as_view()),
]
