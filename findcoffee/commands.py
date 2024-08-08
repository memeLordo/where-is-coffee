from loguru import logger
from telethon import events

from .config import Message, bot
from .database.orm import ORM
from .errors import timeout_handler, value_error_handler

commands = {
    "/start": "message",
    "/login": "message",
    "/search": "message",
    "/help": "message",
    "/exit": "message",
}


async def create_client(event):
    print(ORM.get_user_by(event.sender_id))
    pass

@timeout_handler

@value_error_handler
async def ask_for_keys(event):
    async with bot.conversation(event.sender) as conv:
        timeout = 60
        await conv.send_message(Message.KEYS[0])
        _id = await conv.get_response(timeout=timeout)
        api_id = int(_id.message)

        await conv.send_message(Message.KEYS[1])
        _hash = await conv.get_response(timeout=timeout)
        api_hash = _hash.message

        ORM.insert_user(event.sender_id, api_id, api_hash)
        # Continue with the conversation
        await conv.send_message("Done!")


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    # sender = await event.get_sender()
    logger.info(f"{event.sender.username}:called /start command")
    # ask for keys
    # save keys into .env.client
    # login in client via .env.client
    # from the account start searching for chats
    # return links for chats
    if ORM.get_user(event.sender_id) is None:
        # ORM.insert_user(sender.id, 2, "102")
        logger.info("New user logged in.")
        logger.debug(f"User id: {event.sender_id}")
        await event.respond(Message.LOGIN)
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


@bot.on(events.NewMessage(pattern="/exit"))
async def exit(event, func_name="Comand"):
    async with bot.conversation(event.sender, exclusive=False) as conv:
        await conv.cancel_all()
        logger.info(f"{func_name}: aborted.")
        await event.respond("Operation is cancelled.")


# @bot.on(events.NewMessage)
# async def echo(event):
#     await event.respond(event.text)
