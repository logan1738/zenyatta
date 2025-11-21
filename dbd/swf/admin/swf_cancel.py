

import constants
from discord_actions import get_guild
from helpers import get_constant_value, set_constant_value
from safe_send import safe_send


async def swf_cancel_handler(client, db, message):

    swf_data = get_constant_value(db, 'swf')
    if not swf_data['active']:
        await safe_send(message.channel, 'SWF sign up is not currently active.')
        return
    
    swf_data['active'] = False

    swf_channel = client.get_channel(constants.SWF_CHANNEL)

    await swf_channel.send('Current SWF sign up has been cancelled by an admin.')
    
    set_constant_value(db, 'swf', swf_data)

    guild = await get_guild(client)
    swf_vc_access_role = guild.get_role(constants.SWF_VC_ACCESS_ROLE)

    for member in swf_vc_access_role.members:
        await member.remove_roles(swf_vc_access_role)

    await safe_send(message.channel, 'SWF sign up has been cancelled.')
    
    