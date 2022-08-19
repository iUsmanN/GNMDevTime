from django.urls import path
from django.conf.urls import url, include

from .views import AllRecordsView, Record
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("records/", AllRecordsView.as_view())
]