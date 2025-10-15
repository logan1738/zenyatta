

from common_messages import invalid_number_of_params
from context.context_helpers import get_league_teams_collection_from_context, get_league_url_from_context
from helpers import valid_number_of_params
import constants
from safe_send import safe_send

async def team_page_handler(db, message, context): 

    valid_params, params = valid_number_of_params(message, 2)
    if not valid_params:
        await safe_send(message.channel, 'Please specify the name of the team to get the team page for. (Example: !teampage Polar)')
        return
    
    team_name = params[1]
    lower_team_name = team_name.lower()

    league_teams = get_league_teams_collection_from_context(db, context)
    team = league_teams.find_one({'name_lower': lower_team_name})
    if not team:
        await safe_send(message.channel, 'Could not find any league team with the name "'+str(team_name)+'"')
        return
    
    league_url = get_league_url_from_context(context)

    final_string = 'Click the link below to see the team page for '+team['team_name']
    final_string += '\n\n'+f'{constants.WEBSITE_DOMAIN}/{league_url}/team/'+lower_team_name

    await safe_send(message.channel, final_string)