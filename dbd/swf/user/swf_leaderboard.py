

from safe_send import safe_send


async def swf_leaderboard_handler(db, message):

    users = db['users']

    # find all users with swf_stats
    all_users = users.find({'swf_stats': {'$exists': True}})

    # rank users by most wins
    leaderboard = sorted(all_users, key=lambda u: u['swf_stats'].get('wins', 0), reverse=True)

    # output top 10 users
    output_message = '**SWF Leaderboard**\n'

    for rank, user in enumerate(leaderboard[:10], start=1):
        wins = user['swf_stats'].get('wins', 0)
        output_message += f"\n{rank}. {user['dbd_username']} - Wins: {wins}"

    await safe_send(message.channel, output_message)
