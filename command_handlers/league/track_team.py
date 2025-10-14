

from context.context_helpers import get_league_teams_collection_from_context, get_team_info_channel_from_context
from helpers import get_constant_value, set_constant_value, valid_number_of_params
from safe_send import safe_send


async def track_team_handler(db, message, client, context):

    team_info = get_constant_value(db, 'team_info')

    if not context in team_info:
        await safe_send(message.channel, 'Invalid context: '+context)
        return
    
    team_info_context = team_info[context]

    valid_params, params = valid_number_of_params(message, 2)
    if not valid_params:
        await safe_send(message.channel, 'Invalid number of parameters. Usage: !trackteam <team_name>')
        return
    
    team_name = params[1]

    league_teams = get_league_teams_collection_from_context(db, context)
    team_name_lower = team_name.lower()
    team_object = league_teams.find_one({'name_lower': team_name_lower})

    if not team_object:
        await safe_send(message.channel, 'Team not found: '+team_name)
        return
    
    team_name_normalized = team_object['team_name']

    if team_name_normalized in team_info_context:
        await safe_send(message.channel, f'Team {team_name_normalized} is already being tracked in context {context}.')
        return
    
    # get team info channel
    team_info_channel = get_team_info_channel_from_context(client, context)

    # generate new message
    team_info_message = await safe_send(team_info_channel, team_name_normalized)

    # record message id to dict
    team_info_context[team_name_normalized] = {
        'message_id': team_info_message.id,
    }

    team_info[context] = team_info_context

    # update constant in db
    set_constant_value(db, 'team_info', team_info)
