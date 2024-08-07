import asyncio

from loguru import logger
from telethon import events

from .config import Messages, bot
from .database.orm import ORM
from .errors import timeout_handler


@timeout_handler
async def ask_for_keys(event):
    async with bot.conversation(event.sender_id) as conv:
        # TODO: ass value check
        await conv.send_message(Messages.ASK_KEYS[0])
        _id = await conv.get_response()
        api_id = int(_id.message)

        await conv.send_message(Messages.ASK_KEYS[1])
        _hash = await conv.get_response()
        api_hash = _hash.message

        ORM.insert_user(event.sender_id, api_id, api_hash)
        # Continue with the conversation
        await conv.send_message("Done!")
    await asyncio.sleep(1)
    pass


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    # sender = await event.get_sender()
    logger.info(f"/start initiated by {event.sender.username}")
    # ask for keys
    # save keys into .env.client
    # login in client via .env.client
    # from the account start searching for chats
    # return links for chats
    if ORM.get_user(event.sender_id) is None:
        # ORM.insert_user(sender.id, 2, "102")
        logger.info("New user logged in.")
        logger.debug(f"User id: {event.sender_id}")
        await event.respond(Messages.ASK_LOGIN)
    # ORM.select_users()
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
