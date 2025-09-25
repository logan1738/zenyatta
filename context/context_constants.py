import constants

CONTEXT_TO_LEAGUE_TEAM_COLLECTION = {
    'OW': 'leagueteams',
    'MR': 'rivals_leagueteams',
    'VL': 'valorant_leagueteams',
    'DB': 'dbd_leagueteams',
}

CONTEXT_TO_LEAGUE_TEAM_FIELD = {
    'OW': 'league_team',
    'MR': 'rivals_league_team',
    'VL': 'valorant_league_team',
    'DB': 'dbd_league_team',
}

CONTEXT_TO_LEAGUE_INVITES_FIELD = {
    'OW': 'league_invites',
    'MR': 'rivals_league_invites',
    'VL': 'valorant_league_invites',
    'DB': 'dbd_league_invites',
}

CONTEXT_TO_FAN_OF_FIELD = {
    'OW': 'fan_of',
    'MR': 'fan_of_rivals',
    'VL': 'fan_of_valorant',
    'DB': 'fan_of_dbd',
}

CONTEXT_TO_RIVAL_OF_FIELD = {
    'OW': 'rival_of',
    'MR': 'rival_of_rivals',
    'VL': 'rival_of_valorant',
    'DB': 'rival_of_dbd',
}

CONTEXT_TO_LEAGUE_SEASON_CONSTANT_NAME = {
    'OW': 'league_season',
    'MR': 'league_season_rivals',
    'VL': 'league_season_valorant',
    'DB': 'league_season_dbd',
}

CONTEXT_TO_LEAGUE_TEAM_IMAGE_UPDATE_INDEX = {
    'OW': 'team_image_update_index',
    'MR': 'rivals_team_image_update_index',
    'VL': 'valorant_team_image_update_index',
    'DB': 'dbd_team_image_update_index',
}

CONTEXT_TO_LEAGUE_NOTIFS_CHANNEL = {
    'OW': constants.TEAM_NOTIFS_CHANNEL,
    'MR': constants.RIVALS_TEAM_NOTIFS_CHANNEL,
    'VL': constants.VALORANT_TEAM_NOTIFS_CHANNEL,
    'DB': constants.DBD_TEAM_NOTIFS_CHANNEL,
}

CONTEXT_TO_TEAM_OWNERS_CHANNEL = {
    'OW': constants.TEAM_OWNERS_CHANNEL,
    'MR': constants.RIVALS_TEAM_OWNERS_CHANNEL,
    'VL': constants.VALORANT_TEAM_OWNERS_CHANNEL,
    'DB': constants.DBD_TEAM_OWNERS_CHANNEL,
}

CONTEXT_TO_LEAGUE_ANNOUNCEMENTS_CHANNEL = {
    'OW': constants.LEAGUE_ANNOUNCEMENTS_CHANNEL,
    'MR': constants.RIVALS_LEAGUE_ANNOUNCEMENTS_CHANNEL,
    'VL': constants.VALORANT_LEAGUE_ANNOUNCEMENTS_CHANNEL,
    'DB': constants.DBD_LEAGUE_ANNOUNCEMENTS_CHANNEL,
}

CONTEXT_TO_LEAGUE_URL = {
    'OW': 'sol',
    'MR': 'srl',
    'VL': 'svl',
}

CONTEXT_TO_TEAM_LIST = {
    'OW': constants.TEAM_LIST,
    'MR': constants.RIVALS_TEAM_LIST,
    'VL': constants.VALORANT_TEAM_LIST,
}

CONTEXT_TO_TEAM_ADMIN_ROLE_ID = {
    'OW': 1353479674008961104,
    'MR': 1353487134895378582,
    'VL': 1361872050804887664,
}

CONTEXT_TO_LINEUP_ROLE_LIST = {
    'OW': ['tank', 'dps1', 'dps2', 'sup1', 'sup2'],
    'MR': ['player1', 'player2', 'player3', 'player4', 'player5', 'player6'],
    'VL': ['player1', 'player2', 'player3', 'player4', 'player5']
}

CONTEXT_TO_USER_ID = {
    'OW': 'battle_tag',
    'MR': 'rivals_username',
    'VL': 'riot_id',
}

CONTEXT_TO_CALL = {
    'OW': 'call',
    'MR': 'rivals_call',
    'VL': 'valorant_call',
}

CONTEXT_TO_TEAMS_JOINED_THIS_SEASON = {
    'OW': 'teams_joined_this_season',
    'MR': 'rivals_teams_joined_this_season',
    'VL': 'valorant_teams_joined_this_season',
}