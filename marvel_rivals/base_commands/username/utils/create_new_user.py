from api import get_member, give_role
import constants
import copy

from safe_send import safe_send

async def create_new_user(client, db, user_id, message, rivals_username):
    
    users = db['users']

    username_lower = rivals_username.lower()

    new_user = copy.deepcopy(constants.DEFAULT_BLANK_USER)
    new_user["rivals_username"] = rivals_username
    new_user["rivals_username_lower"] = username_lower
    new_user["discord_id"] = user_id

    users.insert_one(new_user)

    guild = client.get_guild(constants.GUILD_ID)
    reg_role = guild.get_role(constants.REGISTERED_ROLE)

    member = get_member(guild, user_id, 'MR Username Link')
    if member and reg_role:
        await give_role(member, reg_role, 'MR Username Link')

    await safe_send(message.channel, "You've successfully added your Marvel Rivals username to your discord account.")