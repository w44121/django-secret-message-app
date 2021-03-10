from django.urls import path
from secret_message.views import SecretMessageCreateView, SecretMessageDetailView


urlpatterns = [
    path("message/", SecretMessageCreateView.as_view()),
    path("message/<int:pk>", SecretMessageDetailView.as_view()),
]
