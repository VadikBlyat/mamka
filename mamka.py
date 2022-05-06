import asyncio
import requests
import random
import json
from time import sleep
from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser, MessageMediaDocument, PeerChannel, MessageMediaPhoto, InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest

api_id = #сюда пихай апи айди
api_hash = '' # Сюда пихай хеш апи

client = TelegramClient('data', api_id, api_hash, device_model="Iphone", system_version="6.12.0",
                        app_version="10 P (28)")

client.start()

chats = []
last_date = None
chunk_size = 200
groups = []

results = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0))
chats.extend(results.chats)

for i in chats:
    try:
        if i.megagroup == True:
            groups.append(i)
    except:
    	pass

chat = []
for i in groups:
	chat.append(i.id)

print(chat)

@client.on(events.NewMessage(chats = chat))
async def handler(event):
    with open('base.json', 'r', encoding='UTF-8') as t:
        text = json.load(t)
        i = random.choice(text['curses'])
    if str(event.from_id.user_id) in str(1013595259):
        await event.reply(i)
    else:
        pass




client.run_until_disconnected()