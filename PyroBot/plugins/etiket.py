from pyrogram import Client, filters
import asyncio
from pyrogram import TelegramClient, sync, events, utils, types, Button
from pyrogram.events import StopPropagation 

@Client.on_message(filters.command(["basla"]))
async def start(bot, update):

    chat_id=update.chat.id,

assert Client.start()

if not client.is_user_authorized():
     client.send_code_request(BOT_TOKEN)

for member in app.iter_chat_members("chat_id"):
    if not user.bot:
        if user.username != None:
            print(user.username)
            Mention.append(user.username)
        	
for etiket in Mention:
    await bot.send_message(event.chat_id, f"@{etiket} {reason}")
    Mention.remove(etiket)
    await sleep(0.5)

@Client.on_message(filters.command(["start"]))
async def deneme(bot, update):

assert Client.stop()