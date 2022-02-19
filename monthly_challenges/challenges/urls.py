from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.montly_challenge_by_number),
    path("<str:month>", views.montly_challenge, name="month-challenge"),
    re_path(r'^test/(?P<var>\D+)$', views.test),
]


