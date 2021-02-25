from django.urls import path

from .views import TestView


urlpatterns = [
    path('test_view/', TestView.as_view()),
]
