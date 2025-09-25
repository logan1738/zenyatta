

from dbd.base_commands.username import dbd_username_handler
from safe_send import safe_send


async def route_dbd_message(client, db, message, lower_message):

    if lower_message.startswith('!username'):
        await dbd_username_handler(db, message, client)

    else:
        await safe_send(message.channel, 'Invalid command. Please see **!help** for a list of commands.')