

from common_messages import invalid_number_of_params
from helpers import can_be_int, get_constant_value, valid_number_of_params
from safe_send import safe_send


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
    
    await safe_send(message.channel, f'Replacing participant #{replace_index + 1}...')