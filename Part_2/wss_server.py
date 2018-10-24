import ssl
import pathlib
import asyncio
import websockets

async def response(websocket, path):
	message = await websocket.recv()
	print(f"We got the message from the client: {message}")
	await websocket.send("I can confirm I got your message!")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(pathlib.Path(__file__).with_name('mycert.pem'), keyfile = pathlib.Path(__file__).with_name('mykey.key'))


start_server = websockets.serve(response, 'localhost', 1234, ssl = ssl_context)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()