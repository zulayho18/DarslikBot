from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TextbookViewSet

router = DefaultRouter()
router.register(r"textbooks", TextbookViewSet)  # textbooks/ ID bo‘yicha ishlaydi

urlpatterns = [
    path("", include(router.urls)),
]
