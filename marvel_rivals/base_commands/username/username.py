

from helpers import make_string_from_word_list
from marvel_rivals.base_commands.username.utils.create_new_user import create_new_user
from marvel_rivals.base_commands.username.utils.update_user_username import update_user_username
from safe_send import safe_send
from user.user import user_exists

def user_with_username_exists(db, username):

    username_lower = username.lower()

    users = db['users']
    username_user = users.find_one({'rivals_username_lower': username_lower})

    return username_user


async def username_handler(client, db, message):

    word_parts = message.content.split()
    rivals_username = make_string_from_word_list(word_parts, 1)

    if len(rivals_username) > 30 or len(rivals_username) < 1:
        await safe_send(message.channel, 'The marvel rivals username you provided is not valid.')
        return
    
    user_with_username = user_with_username_exists(db, rivals_username)
    if user_with_username:
        if user_with_username['discord_id'] == message.author.id:
            await safe_send(message.channel, 'You have already linked this marvel rivals username to your profile.')
        else:
            await safe_send(message.channel, 'That marvel rivals username is already linked to a another discord user. Please contact staff if you need help.')
        return

    user_id = message.author.id
    user = user_exists(db, user_id)
    if user_exists(db, user_id):
        await update_user_username(db, user, message, rivals_username) 
    else:
        await create_new_user(client, db, user_id, message, rivals_username)
