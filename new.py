import asyncio
from starlette.applications import Starlette
from starlette.routing import WebSocketRoute

print("initialize...")

async def detect(websocket):
    try:
        await websocket.accept()
        for i in range(100):
            payload = f'Tes ini {i}'
            print(payload)
            await websocket.send_text(payload)
            await asyncio.sleep(2) 
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()

routes = [
    WebSocketRoute("/pri", endpoint=detect)
]

app = Starlette(routes=routes)
