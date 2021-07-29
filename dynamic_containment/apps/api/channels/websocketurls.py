from django.urls import re_path

from apps.api.channels.some_consumer import SomeConsumer

websocket_urlpatterns = [
    re_path(r'ws/some-consumer/(?P<room_name>\w+)/$', SomeConsumer.as_asgi()),
]
