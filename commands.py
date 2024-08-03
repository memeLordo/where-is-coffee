from telethon import events

from config import bot


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.respond("Hi!")
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern="/search"))
async def search(event):
    # searching...
    pass


# @bot.on(events.NewMessage)
# async def echo(event):
#     await event.respond(event.text)
