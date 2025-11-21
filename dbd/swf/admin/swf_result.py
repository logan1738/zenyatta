


from helpers import get_constant_value
from safe_send import safe_send
from user.user import get_user_tokens, user_exists
import constants

DEFAULT_SWF_STATS = {
    'wins': 0,
    'losses': 0,
}


SWF_WIN_MESSAGE = 'The SWF team won! Each participant has been awarded 500 tokens.'
SWF_LOSS_MESSAGE = 'The SWF team lost. Each participant has been awarded 100 tokens.'

async def swf_result_handler(client, db, message, is_win):

    swf_data = get_constant_value(db, 'swf')

    if not swf_data['active']:
        await safe_send(message.channel, 'SWF is not currently active.')
        return
    
    if not swf_data['picked']:
        await safe_send(message.channel, 'SWF participants have not been picked yet.')
        return

    picked_participants = swf_data['picked_participants']

    tokens_to_award_each_user = 500 if is_win else 100
    swf_result_message = SWF_WIN_MESSAGE if is_win else SWF_LOSS_MESSAGE

    users = db['users']
    for user_id in picked_participants:
        db_user = user_exists(db, user_id)
        if db_user:
            new_tokens = get_user_tokens(db_user) + tokens_to_award_each_user
            swf_stats = db_user.get('swf_stats', DEFAULT_SWF_STATS.copy())

            if is_win:
                swf_stats['wins'] += 1
            else:
                swf_stats['losses'] += 1

            users.update_one( {'discord_id': user_id}, { '$set': {'tokens': new_tokens,'swf_stats': swf_stats} } )

    swf_channel = client.get_channel(constants.SWF_CHANNEL)
    await safe_send(swf_channel, swf_result_message)

    await safe_send(message.channel, 'Sucessfully ended the SWF event: ' + swf_result_message)





