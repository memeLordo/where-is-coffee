from telethon import events

from config import bot


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.respond("Hi!")
    raise events.StopPropagation


# @bot.on(events.NewMessage)
# async def echo(event):
#     await event.respond(event.text)


def main():
    """Start the bot."""
    bot.run_until_disconnected()


if __name__ == "__main__":
    main()
