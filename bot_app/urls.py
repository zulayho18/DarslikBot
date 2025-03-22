from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BotUserViewSet

router = DefaultRouter()
router.register(r'bot-users', BotUserViewSet)  # `bot-users` API

urlpatterns = [
    path('', include(router.urls)),
]






