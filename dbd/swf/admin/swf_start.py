

from helpers import get_constant_value, set_constant_value
from safe_send import safe_send


async def swf_start_handler(db, message):

    
    swf_data = get_constant_value(db, 'swf')
    if swf_data['active']:
        await safe_send(message.channel, 'SWF sign up is already active.')
        return
    
    swf_data['active'] = True
    set_constant_value(db, 'swf', swf_data)

    await safe_send(message.channel, 'SWF sign up has been started.')
    

