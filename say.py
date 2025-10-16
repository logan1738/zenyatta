from safe_send import safe_send
from discord_actions import get_guild
import constants

async def say_handler(message, client):
    rest = message.content[len("!say "):].strip()
    guild = await get_guild(client)
    chat_channel = guild.get_channel(constants.CHAT_CHANNEL)
    await safe_send(chat_channel, rest)