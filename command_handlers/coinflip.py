

from random import random

from safe_send import safe_send


async def coinflip_handler(message):

    params = message.content.split()

    if len(params) != 1 and len(params) != 3:
        await safe_send(message.channel, 'Usage: **!coinflip** OR **!coinflip Option1 Option2**')
        return
    
    if len(params) == 1:
        result = random.choice(['Heads', 'Tails'])
        await safe_send(message.channel, f'The result is **{result}**')
        return
    
    option1 = params[1]
    option2 = params[2]

    result = random.choice([option1, option2])

    await safe_send(message.channel, f'**{result}** won the coinflip!')