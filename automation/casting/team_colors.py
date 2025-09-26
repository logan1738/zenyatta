


from common_messages import invalid_number_of_params
from helpers import valid_number_of_params
from safe_send import safe_send


# color vars:
YELLOW = 'YELLOW'
LIME_GREEN = 'LIME GREEN'
NEON_BLUE = 'NEON BLUE'
AQUA = 'AQUA'
TAWNY = 'TAWNY'
ORANGE = 'ORANGE'
MAGENTA = 'MAGENTA'
BLUE = 'BLUE'
RED = 'RED'
GOLD = 'GOLD'
GREEN = 'GREEN'
PINK = 'PINK'
PURPLE = 'PURPLE'


INCOMPATIBLE_COLORS = {
    YELLOW: [LIME_GREEN, GOLD],
    LIME_GREEN: [YELLOW],
    NEON_BLUE: [BLUE],
    AQUA: [],
    TAWNY: [ORANGE],
    ORANGE: [TAWNY, GOLD],
    MAGENTA: [PINK],
    BLUE: [NEON_BLUE],
    RED: [],
    GOLD: [YELLOW, LIME_GREEN, ORANGE],
    GREEN: [],
    PINK: [MAGENTA],
    PURPLE: []
}


TEAM_DEFAULT_COLORS = {

    'Aces': {
        'primary': RED,
        'secondary': PURPLE
    },

    'Angels': {
        'primary': YELLOW,
        'secondary': NEON_BLUE
    },

    'Celestials': {
        'primary': BLUE,
        'secondary': AQUA
    },

    'Deadlock': {
        'primary': RED,
        'secondary': ORANGE
    },

    'Diamonds': {
        'primary': NEON_BLUE,
        'secondary': AQUA
    },

    'Eclipse': {
        'primary': AQUA,
        'secondary': BLUE
    },

    'Evergreen': {
        'primary': GREEN,
        'secondary': PINK
    },

    'Fresas': {
        'primary': RED,
        'secondary': LIME_GREEN
    },

    'Guardians': {
        'primary': MAGENTA,
        'secondary': PURPLE
    },

    'Horizon': {
        'primary': TAWNY,
        'secondary': PURPLE
    },

    'Hunters': {
        'primary': GREEN,
        'secondary': GOLD
    },

    'Instigators': {
        'primary': PURPLE,
        'secondary': AQUA,
    },

    'Legion': {
        'primary': RED,
        'secondary': PURPLE
    },

    'Lotus': {
        'primary': PINK,
        'secondary': GOLD
    },

    'Mantas': {
        'primary': AQUA,
        'secondary': BLUE
    },

    'Misfits': {
        'primary': LIME_GREEN,
        'secondary': GREEN
    },

    'Monarchs': {
        'primary': ORANGE,
        'secondary': GOLD
    },

    'Olympians': {
        'primary': GOLD,
        'secondary': ORANGE
    },

    'Outliers': {
        'primary': PURPLE,
        'secondary': TAWNY
    },

    'Penguins': {
        'primary': TAWNY,
        'secondary': YELLOW
    },

    'Phantoms': {
        'primary': BLUE,
        'secondary': PURPLE
    },

    'Phoenix': {
        'primary': TAWNY,
        'secondary': GOLD
    },

    'Polar': {
        'primary': NEON_BLUE,
        'secondary': AQUA
    },

    'Ragu': {
        'primary': RED,
        'secondary': PURPLE
    },

    'Saturn': {
        'primary': ORANGE,
        'secondary': GOLD
    },

    'Saviors': {
        'primary': PURPLE,
        'secondary': MAGENTA
    },

    'Sentinels': {
        'primary': PURPLE,
        'secondary': AQUA
    },

    'Tsunami': {
        'primary': AQUA,
        'secondary': BLUE
    },
}


COLOR_OVERRIDES = {

    'Aces-Deadlock': {
        'Aces': PURPLE,
        'Deadlock': RED
    },

    'Aces-Fresas': {
        'Aces': RED,
        'Fresas': LIME_GREEN
    },

    'Aces-Legion': {
        'Aces': PURPLE,
        'Legion': RED
    },

    'Aces-Ragu': {
        'Aces': PURPLE,
        'Ragu': RED
    },

    'Angels-Misfits': {
        'Angels': YELLOW,
        'Misfits': GREEN
    },

    'Angels-Olympians': {
        'Angels': NEON_BLUE,
        'Olympians': GOLD
    },

    'Celestials-Diamonds': {
        'Celestials': AQUA,
        'Diamonds': NEON_BLUE
    },

    'Celestials-Phantoms': {
        'Celestials': BLUE,
        'Phantoms': PURPLE
    },

    'Celestials-Polar': {
        'Celestials': AQUA,
        'Polar': NEON_BLUE
    },

    'Deadlock-Fresas': {
        'Deadlock': RED,
        'Fresas': LIME_GREEN
    },

    'Deadlock-Legion': {
        'Deadlock': ORANGE,
        'Legion': RED
    },

    'Deadlock-Ragu': {
        'Deadlock': ORANGE,
        'Ragu': RED
    },

    'Diamonds-Phantoms': {
        'Diamonds': NEON_BLUE,
        'Phantoms': PURPLE
    },

    'Diamonds-Polar': {
        'Diamonds': NEON_BLUE,
        'Polar': AQUA
    },

    'Eclipse-Mantas': {
        'Eclipse': BLUE,
        'Mantas': AQUA
    },

    'Eclipse-Tsunami': {
        'Eclipse': BLUE,
        'Tsunami': AQUA
    },

    'Evergreen-Hunters': {
        'Evergreen': PINK,
        'Hunters': GREEN
    },

    'Fresas-Legion': {
        'Fresas': LIME_GREEN,
        'Legion': RED
    },

    'Fresas-Ragu': {
        'Fresas': LIME_GREEN,
        'Ragu': RED
    },

    'Guardians-Lotus': {
        'Guardians': PURPLE,
        'Lotus': PINK
    },

    'Horizon-Monarchs': {
        'Horizon': PURPLE,
        'Monarchs': ORANGE
    },

    'Horizon-Penguins': {
        'Horizon': PURPLE,
        'Penguins': TAWNY
    },

    'Horizon-Phoenix': {
        'Horizon': PURPLE,
        'Phoenix': TAWNY
    },

    'Horizon-Saturn': {
        'Horizon': PURPLE,
        'Saturn': ORANGE
    },

    'Instigators-Outliers': {
        'Instigators': PURPLE,
        'Outliers': TAWNY
    },

    'Instigators-Saviors': {
        'Instigators': AQUA,
        'Saviors': PURPLE
    },

    'Instigators-Sentinels': {
        'Instigators': AQUA,
        'Sentinels': PURPLE
    },

    'Legion-Ragu': {
        'Legion': PURPLE,
        'Ragu': RED
    },

    'Mantas-Tsunami': {
        'Mantas': AQUA,
        'Tsunami': BLUE
    },

    'Misfits-Olympians': {
        'Misfits': GREEN,
        'Olympians': GOLD
    },

    'Monarchs-Penguins': {
        'Monarchs': GOLD,
        'Penguins': TAWNY
    },

    'Monarchs-Phoenix': {
        'Monarchs': GOLD,
        'Phoenix': TAWNY
    },

    'Monarchs-Saturn': {
        'Monarchs': GOLD,
        'Saturn': TAWNY
    },

    'Monarchs-Olympians': {
        'Monarchs': ORANGE,
        'Olympians': YELLOW
    },

    'Olympians-Saturn': {
        'Olympians': GOLD,
        'Saturn': TAWNY
    },

    'Outliers-Saviors': {
        'Outliers': TAWNY,
        'Saviors': PURPLE
    },

    'Outliers-Sentinels': {
        'Outliers': TAWNY,
        'Sentinels': PURPLE
    },

    'Penguins-Phoenix': {
        'Penguins': GOLD,
        'Phoenix': TAWNY
    },

    'Penguins-Saturn': {
        'Penguins': TAWNY,
        'Saturn': GOLD
    },

    'Phantoms-Polar': {
        'Phantoms': PURPLE,
        'Polar': NEON_BLUE
    },

    'Phoenix-Saturn': {
        'Phoenix': TAWNY,
        'Saturn': GOLD
    },

    'Saviors-Sentinels': {
        'Saviors': PURPLE,
        'Sentinels': AQUA
    },

}

def colors_compatible(color1, color2):

    if color1 == color2:
        return False

    if color1 in INCOMPATIBLE_COLORS[color2]:
        return False
    
    if color2 in INCOMPATIBLE_COLORS[color1]:
        return False
    
    return True


def build_override_string(team1, team2):

    # find which comes first alphabetically
    if team1 < team2:
        return f"{team1}-{team2}"
    else:
        return f"{team2}-{team1}"



def normalize_team_name(team_name):

    team_name_lower = team_name.lower()

    # capitalize first letter
    return team_name_lower.capitalize()


async def team_colors_handler(message):

    valid_params, params = valid_number_of_params(message, 3)
    if not valid_params:
        await invalid_number_of_params(message)
        return
    
    team_1 = params[1]
    team_2 = params[2]

    team_1 = normalize_team_name(team_1)
    team_2 = normalize_team_name(team_2)

    if team_1 not in TEAM_DEFAULT_COLORS:
        await safe_send(message.channel, 'Invalid team name: '+team_1)
        return
    
    if team_2 not in TEAM_DEFAULT_COLORS:
        await safe_send(message.channel, 'Invalid team name: '+team_2)
        return
    
    if team_1 == team_2:
        await safe_send(message.channel, 'A team cannot play against itself!')
        return

    team_1_color = TEAM_DEFAULT_COLORS[team_1]['primary']
    team_2_color = TEAM_DEFAULT_COLORS[team_2]['primary']

    if not colors_compatible(team_1_color, team_2_color):

        override_string = build_override_string(team_1, team_2)

        if not override_string in COLOR_OVERRIDES:
            await safe_send('Incompatible team colors! Please let an admin know so they can add an override for this matchup.')
            return
        
        override = COLOR_OVERRIDES[override_string]

        team_1_color = override[team_1]
        team_2_color = override[team_2]

    await safe_send(message, f"Team colors for {team_1} vs {team_2}:\n{team_1}: {team_1_color}\n{team_2}: {team_2_color}")
