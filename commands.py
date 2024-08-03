import asyncio

# import pandas as pd
from telethon import events

from config import ASK_KEYS, bot


def check_db():
    pass


async def ask_for_keys(event):
    await event.respond(ASK_KEYS)
    await asyncio.sleep(1)
    pass


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    check_db()
    # ask for keys
    # save keys into .env.client
    # login in client via .env.client
    # from the account start searching for chats
    # return links for chats
    await ask_for_keys(event)
    await event.respond("Hi!")
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern="/search"))
async def search(event):
    # searching...
    pass


# @bot.on(events.NewMessage)
# async def echo(event):
#     await event.respond(event.text)
