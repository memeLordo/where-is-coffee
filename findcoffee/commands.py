from loguru import logger
from telethon import TelegramClient, events

from .config import Message, bot
from .database.model import UserORM
from .database.orm import ORM
from .errors import timeout_handler, value_error_handler

commands = {
    "/start": "message",
    "/login": "message",
    "/search": "message",
    "/help": "message",
    "/exit": "message",
}


async def find_bot():
    pass


async def create_client(event):
    global client
    user = ORM.get_user_by(event.sender_id)
    # logger.debug(user)
    phone = "Some phone."
    client = TelegramClient("./sessions/client", user.api_id, user.api_hash)
    async with bot.conversation(event.sender) as conv:
        await conv.send_message("Please enter your code.")
        await client.connect()

        await client.send_code_request(phone)
        _code = await conv.get_response()
        code = _code.message
        assert code not in commands.keys()
        # telethon.errors.rpcerrorlist.PhoneCodeInvalidError
        # ConnectionError
        # possible auth errors: https://tl.telethon.dev/methods/auth/send_code.html
        await client.sign_in(phone, code)


@timeout_handler
@value_error_handler
async def ask_for_keys(event):
    async with bot.conversation(event.sender) as conv:
        timeout = 60
        await conv.send_message(Message.KEYS[0])
        _id = await conv.get_response(timeout=timeout)
        assert _id.message not in commands.keys()
        api_id = int(_id.message)

        await conv.send_message(Message.KEYS[1])
        _hash = await conv.get_response(timeout=timeout)
        assert _hash.message not in commands.keys()
        api_hash = _hash.message

        ORM.insert_user(event.sender_id, api_id, api_hash)
        # Continue with the conversation
        await conv.send_message("Done!")  # TODO: change to Message.KEYS[2]


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    # sender = await event.get_sender()
    logger.info(f"{event.sender.username}:called /start command")
    # ask for keys
    # save keys into .env.client
    # login in client via .env.client
    # from the account start searching for chats
    # return links for chats
    if ORM.is_user_exist(event.sender_id):
        return
        # ORM.insert_user(sender.id, 2, "102")
    logger.info("New user logged in.")
    logger.debug(f"User id: {event.sender_id}")
    await event.respond(Message.LOGIN)
    # ORM.select_users()
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern="/search"))
async def search(event):
    # searching...
    await create_client(event)
    # client.start()
    # with client:
    #     client.loop.run_until_complete(find_bot())


@bot.on(events.NewMessage(pattern="/help"))
async def help(event):
    # display help...
    pass


@bot.on(events.NewMessage(pattern="/login"))
async def login(event):
    # logging in...
    logger.debug(ORM.is_user_exist(event.sender_id))
    if ORM.is_user_exist(event.sender_id):
        await event.respond("You are already have an account.")
    else:
        await ask_for_keys(event)
    await create_client(event)


@bot.on(events.NewMessage(pattern="/exit"))
async def exit(event, func_name="Comand"):
    async with bot.conversation(event.sender, exclusive=False) as conv:
        await conv.cancel_all()
        logger.info(f"{func_name}: aborted.")
        await event.respond("Operation is cancelled.")


# @bot.on(events.NewMessage)
# async def echo(event):
#     await event.respond(event.text)
