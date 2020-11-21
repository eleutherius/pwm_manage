import asyncio
import websockets
import json

class WebSoketRunner:
    def __init__(self, engine: object, logger: object):
        self.engine = engine
        self.logger = logger

    async def consumer(self, message):
        output_list = json.loads(message)
        self.logger.debug(f'INPUT json: {output_list}')
        engine = self.engine(output_list).pwm_controller()


    async def websocket_server(self, websocket, path):
        async for message in websocket:
            await self.consumer(message)

    def start(self):
        start_server = websockets.serve(self.websocket_server, "127.0.0.1", 5685)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
