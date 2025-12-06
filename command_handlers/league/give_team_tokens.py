
from common_messages import invalid_number_of_params
import constants
from helpers import can_be_int, make_string_from_word_list
import math
from rewards import change_tokens

from safe_send import safe_send
from user.user import user_exists


async def give_team_tokens(message, db, team_name, tokens_to_give):

    lower_team_name = team_name.lower()

    league_teams = db['leagueteams']
    team_obj = league_teams.find_one({'name_lower': lower_team_name})
    if not team_obj:
        await safe_send(message.channel, 'Did not find team')
        return

    team_owner_id = team_obj['owner_id']
    owner_user = user_exists(db, team_owner_id)
    if not owner_user:
        await safe_send(message.channel, 'Critical error. Team owner not found. No tokens sent.')
        return
    
    await change_tokens(db, owner_user, tokens_to_give, 'sol-match-tokens')
    await safe_send(message.channel, 'Tokens sent to the team owner.')


async def give_team_tokens_handler(db, message):

    word_parts = message.content.split()
    if len(word_parts) < 3:
        await invalid_number_of_params(message)
        return
    
    tokens_to_give = word_parts[2]
    if not can_be_int(tokens_to_give):
        await safe_send(message.channel, tokens_to_give+' is not an integer')
        return
    tokens_to_give = int(tokens_to_give)
    
    team_name = word_parts[1]

    await give_team_tokens(message, db, team_name, tokens_to_give)
    

    



