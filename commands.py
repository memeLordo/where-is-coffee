import asyncio

from telethon import events

from config import ASK_KEYS, bot


async def ask_for_keys(event):
    await event.respond(ASK_KEYS)
    await asyncio.sleep(1)
    pass


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
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
