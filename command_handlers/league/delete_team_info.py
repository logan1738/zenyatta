

from context.context_helpers import get_team_info_channel_from_context
from discord_actions import get_message_by_channel_and_id
from helpers import get_constant_value, set_constant_value
from safe_send import safe_send
import time

async def delete_team_info_handler(client, db, message, context):

    team_info = get_constant_value(db, 'team_info')

    if not context in team_info:
        await safe_send(message.channel, 'Invalid context: '+context)
        return
    
    team_info_context = team_info[context]

    team_info_channel = get_team_info_channel_from_context(client, context)
    team_info_channel_id = team_info_channel.id

    for team_name in team_info_context:

        team_message_id = team_info_context[team_name]['message_id']
        if team_message_id != 0:
            team_message = await get_message_by_channel_and_id(client, team_info_channel_id, team_message_id)
            if team_message:
                await team_message.delete()
            team_info_context[team_name]['message_id'] = 0
            time.sleep(1)

    team_info[context] = team_info_context

    set_constant_value(db, 'team_info', team_info)

    await safe_send(message.channel, f'Team info messages deleted for context {context}.')
