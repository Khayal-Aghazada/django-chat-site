from django.urls import path , include
from Chatting.consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    path("" , ChatConsumer.as_asgi()) , 
] 