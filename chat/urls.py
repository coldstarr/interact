from django.urls import path, include
from .views import ChatPageView, HomePageView, RandomTokenView
 
 
urlpatterns = [
    path("chat/", ChatPageView.as_view(), name="chat-page"),
    path("", HomePageView.as_view(), name="home-page"),
    path('get_token/', RandomTokenView.as_view(), name='get_token')
]