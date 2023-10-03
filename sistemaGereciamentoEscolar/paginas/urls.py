from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), ),  # Use as_view() method here
]
