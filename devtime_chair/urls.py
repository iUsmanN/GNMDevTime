from django.urls import path
from django.conf.urls import url, include

from .views import AllRecordsView, Record, RecordView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("all/", AllRecordsView.as_view()),
    path("add/", RecordView.as_view())
]