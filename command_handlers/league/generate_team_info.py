

from context.context_helpers import get_team_info_channel_from_context
from helpers import get_constant_value, set_constant_value
from league import get_team_color_by_name
from safe_send import safe_create_embed, safe_send, safe_send_embed


def context_messages_exist(team_info_context):

    for team_name in team_info_context:
        if team_info_context[team_name]['message_id'] != 0:
            return True

    return False
    

def create_team_embed(team_name):

    team_embed = safe_create_embed(team_name, color=get_team_color_by_name(team_name))
    team_embed.set_image(url='https://spicyesports.com/static/media/Eclipse.e4cdd239089f8dcec7ee.png')
    return team_embed


async def generate_team_info_handler(client, db, message, context):

    team_info = get_constant_value(db, 'team_info')

    if not context in team_info:
        await safe_send(message.channel, 'Invalid context: '+context)
        return
    
    team_info_context = team_info[context]

    if context_messages_exist(team_info_context):
        await safe_send(message.channel, f'Team info messages already exist for context {context}. Cannot generate new ones.')
        return
    
    team_info_channel = get_team_info_channel_from_context(client, context)

    team_names_sorted_alphabetically = sorted(team_info_context.keys())

    for team_name in team_names_sorted_alphabetically:
        team_embed = create_team_embed(team_name)
        team_info_message = await safe_send_embed(team_info_channel, team_embed)
        team_info_context[team_name]['message_id'] = team_info_message.id

    team_info[context] = team_info_context

    set_constant_value(db, 'team_info', team_info)

    await safe_send(message.channel, f'Team info messages generated for context {context}.')
    
