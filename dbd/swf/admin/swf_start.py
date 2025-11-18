

import constants
from helpers import get_constant_value, set_constant_value
from safe_send import safe_send



async def start_swf(client, db, swf_data):


    swf_channel = client.get_channel(constants.FEATURE_CHANNEL)

    await swf_channel.send('Next SWF event is ready for sign ups! Click the reaction below for a chance to be selected!')


    swf_data['active'] = True
    set_constant_value(db, 'swf', swf_data)



async def swf_start_handler(client, db, message):

    
    swf_data = get_constant_value(db, 'swf')
    if swf_data['active']:
        await safe_send(message.channel, 'SWF sign up is already active.')
        return
    
    await start_swf(client, db, swf_data)

    await safe_send(message.channel, 'SWF sign up has been started.')
    

