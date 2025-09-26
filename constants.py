import copy
import os
from dotenv import load_dotenv

load_dotenv()

VERSION = '1.11.50'

OPEN_AI_TOKEN = os.getenv("OPEN_AI_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
STREAMLABS_TOKEN = os.getenv("STREAMLABS_TOKEN")

WEBSITE_DOMAIN = 'https://spicyesports.com'

ALL_CONTEXTS = ['OW', 'MR', 'VL', 'DB']

BOT_ID = 1130225436006305946

EVENT_ROLE = 1153799657416310957
GUILD_ID = 1130553449491210442
REGISTERED_ROLE = 1140095032104321165
SPICY_RAGU_ID = 1112204092723441724
STAFF_PING = f'<@{SPICY_RAGU_ID}>'
ZEN_ID = 1130225436006305946
PUSH_BOT_ID = 1183858823614713929
MEMBER_ROLE_ID = 1131309952200347741
SERVER_NOTIFS_ROLE = 1143577309895471134
TOURNEY_NOTIFS_ROLE = 1143577442531950612
TWITCH_NOTIFS_ROLE = 1143577582575554712
LEAGUE_NOTIFS_ROLE = 1255683967353491476

TIME_BETWEEN_GIFTS = 28800
TIME_BETWEEN_SHOP = 604800
TIME_IN_30_DAYS = 2592000
MAX_PLAYER_TEAMS = 20
SQUISHY_ID = 1150575886668669018
GIFT_ROLE_ID = 1146461901929336892
TOKEN_NOTIF_ROLE_ID = 1246634634259857459
SUB_VOTE_ROLE_ID = 1273403775024894062
QUEST_NOTIF_ROLE_ID = 1276604700690485309
SOL_TODAY_NOTIF_ROLE_ID = 1315919727222198362
HELPER_ROLE_ID = 1146460493289115819
TIER_3_MOD_ROLE_ID = 1410756981928755240
XP_HELPER_ROLE_ID = 1355991291594277129
CHANNEL_POINTS_ROLE_ID = 1208922341749293057
TWITCH_PACKS_ROLE_ID = 1213188461746454608
IMAGE_PERMS_ROLE = 1131364943371976834
TOURNEY_COMMANDS_PERMS_ROLE = 1298709598626123908
STATE_CAPTAIN_ROLE = 1302360749108232262

OVERWATCH_ROLE = 1318717229793280050
MARVEL_RIVALS_ROLE = 1316612393073381447
VALORANT_ROLE = 1361828873796452535
DBD_ROLE = 1419033077061255188

SUPPORTER_ROLE_ID = 1336111411398443040

SERVER_NOTIF_MSG = 1143629385195323422
TOURNEY_NOTIF_MSG = 1143629387665780806
TWITCH_NOTIF_MSG = 1143629390387888328
LEAGUE_NOTIF_MSG = 1255950510238990426
GIFT_NOTIF_MSG = 1186377894411370578
TOKEN_SHOP_NOTIF_MSG = 1246635093263384607
SUB_VOTE_NOTIF_MSG = 1273403959842963517
QUEST_NOTIF_MSG = 1276604655430008832
SOL_TODAY_NOTIF_MSG = 1315920400672362587

OVERWATCH_MSG = 1316613550130856057
MARVEL_RIVALS_MSG = 1316613551825223700
VALORANT_MSG = 1361831611368476855
DBD_MSG = 1419193303563239531

SERVER_LEVEL_MESSAGE = 1234933381603659817
NEXT_LEVELS_MESSAGE = 1234933542899810477


TWITCH_SUB_ROLE = 1161078724414943362
SERVER_BOOSTER_ROLE = 1138358504072171541

# CHANNELS
EVENT_CHANNEL_ID = 1157408569247936563
ROULETTE_CHANNEL = 1141867997280092191
BLACKJACK_CHANNEL = 1153715477772775464
MINE_CHANNEL = 1157026865177960548
RPS_CHANNEL = 1179286199836364820

BOT_CHANNEL = 1130553489106411591
RIVALS_BOT_CHANNEL = 1318388766691295272
VALORANT_BOT_CHANNEL = 1361878612638433510

BOT_CHAT_CHANNEL = 1184226404531982406
OFFER_REDEMPTIONS_CHANNEL_ID = 1414351138790178916
SHOP_CHANNEL_ID = 1187062494561325056
SUGGEST_CHANNEL = 1133850857037901956
FEATURE_CHANNEL = 1323028774568071288
ERROR_LOGS_CHANNEL = 1174139356156538880
CHAT_CHANNEL = 1130553450279747606
ADMIN_COMMAND_CHANNEL = 1131625086722523297
MARVEL_ADMIN_COMMAND_CHANNEL = 1318403138755100764
SERVER_SUGGEST_CHANNEL = 1154822833768235200

TEAM_NOTIFS_CHANNEL = 1171264069198684281
RIVALS_TEAM_NOTIFS_CHANNEL = 1318434949128519710
VALORANT_TEAM_NOTIFS_CHANNEL = 1361871682691928144
DBD_TEAM_NOTIFS_CHANNEL = 1420875557029019682

GEM_TRADING_CHANNEL = 1175847268243492965
DAILY_AUCTION_CHANNEL = 1181662345408290957
CARD_TRADING_CHANNEL = 1211776041983549531
CLIPS_CHANNEL = 1162439760409804800
UPDATE_CHANNEL = 1161355042830430269
MODS_CHANNEL = 1412180969569648721
PACK_OPEN_CHANNEL = 1233596350306713600
SERVER_LEVEL_CHANNEL = 1234932215482155048
XP_BATTLE_CHANNEL = 1243727256182984794
ANNOUNCEMENTS_CHANNEL_ID = 1133457825461440632

LEAGUE_ANNOUNCEMENTS_CHANNEL = 1343724891781730304
RIVALS_LEAGUE_ANNOUNCEMENTS_CHANNEL = 1343725102688374794
VALORANT_LEAGUE_ANNOUNCEMENTS_CHANNEL = 1361872494914699274
DBD_LEAGUE_ANNOUNCEMENTS_CHANNEL = 1419195529656664086

BET_CHANNEL_ID = 1248421720721719346
SUB_VOTE_CHANNEL = 1272712092436402247
STATE_CUP_CHANNEL = 1300343410699403294

TEAM_OWNERS_CHANNEL = 1171875033816236032
RIVALS_TEAM_OWNERS_CHANNEL = 1318380926031368264
VALORANT_TEAM_OWNERS_CHANNEL = 1361872170128642118
DBD_TEAM_OWNERS_CHANNEL = 1420875852194775163

OPENING_DROPS_CHANNEL = 1332055598057001021
CARD_BATTLE_CHANNEL = 1337831046217072711
CARD_BATTLE_RESULTS_CHANNEL = 1337903393825362072
MARVEL_RIVALS_MATCH_COMMANDS_CHANNEL = 1347315889652895847
VALORANT_MATCH_COMMANDS_CHANNEL = 1411045222825201715

PACK_EMOJI_ID = 1206654460735258654

RIVALS_CATEGORY_ID = 1316612507573424128
RIVALS_TEAMS_CATEGORY_ID = 1331720386995425290

VALORANT_CATEGORY_ID = 1361863357296152617
VALORANT_TEAMS_CATEGORY_ID = 1361875968704254052

DBD_CATEGORY_ID = 1419033285136224427

LEAGUE_NOTIFS_MENTION = '<@&1255683967353491476>'

MAX_WAGER = 10000
SECONDS_IN_A_WEEK = 604800

ALL_LEAGUE_CONTEXTS = {
    'OW', 'MR', 'VL', 'DB'
}

DEFAULT_GEMS = {
    'red': 0,
    'blue': 0,
    'yellow': 0,
    'green': 0,
    'purple': 0,
    'orange': 0,
    'pink': 0,
    'teal': 0,
    'white': 0,
    'black': 0
}

GEM_COLORS = [
    'red',
    'blue',
    'yellow',
    'green',
    'purple',
    'orange',
    'pink',
    'teal',
    'white',
    'black'
]

GEM_COLOR_TO_STRING = {
    'red': '<:gemred:1159202371998597211>',
    'blue': '<:gemblue:1159202447676424292>',
    'yellow': '<:gemyellow:1159202451652624495>',
    'green': '<:gemgreen:1159202443947679885>',
    'purple': '<:gempurple:1159202449068916837>',
    'orange': '<:gemorange:1159202446128730153>',
    'teal': '<:gemteal:1159202442559361104>',
    'pink': '<:gempink:1159202453028360334>',
    'white': '<:gemwhite:1159202441116516362>',
    'black': '<:gemblack:1159202439031959643>'
}

TEAM_NAME_TO_EMOJI_EMBED_STRING = {
    'Olympians': '<:olympians:1174062447779385464>',
    'Polar': '<:polar:1173786406238298242>',
    'Eclipse': '<:eclipse:1174517640987938926>',
    'Saviors': '<:saviors:1176588866828914748>',
    'Ragu': '<:ragu:1179505864294539324>',
    'Instigators': '<:instigators:1236040112798830763>',
    'Guardians': '<:guardians:1200148962443800616>',
    'Fresas': '<:fresas:1200202833170026669>',
    'Outliers': '<:outliers:1200928308922167357>',
    'Phoenix': '<:phoenix:1200926320767545484>',
    'Saturn': '<:saturn:1236025870460780654>',
    'Celestials': '<:celestials:1241135985258135573>',
    'Misfits': '<:misfits:1237197162354446336>',
    'Evergreen': '<:evergreen:1241087086207959040>',
    'Hunters': '<:hunters:1245542818731134976>',
    'Diamonds': '<:diamonds:1280213177782501437>',
    'Phantoms': '<:phantoms:1274435777559789690>',
    'Angels': '<:angels:1270065321226801233>',
    'Legion': '<:legion:1279173590218182666>',
    'Sentinels': '<:sentinels:1278802858338291753>',
    'Lotus': '<:lotus:1298683346314072234>',
    'Deadlock': '<:deadlock:1298375893839773818>',
    'Horizon': '<:horizon:1305322090513301564>',
    'Monarchs': '<:monarchs:1305323035611631616>',
    'Aces': '<:aces:1348420990023241769>',
    'Mantas': '<:mantas:1348446040927371304>',
    'Penguins': '<:penguins:1408887466575925421>',
    'Tsunami': '<:tsunami:1408887492123561994>',
    'Frogs': '<:spicyesports:1344813172342788177>'
}

DEFAULT_TEAM_EMOJI = '<:spicyesports:1344813172342788177>'

SPICY_DROP_EMOJI_STRING = '<:spicy_drop:1327677388720701450>'
SPICY_PACK_EMOJI_STRING = '<:pack:1206654460735258654>'
SPICY_COIN_EMOJI_STRING = '<:spicycoin:1414833315508125726>'
SPICY_VOUCHER_EMOJI_STRING = '<:spicy_voucher:1371334935557963910>'


MAP_NAME_TO_IMAGE = {

    # Control
    'Antarctic Peninsula': 'https://i.postimg.cc/Y0NWT7gh/Antarctic-Peninsula.webp',
    'Busan': 'https://i.postimg.cc/X7858V4P/Busan.webp',
    'Ilios': 'https://i.postimg.cc/jdKNPW0N/Ilios.webp',
    'Lijang Tower': 'https://i.postimg.cc/SQcCn65k/Lijang-Tower.webp',
    'Nepal': 'https://i.postimg.cc/pLcnwq9Y/Nepal.webp',
    'Oasis': 'https://i.postimg.cc/MppQ3hGp/Oasis.webp',
    'Samoa': 'https://i.postimg.cc/zfLR8KKm/Samoa.webp',

    # Escort
    'Circuit Royal': 'https://i.postimg.cc/52yXSLPH/Circuit-Royal.webp',
    'Dorado': 'https://i.postimg.cc/13dfCXTv/Dorado.webp',
    'Havana': 'https://i.postimg.cc/B69t3yJD/Havana.webp',
    'Junkertown': 'https://i.postimg.cc/wM9vymyj/Junkertown.webp',
    'Rialto': 'https://i.postimg.cc/d3n08Vrm/Rialto.webp',
    'Route 66': 'https://i.postimg.cc/rm1sw-JpH/Route-66.webp',
    'Shambali Monastery': 'https://i.postimg.cc/hPpJmp0W/Shambali-Monastery.webp',
    'Watchpoint Gibraltar': 'https://i.postimg.cc/DzbmtF3n/Watchpoint-Gibraltar.webp',

    # Flashpoint
    'New Junk City': 'https://i.postimg.cc/C1sMgxPT/New-Junk-City.webp',
    'Suravasa': 'https://i.postimg.cc/hv4DPR6J/Survasa.webp',

    # Hybrid
    'Blizzard World': 'https://i.postimg.cc/pdDRfdth/Blizzard-World.webp',
    'Eichenwalde': 'https://i.postimg.cc/90f2HtwZ/Eichenwalde.webp',
    'Hollywood': 'https://i.postimg.cc/9f3cw7sH/Hollywood.webp',
    "King's Row": 'https://i.postimg.cc/3R1hqbN3/King-s-Row.webp',
    'Midtown': 'https://i.postimg.cc/sDNjy8cX/Midtown.webp',
    'Numbani': 'https://i.postimg.cc/MpfWGDPY/Numbani.webp',
    'Paraiso': 'https://i.postimg.cc/26rm2fzH/Paraiso.webp',

    # Push
    'Colosseo': 'https://i.postimg.cc/k5ddgdtn/Colosseo.webp',
    'Esperanca': 'https://i.postimg.cc/jjQYWkzy/Esperanca.webp',
    'New Queen Street': 'https://i.postimg.cc/fRdNsby2/New-Queen-Street.webp',
    'Runasapi': 'https://i.imgur.com/2KxXZoX.png'

}

NO_MAP_IMAGE = 'https://i.postimg.cc/7ZGSyLRW/NoMap.png'

MAP_NAME_TO_NAME_IMG = {

    # Control
    'Antarctic Peninsula': 'https://i.postimg.cc/65X5WnXD/Antartic-Peninsula.png',
    'Busan': 'https://i.postimg.cc/MGvzPY7j/Busan.png',
    'Ilios': 'https://i.postimg.cc/pLVW8vyC/Ilios.png',
    'Lijang Tower': 'https://i.postimg.cc/3JFrdNrW/Lijang-Tower.png',
    'Nepal': 'https://i.postimg.cc/FHP9V6L4/Nepal.png',
    'Oasis': 'https://i.postimg.cc/xCmnYTFf/Oasis.png',
    'Samoa': 'https://i.postimg.cc/fbpD60Cq/Samoa.png',

    # Escort
    'Circuit Royal': 'https://i.postimg.cc/HLhXR3fG/Circuit-Royal.png',
    'Dorado': 'https://i.postimg.cc/cHtwSw-Sv/Dorado.png',
    'Havana': 'https://i.postimg.cc/J0bXy8tm/Havana.png',
    'Junkertown': 'https://i.postimg.cc/NGTmC6DV/Junkertown.png',
    'Rialto': 'https://i.postimg.cc/Y0cgq0rb/Rialto.png',
    'Route 66': 'https://i.postimg.cc/MKmRqzhm/Route-66.png',
    'Shambali Monastery': 'https://i.postimg.cc/wTpJC1bB/Shambali-Monastery.png',
    'Watchpoint Gibraltar': 'https://i.postimg.cc/dVQC0zFP/Watchpoint-Gibraltar.png',

    # Flashpoint
    'New Junk City': 'https://i.postimg.cc/3NpqdkgR/New-Junk-City.png',
    'Suravasa': 'https://i.postimg.cc/9XqKxnvh/Survasa.png',

    # Hybrid
    'Blizzard World': 'https://i.postimg.cc/T2rQ5Mzp/Blizzard-World.png',
    'Eichenwalde': 'https://i.postimg.cc/fTCK57Ts/Eichenwalde.png',
    'Hollywood': 'https://i.postimg.cc/HkPt1pyP/Hollywood.png',
    "King's Row": 'https://i.postimg.cc/xTn5KpQg/King-s-Row.png',
    'Midtown': 'https://i.postimg.cc/52tmrH6C/Midtown.png',
    'Numbani': 'https://i.postimg.cc/FKMg1DGy/Numbani.png',
    'Paraiso': 'https://i.postimg.cc/ZqBxT1PY/Paraiso.png',

    # Push
    'Colosseo': 'https://i.postimg.cc/Y2bGsdgd/Colosseo.png',
    'Esperanca': 'https://i.postimg.cc/HsncDb9d/Esperanca.png',
    'New Queen Street': 'https://i.postimg.cc/NMP4BBS0/New-Queen-Street.png',
    'Runasapi': 'https://i.imgur.com/Yl8xgqG.png'

}

NO_MAP_NAME = 'https://i.postimg.cc/hPNGk6G1/No-Map.png'

TEAM_LIST = ['Olympians', 'Polar', 'Eclipse', 'Saviors', 'Ragu', 'Instigators', 'Guardians',  'Fresas', 'Outliers', 'Phoenix', 
             'Celestials', 'Saturn', 'Evergreen', 'Misfits', 'Hunters', 'Legion', 'Diamonds', 'Angels', 'Phantoms', 'Sentinels',
             'Lotus', 'Deadlock', 'Horizon', 'Monarchs', 'Aces', 'Mantas', 'Penguins', 'Tsunami']

RIVALS_TEAM_LIST = ['Angels', 'Celestials', 'Deadlock', 'Evergreen', 'Fresas', 'Guardians', 'Hunters', 'Lotus', 'Misfits','Ragu']

VALORANT_TEAM_LIST = ['Deadlock', 'Guardians', 'Horizon', 'Hunters', 'Lotus', 'Polar', 'Ragu', 'Saviors']

DBD_TEAM_LIST = ['Ragu', 'Hunters']

LOWERCASE_HERO_NAMES = ['ana', 'ashe', 'baptiste', 'bastion', 'brigitte', 'cassidy', 'dva', 'doomfist', 'echo', 'genji', 'hanzo', 'illari', 
                        'junker queen', 'junkrat', 'juno', 'kiriko', 'lifeweaver', 'lucio', 'mauga', 'mei', 'mercy', 'moira', 'orisa', 'ramattra', 'reaper', 
                        'reinhardt', 'roadhog', 'sigma', 'sojourn', 'soldier 76', 'sombra', 'symmetra', 'torbjorn', 'tracer', 'venture', 'widowmaker', 
                        'winston', 'wrecking ball', 'zarya', 'zenyatta', 'pharah', 'hazard', 'wuyang', 'freja']

LOWERCASE_BAN_HERO_NAMES = ['ana', 'ashe', 'baptiste', 'bastion', 'brigitte', 'cassidy', 'dva', 'doomfist', 'echo', 'genji', 'hanzo', 'illari', 
                        'queen', 'junkrat', 'juno', 'kiriko', 'lifeweaver', 'lucio', 'mauga', 'mei', 'mercy', 'moira', 'orisa', 'ramattra', 'reaper', 
                        'reinhardt', 'roadhog', 'sigma', 'sojourn', 'soldier', 'sombra', 'symmetra', 'torbjorn', 'tracer', 'venture', 'widowmaker', 
                        'winston', 'ball', 'zarya', 'zenyatta', 'pharah', 'hazard', 'wuyang', 'freja']

SEASON_ACTIVE = False


TIMESLOT_TO_INFO = {

    'W-6': ['Wednesday', 6],
    'W-7': ['Wednesday', 7],
    'W-8': ['Wednesday', 8],
    'W-9': ['Wednesday', 9],
    'W-10': ['Wednesday', 10],

    'T-6': ['Thursday', 6],
    'T-7': ['Thursday', 7],
    'T-8': ['Thursday', 8],
    'T-9': ['Thursday', 9],
    'T-10': ['Thursday', 10],

    'F-6': ['Friday', 6],
    'F-7': ['Friday', 7],
    'F-8': ['Friday', 8],
    'F-9': ['Friday', 9],
    'F-10': ['Friday', 10],

    'S-2': ['Saturday', 2],
    'S-3': ['Saturday', 3],
    'S-4': ['Saturday', 4],
    'S-5': ['Saturday', 5],
    'S-6': ['Saturday', 6],
    'S-7': ['Saturday', 7],
    'S-8': ['Saturday', 8],
    'S-9': ['Saturday', 9],
    'S-10': ['Saturday', 10],

    'X-2': ['Sunday', 2],
    'X-3': ['Sunday', 3],
    'X-4': ['Sunday', 4],
    'X-5': ['Sunday', 5],
    'X-6': ['Sunday', 6],
    'X-7': ['Sunday', 7],
    'X-8': ['Sunday', 8],
    'X-9': ['Sunday', 9],
    'X-10': ['Sunday', 10],

}


DEFAULT_BLANK_USER = {
    "entries": [],
    'teams': [],
    'pickaxes': 0,
    'invited_valid': True,
    'level': 1,
    'xp': 0,
    'gems': copy.deepcopy(DEFAULT_GEMS),
    'lootboxes': [],
    'league_team': 'None',
    'league_invites': []
}


MAIN_BROADCASTER_ID = '192319978'
SECOND_BROADCASTER_ID = '1186754623'
THIRD_BROADCASTER_ID = '1272958195'

TWITCH_CLIENT_ID = '46t2o4ora6yz8o1x5ws18qn2ueiz4v'
SECOND_CLIENT_ID = 'flqc4bwzq9w2i6bxyybbuxrjnxtn6g'
THIRD_CLIENT_ID = 'ew6in7c0vlzjmr55ak2g0lfmv2kz33'


TOKEN_SHOP_USD_PRICES = [
    6, # 500 ow coins
    11, # 1,000 ow coins
    10, # battle new $10
    10, # discord nitro
    10, # 1,000 V-Bucks
    13, # steam card
    0, # 500 pp (discontinued)
]

# For auto-mod moderation
VERY_BAD_WORD_LIST = ['nigger', 'nigga', 'hitler', 'faggot', 'retard', 'beaner', 'chink']