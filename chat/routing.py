from django.urls import re_path , include
from chat.consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    re_path(r'ws/(?P<room_name>\w+)/(?P<username>[\w.@+-]+)/(?P<token>[\w.@+-]+)/$', ChatConsumer.as_asgi()),
]


