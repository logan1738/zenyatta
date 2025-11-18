
import constants
from discord_actions import get_guild
from safe_send import safe_send
from user.user import user_exists


async def verify_twitch_subs(db, channel, client):

    guild = await get_guild(client)

    twitch_sub_role = guild.get_role(constants.TWITCH_SUB_ROLE)

    twitch_sub_members = [member for member in twitch_sub_role.members]

    await safe_send(channel, f'There are currently {len(twitch_sub_members)} members with the Twitch Sub role in the server.')

    twitch_sub_id_array = [member.id for member in twitch_sub_members]

    added_subs = 0
    removed_subs = 0

    # Remove any subs that are no longer subscribed
    users = db['users']
    all_subscribed_users = list(users.find({'twitch_subscriber': True}))
    for subscribed_user in all_subscribed_users:
        user_id = subscribed_user['discord_id']
        if user_id not in twitch_sub_id_array:
            users.update_one({'discord_id': user_id}, {'$set': {'twitch_subscriber': False}})
            removed_subs += 1

    # Add any subs that are newly subscribed
    for twitch_sub_id in twitch_sub_id_array:
        user_document = user_exists(db, twitch_sub_id)
        if user_document:
            if not user_document.get('twitch_subscriber', False):
                users.update_one({'discord_id': twitch_sub_id}, {'$set': {'twitch_subscriber': True}})
                added_subs += 1

    await safe_send(channel, f'Verification complete! Added {added_subs} new Twitch Subs, removed {removed_subs} old Twitch Subs.')