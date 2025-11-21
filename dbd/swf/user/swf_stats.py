

from common_messages import not_registered_response
from safe_send import safe_send
from user.user import user_exists


async def swf_stats_handler(db, message):

    user = user_exists(db, message.author.id)
    if not user:
        await not_registered_response(message, 'DB')
        return
    
    swf_stats = user.get('swf_stats', {'wins': 0, 'losses': 0})
    wins = swf_stats['wins']
    losses = swf_stats['losses']

    output_message = '**SWF Stats for ' + message.author.name + '**\n'
    output_message += f"Wins: {wins}\n"
    output_message += f"Losses: {losses}\n"
    output_message += f"Win Percentage: { (wins / (wins + losses) * 100) if (wins + losses) > 0 else 0:.2f}%"

    await safe_send(message.channel, output_message)