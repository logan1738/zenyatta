

import constants
from discord_actions import get_message_by_channel_and_id
from helpers import get_constant_value, set_constant_value
from safe_send import safe_send
from user.user import user_exists
import random

NUM_SWF_PARTICIPANTS = 3




def build_swf_player_array(dbd_users):

    users_with_probabilities = []

    for user in dbd_users:

        number_rejections = user.get('swf_rejections', 0)
        is_sub = user.get('twitch_subscriber', False)

        base_probability = 1
        probability_with_rejections = base_probability + number_rejections
        if is_sub:
            probability_with_rejections *= 2

        entry = {
            'user': user,
            'selection_probability': probability_with_rejections
        }

        users_with_probabilities.append(entry)


    probability_array = []

    for entry in users_with_probabilities:
        user_id = entry['user']['discord_id']
        for _ in range(entry['selection_probability']):
            probability_array.append(user_id)


    return probability_array


def pick_player_and_remove_from_array(swf_array):

    random_user_id = random.choice(swf_array)
    swf_array = [user_id for user_id in swf_array if user_id != random_user_id]

    return random_user_id, swf_array

    

async def swf_pick_players(db, dbd_users, swf_data):

    swf_data['picked'] = True
    swf_data['valid_sign_up_ids'] = [user['discord_id'] for user in dbd_users]

    swf_array = build_swf_player_array(dbd_users)

    picked_participants = []
    for _ in range(NUM_SWF_PARTICIPANTS):
        picked_user_id, swf_array = pick_player_and_remove_from_array(swf_array)
        picked_participants.append(picked_user_id)

    swf_data['picked_participants'] = picked_participants

    await set_constant_value(db, 'swf', swf_data)


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

    # BYPASS THIS FOR NOW, MAKE SURE TO RE-ENABLE LATER
    if len(valid_users) < NUM_SWF_PARTICIPANTS and False:
        num_valid = len(valid_users)
        await safe_send(message.channel, f'There were not enough users in the database that signed up. Only {num_valid} database user(s) have signed up.')
        await safe_send(message.channel, str(valid_users[0]['discord_id']))
        return
    
    dbd_users = []
    for user in valid_users:
        if 'dbd_username' in user and user['dbd_username']:
            dbd_users.append(user)

    # ADD EXTRA USERS RIGHT NOW FOR TESTING, REMOVE LATER
    extra_user_1 = user_exists(db, 592828437131952130) # Jacob
    extra_user_2 = user_exists(db, 706266168872140847) # Smelly Snail
    dbd_users.append(extra_user_1)
    dbd_users.append(extra_user_2)

    if len(dbd_users) < NUM_SWF_PARTICIPANTS:
        num_dbd = len(dbd_users)
        await safe_send(message.channel, f'There were not enough users with DBD usernames in the database that signed up. Only {num_dbd} user(s) with DBD usernames have signed up.')
        return
    
    await swf_pick_players(db, dbd_users, swf_data)

    await safe_send(message.channel, 'SWF participants have been picked successfully.')

    


