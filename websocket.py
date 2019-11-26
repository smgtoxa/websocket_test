import asyncio
import websockets


async def test(websocket, path):
    while True:
        await websocket.send("Test")
        test_message = await websocket.recv()
        print(f"< {test_message}")

start_server = websockets.serve(test, "127.0.0.1", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()