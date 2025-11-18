

import constants
from discord_actions import get_message_by_channel_and_id
from helpers import get_constant_value
from safe_send import safe_send


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

    if len(signed_up_users) < NUM_SWF_PARTICIPANTS + 1:  # +1 to account for the bot itself
        await safe_send(message.channel, 'Not enough users have signed up for SWF to pick participants.')
        return
    
    await safe_send(message.channel, 'Picking SWF participants...')


    


