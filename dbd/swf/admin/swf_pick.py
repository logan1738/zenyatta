

import constants
from discord_actions import get_message_by_channel_and_id
from helpers import get_constant_value
from safe_send import safe_send
from user.user import user_exists


NUM_SWF_PARTICIPANTS = 3

async def swf_pick_players():

    pass



async def swf_pick_handler(client, db, message):

    swf_data = get_constant_value(db, 'swf')

    if not swf_data['active']:
        await safe_send(message.channel, 'SWF sign up is not currently active.')
        return
    
    if swf_data['picked']:
        await safe_send(message.channel, 'SWF participants have already been picked.')
        return
    
    sign_up_message = await get_message_by_channel_and_id(client, constants.SWF_CHANNEL, swf_data['sign_up_msg_id'])
    if not sign_up_message:
        await safe_send(message.channel, 'Could not find SWF sign up message.')
        return
    
    message_reactions = sign_up_message.reactions
    # There will always only be one reaction (the ✅)
    sign_up_reaction = message_reactions[0]

    signed_up_users = [user async for user in sign_up_reaction.users()]


    # BYPASS THIS FOR NOW, MAKE SURE TO RE-ENABLE LATER
    if (len(signed_up_users) < NUM_SWF_PARTICIPANTS + 1) and False:  # +1 to account for the bot itself
        num_signed_up = len(signed_up_users) - 1
        await safe_send(message.channel, f'Not enough users have signed up for SWF to pick participants. Only {num_signed_up} user(s) have signed up.')
        return
    
    valid_users = []
    for user in signed_up_users:
        if user.id == constants.BOT_ID:
            continue
        
        db_user = user_exists(db, user.id)
        if db_user:
            valid_users.append(db_user)

    if len(valid_users) < NUM_SWF_PARTICIPANTS:
        num_valid = len(valid_users)
        await safe_send(message.channel, f'There were not enough users in the database that signed up. Only {num_valid} database user(s) have signed up.')
        return
    
    dbd_users = []
    for user in valid_users:
        if 'dbd_username' in user and user['dbd_username']:
            dbd_users.append(user)

    if len(dbd_users) < NUM_SWF_PARTICIPANTS:
        num_dbd = len(dbd_users)
        await safe_send(message.channel, f'There were not enough users with DBD usernames in the database that signed up. Only {num_dbd} user(s) with DBD usernames have signed up.')
        return
    
    await safe_send(message.channel, 'Picking SWF participants...')


    


