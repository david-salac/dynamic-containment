import json
import time
from channels.generic.websocket import AsyncWebsocketConsumer


class SomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        for i in range(10):
            await self.send(text_data=json.dumps({
                'message-from-server': f'{self.scope["user"]} {message} {i}'
            }))

        await self.close()
