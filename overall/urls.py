from django.urls import path
from . import views

urlpatterns = [
    path('', views.TenMostFamousInstagrams.as_view(), name='ten_most_famous_instagrams'),
]