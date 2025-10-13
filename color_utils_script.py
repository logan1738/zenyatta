

from automation.casting.team_colors import COLOR_OVERRIDES, INCOMPATIBLE_COLORS, TEAM_DEFAULT_COLORS


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


def get_incompatible_teams():

    for team in TEAM_DEFAULT_COLORS:
        
        primary_color = TEAM_DEFAULT_COLORS[team]['primary']

        for other_team in TEAM_DEFAULT_COLORS:

            if team != other_team:
                other_team_primary_color = TEAM_DEFAULT_COLORS[other_team]['primary']

                if not colors_compatible(primary_color, other_team_primary_color):

                    override_string = build_override_string(team, other_team)
                    if not override_string in COLOR_OVERRIDES:
                        print(f"{team} ({primary_color}) is incompatible with {other_team} ({other_team_primary_color})")


get_incompatible_teams()