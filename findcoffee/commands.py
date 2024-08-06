import asyncio

from loguru import logger
from telethon import events

from .config import Messages, bot


async def ask_for_keys(event):
    await event.respond(Messages.ASK_KEYS)
    await asyncio.sleep(1)
    pass


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    sender = await event.get_sender()
    logger.info(f"/start initiated by {sender.first_name}")
    # ask for keys
    # save keys into .env.client
    # login in client via .env.client
    # from the account start searching for chats
    # return links for chats

    # if check_db(event.sender_id):
    #     logger.info("New user logged in.")
    #     logger.debug(f"User id: {event.sender_id}")
    #     await event.respond(Messages.ASK_LOGIN)
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern="/search"))
async def search(event):
    # searching...
    pass


@bot.on(events.NewMessage(pattern="/help"))
async def help(event):
    # display help...
    pass


@bot.on(events.NewMessage(pattern="/login"))
async def login(event):
    # logging in...
    await ask_for_keys(event)
    pass


# @bot.on(events.NewMessage)
# async def echo(event):
#     await event.respond(event.text)
