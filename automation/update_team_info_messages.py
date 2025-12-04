

from command_handlers.league.generate_team_info import create_team_embed
from context.context_helpers import get_league_teams_collection_from_context, get_team_info_channel_id_from_context
from discord_actions import get_message_by_channel_and_id
from helpers import get_constant_value, set_constant_value
from safe_send import safe_send


async def update_team_info_messages(client, db, message, context):

    teams_to_update_document = get_constant_value(db, 'teams_to_update')
    team_info_document = get_constant_value(db, 'team_info')

    if not context in teams_to_update_document:
        await safe_send(message.channel, 'No teams to found for context: ' + context)
        return
    
    teams_to_update = teams_to_update_document[context]

    if len(teams_to_update) == 0:
        await safe_send(message.channel, 'No teams to update for context: ' + context)
        return
    
    if not context in team_info_document:
        await safe_send(message.channel, 'No team info found for context: ' + context)
        return
    
    team_info_context = team_info_document[context]

    teams_to_update_count = len(teams_to_update)
    teams_updated = 0
    for team_name in teams_to_update:
        team_info_message_id = team_info_context[team_name]['message_id']

        league_teams_collection = get_league_teams_collection_from_context(db, context)
        league_team = league_teams_collection.find_one({'team_name': team_name})
        if not league_team:
            continue

        existing_message = await get_message_by_channel_and_id(client, get_team_info_channel_id_from_context(context), team_info_message_id)
        new_content = create_team_embed(db, team_name, league_team, context)

        await existing_message.edit(embed=new_content)

    teams_to_update_document[context] = []
    set_constant_value(db, 'teams_to_update', teams_to_update_document)

    await safe_send(message.channel, f'Updated {teams_updated}/{teams_to_update_count} team info messages for context: {context}')


