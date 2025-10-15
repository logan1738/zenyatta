

import copy
from api import get_member, give_role
import constants
from helpers import make_string_from_word_list
from safe_send import safe_send
from user.user import user_exists

def create_new_user_from_dbd_username(db, dbd_username, user_id):

    users = db['users']

    dbd_username_lower = dbd_username.lower()

    new_user = copy.deepcopy(constants.DEFAULT_BLANK_USER)
    new_user["dbd_username"] = dbd_username
    new_user["dbd_username_lower"] = dbd_username_lower
    new_user["discord_id"] = user_id

    users.insert_one(new_user)


def handle_dbd_username_link_success(db, message, dbd_username):

    users = db['users']
    existing_user = user_exists(db, message.author.id)

    if existing_user:

        users.update_one({'discord_id': message.author.id}, {'$set': {'dbd_username': dbd_username, 'dbd_username_lower': dbd_username.lower()}})

    else:
        create_new_user_from_dbd_username(db, dbd_username, message.author.id)




async def dbd_username_link(db, message, client, user, dbd_username):

    if len(dbd_username) > 30:
        await safe_send(message.channel, 'The DBD username you provided is not valid.')
        return

    if not ('#' in dbd_username):
        await safe_send(message.channel, "The DBD username you provided seems to be missing the # and part at the end. Please include that too.")
        return

    if dbd_username[0] == '#':
        await safe_send(message.channel, 'DBD usernames cannot start with the "#" character. Please use this format: Username#1234')
        return

    lower_id = dbd_username.lower()
    users = db['users']

    user_with_dbd_username = users.find_one({'dbd_username_lower': lower_id})

    if user_with_dbd_username:
        if user_with_dbd_username['discord_id'] == message.author.id:
            await safe_send(message.channel, "You've already linked this DBD username.")
        else:
            await safe_send(message.channel, "That DBD username has already been connected to a different discord account. Please contact staff if you need help.")
        return

    handle_dbd_username_link_success(db, message, dbd_username)

    guild = client.get_guild(constants.GUILD_ID)
    reg_role = guild.get_role(constants.REGISTERED_ROLE)
    member = get_member(guild, user.id, 'DBD Username Link')
    if member and reg_role:
        await give_role(member, reg_role, 'DBD Username Link')

    await safe_send(message.channel, "Success! Your DBD username has been linked to the Spicy Esports server! (Please note: if you change your DBD username please use the !dbd command again to update it!)")


async def dbd_username_handler(db, message, client):
    
    word_parts = message.content.split()
    dbd_username = make_string_from_word_list(word_parts, 1)

    await dbd_username_link(db, message, client, message.author, dbd_username)