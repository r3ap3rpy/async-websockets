import asyncio
import websocket
import ssl

async def message():
	ws = websocket.WebSocket(sslopt = {'cert_reqs':ssl.CERT_NONE})
	ws.connect('wss://localhost:1234')
	msg = input("The message to be sent: ")
	ws.send(msg)
	print(ws.recv())

asyncio.get_event_loop().run_until_complete(message())