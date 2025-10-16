from safe_send import safe_send
import random

async def raffle_winner_handler(db, message):
    giant_array = []

    users = db['users']
    all_users = users.find()

    for user in all_users:
        if 'tickets' in user:
            for i in range(user['tickets']):
                giant_array.append(user['battle_tag'])

    lucky_winner = random.choice(giant_array)

    await safe_send(message.channel, 'The winner of the raffle is the user with the battle tag: '+lucky_winner)