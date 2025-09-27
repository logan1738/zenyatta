import constants
from safe_send import safe_dm
from user.user import user_exists

async def member_joined(member, db, client):

    guild = client.get_guild(constants.GUILD_ID)
    role = guild.get_role(constants.MEMBER_ROLE_ID)
    server_notifs = guild.get_role(constants.SERVER_NOTIFS_ROLE)
    tourney_notifs = guild.get_role(constants.TOURNEY_NOTIFS_ROLE)
    twitch_notifs = guild.get_role(constants.TWITCH_NOTIFS_ROLE)
    league_notifs = guild.get_role(constants.LEAGUE_NOTIFS_ROLE)

    if role is not None:

        registered_user = user_exists(db, member.id)
        if registered_user:
            registered_role = guild.get_role(constants.REGISTERED_ROLE)
            image_perm_role = guild.get_role(constants.IMAGE_PERMS_ROLE)
            await member.add_roles(role, server_notifs, tourney_notifs, twitch_notifs, league_notifs, registered_role, image_perm_role)
        else:
            await member.add_roles(role, server_notifs, tourney_notifs, twitch_notifs, league_notifs)