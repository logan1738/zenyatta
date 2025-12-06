
from context.context_helpers import get_league_invites_field, get_league_teams_collection_from_context
from discord_actions import get_guild
from helpers import get_constant_value, get_league_emoji_from_team_name
from safe_send import safe_add_field, safe_create_embed, safe_edit_embed, safe_set_footer
from user.user import get_league_invites_with_context, get_league_team_with_context, user_exists
import discord

async def validate_admin(db, message, context='OW'):

    user = user_exists(db, message.author.id)
    if not user:
        return None, None, None, None
    
    user_team = get_league_team_with_context(user, context)
    if user_team == "None":
        return None, None, None, None

    league_teams = get_league_teams_collection_from_context(db, context)
    my_team = league_teams.find_one({'team_name': user_team})
    if not my_team:
        return None, None, None, None

    is_admin = False
    team_members = my_team['members']
    for member in team_members:
        if member['discord_id'] == user['discord_id'] and member['is_admin']:
            is_admin = True
            break

    is_owner = False
    if my_team['owner_id'] == user['discord_id']:
        is_owner = True

    return is_admin, my_team, my_team['team_name'], is_owner


TEAM_NAME_TO_TEAM_COLOR = {
    'Polar': discord.Colour(0x00c9eb),
    'Olympians': discord.Colour(0xf9c429),
    'Eclipse': discord.Colour(0x005fe8),
    'Saviors': discord.Colour(0x771da7),
    'Ragu': discord.Colour(0xE02814),
    'Instigators': discord.Colour(0x0c0c0c),
    'Guardians': discord.Colour(0xff2af5),
    'Phoenix': discord.Colour(0xf15a29),
    'Fresas': discord.Colour(0xf92446),
    'Outliers': discord.Colour(0x361c89),
    'Celestials': discord.Colour(0x00aff0),
    'Saturn': discord.Colour(0xffb816),
    'Evergreen': discord.Colour(0x074735),
    'Misfits': discord.Colour(0xc3db35),
    'Hunters': discord.Colour(0x41564e),
    'Angels': discord.Colour(0xfff395),
    'Phantoms': discord.Colour(0xaabdcc),
    'Sentinels': discord.Colour(0x401b7a),
    'Diamonds': discord.Colour(0x78f0da),
    'Legion': discord.Colour(0xff0d1a),
    'Lotus': discord.Colour(0xfcb2c5),
    'Deadlock': discord.Colour(0xa60322),
    'Horizon': discord.Colour(0xfd8500),
    'Monarchs': discord.Colour(0x955d01),
    'Aces': discord.Colour(0xA2A2A2),
    'Mantas': discord.Colour(0x00476a),
    'Penguins': discord.Colour(0xf7961d),
    'Tsunami': discord.Colour(0x1b6fa2),
    'Frogs': discord.Colour(0x15e012),
    'Cottontails': discord.Colour(0xe1affa)
}

def get_team_color_by_name(team_name):

    if team_name in TEAM_NAME_TO_TEAM_COLOR:
        return TEAM_NAME_TO_TEAM_COLOR[team_name]
    
    return discord.Colour(0xFFFFFF)


TEAM_NAME_TO_TEAM_LOGO_URL = {
    'Polar': 'https://spicyesports.com/static/media/Polar.afd2ffc383f5eae45aca.png',
    'Olympians': 'https://spicyesports.com/static/media/Olympians.1226efdd6e2647ae266e.png',
    'Eclipse': 'https://spicyesports.com/static/media/Eclipse.e4cdd239089f8dcec7ee.png',
    'Saviors': 'https://spicyesports.com/static/media/Saviors.5eea71d3e31f461aa2c7.png',
    'Ragu': 'https://spicyesports.com/static/media/Ragu.aabdb0f398a3662f0379.png',
    'Instigators': 'https://spicyesports.com/static/media/Instigators.5d6fff76542f1db977a3.png',
    'Guardians': 'https://spicyesports.com/static/media/Guardians.a78a5aba9ac16ddffe36.png',
    'Phoenix': 'https://spicyesports.com/static/media/Phoenix.9c4abe3972bc250a4863.png',
    'Fresas': 'https://spicyesports.com/static/media/Fresas.a4cec89854afb9b9f31f.png',
    'Outliers': 'https://spicyesports.com/static/media/Outliers.517042f0ddc6d06ea95b.png',
    'Celestials': 'https://spicyesports.com/static/media/Celestials.162658494da7da5731c4.png',
    'Saturn': 'https://spicyesports.com/static/media/Saturn.4f4d3be9b96f03273cca.png',
    'Evergreen': 'https://spicyesports.com/static/media/Evergreen.cfd15d99f789d6a09f5a.png',
    'Misfits': 'https://spicyesports.com/static/media/Misfits.df89ff417be1b22ceb7a.png',
    'Hunters': 'https://spicyesports.com/static/media/Hunters.7806accc3f6d19a15006.png',
    'Angels': 'https://spicyesports.com/static/media/Angels.0209e3f19b850f83d275.png',
    'Phantoms': 'https://spicyesports.com/static/media/Phantoms.d9163e30e5a04aef0ecd.png',
    'Sentinels': 'https://spicyesports.com/static/media/Sentinels.131ba5d0ec9f6bb4f34d.png',
    'Diamonds': 'https://spicyesports.com/static/media/Diamonds.69459c71bbf761812351.png',
    'Legion': 'https://spicyesports.com/static/media/Legion.6b15cc8e73e5fa47ff39.png',
    'Lotus': 'https://spicyesports.com/static/media/Lotus.0ffc9685eba5019bfbed.png',
    'Deadlock': 'https://spicyesports.com/static/media/Deadlock.30821419d7ab5e8f1693.png',
    'Horizon': 'https://spicyesports.com/static/media/Horizon.f0b44e7955336bd40a16.png',
    'Monarchs': 'https://spicyesports.com/static/media/Monarchs.78705155f9a7e6f3cf45.png',
    'Aces': 'https://spicyesports.com/static/media/Aces.4d33616a35f35ff74ec6.png',
    'Mantas': 'https://spicyesports.com/static/media/Mantas.b4acf814b2c4ed6f7a54.png',
    'Penguins': 'https://spicyesports.com/static/media/Penguins.d63ee6c8b4325a935814.png',
    'Tsunami': 'https://spicyesports.com/static/media/Tsunami.9a5f28db18adb2394e04.png',
    'Frogs': '',
    'Cottontails': ''
}


def get_team_logo_url_by_name(team_name):

    if team_name in TEAM_NAME_TO_TEAM_LOGO_URL:
        return TEAM_NAME_TO_TEAM_LOGO_URL[team_name]
    
    return ''



def make_team_description(team):

    if len(team['allies']) == 0 and len(team['rivals']) == 0:
        return ''

    final_desc = ''

    has_allies = False

    if len(team['allies']) > 0:
        has_allies = True
        ally_string = 'Allies:'
        for ally in team['allies']:
            ally_emoji_string = get_league_emoji_from_team_name(ally)
            ally_string += ' '+ally_emoji_string+' '+ally

        final_desc += ally_string

    if len(team['rivals']) > 0:
        if has_allies:
            final_desc += '\n'

        rival_string = 'Rivals:'
        for rival in team['rivals']:
            rival_emoji_string = get_league_emoji_from_team_name(rival)
            rival_string += ' '+rival_emoji_string+' '+rival

        final_desc += rival_string
    
    return final_desc
        

CONTEXT_TO_DEFAULT_USER_ID = {
    'OW': '[Battle Tag Not Found]',
    'MR': '[Username Not Found]',
    'DB': '[Dead by Daylight Username Not Found]',
}

def make_member_game_id(db, member, context):
    
    member_id = CONTEXT_TO_DEFAULT_USER_ID[context]

    user = user_exists(db, member['discord_id'])

    if user:
        if context == 'OW':
            try:
                member_id = user['battle_tag'].split('#')[0]
            except Exception as e:
                raise Exception('Could not find a battle tag for user with id '+str(member['discord_id']))
        elif context == 'DB':
            try:
                member_id = user['dbd_username']
            except Exception as e:
                raise Exception('Could not find a dead by daylight username for user with id '+str(member['discord_id']))
        else:
            if 'rivals_username' in user:
                member_id = user['rivals_username']

    return member_id

def remove_league_invite(user, team_name, db, context='OW'):

    league_invites = get_league_invites_with_context(user, context)
    invites_field = get_league_invites_field(context)
    final_invites = []

    for invite in league_invites:
        if invite != team_name:
            final_invites.append(invite)

    users = db['users']
    users.update_one({"discord_id": user['discord_id']}, {"$set": {invites_field: final_invites}})


def user_admin_on_team(user_id, league_team):

    for member in league_team['members']:

        if member['discord_id'] == user_id:
            if member['is_admin']:
                return True
            else:
                return False

    return False


def get_team_record_string(db, team_name):

    league_season = get_constant_value(db, 'league_season')

    standings = db['standings']
    standings_obj = standings.find_one({'season': league_season})

    team_record = standings_obj['teams'][team_name]

    team_wins = team_record['wins']
    team_losses = team_record['losses']

    return 'W: '+str(team_wins)+' L: '+str(team_losses)


def has_username_for_game(user, context):

    if context == 'OW':
        if 'battle_tag' in user:
            return True
    elif context == 'MR':
        if 'rivals_username' in user:
            return True
    elif context == 'DB':
        if 'dbd_username' in user:
            return True

    return False