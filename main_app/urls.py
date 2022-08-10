from django.urls import path
from .views import CallsView

urlpatterns = [
    path('calls/', CallsView.as_view())
]
