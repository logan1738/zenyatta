

from common_messages import invalid_number_of_params
from dbd.swf.admin.swf_pick import output_users_picked
from helpers import can_be_int, get_constant_value, set_constant_value, valid_number_of_params
from safe_send import safe_send
import random

async def swf_replace_handler(client, db, message):

    valid_params, params = valid_number_of_params(message, 2)
    if not valid_params:
        await invalid_number_of_params(message)
        return
    
    replace_param = params[1]
    
    if not can_be_int(replace_param):
        await safe_send(message.channel, 'The replace command requires the first parameter to be the participant number to replace (1, 2, or 3).')
        return
    
    replace_index = int(replace_param) - 1
    if replace_index < 0 or replace_index > 2:
        await safe_send(message.channel, 'The replace command requires the first parameter to be the participant number to replace (1, 2, or 3).')
        return
    
    swf_data = get_constant_value(db, 'swf')

    valid_sign_up_ids = swf_data['valid_sign_up_ids']
    if len(valid_sign_up_ids) == 0:
        await safe_send(message.channel, 'There are no valid sign ups remaining to replace the participant with. This round must be cancelled.')
        return
    
    # Just pick a complete random user when replacing for simplicity
    new_participant_id = random.choice(valid_sign_up_ids)

    picked_participants = swf_data['picked_participants']
    picked_participants[replace_index] = new_participant_id

    new_valid_sign_ups = []
    for user_id in valid_sign_up_ids:
        if user_id != new_participant_id:
            new_valid_sign_ups.append(user_id)

    swf_data['picked_participants'] = picked_participants
    swf_data['valid_sign_up_ids'] = new_valid_sign_ups

    set_constant_value(db, 'swf', swf_data)

    await output_users_picked(db, client, picked_participants, True)