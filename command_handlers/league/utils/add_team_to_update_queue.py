

from helpers import get_constant_value


def add_team_to_update_queue(db, context, team_name):

    teams_to_update_document = get_constant_value(db, 'teams_to_update')
    teams_in_context = teams_to_update_document.get(context, [])

    if team_name not in teams_in_context:
        teams_in_context.append(team_name)
        db['constants'].update_one({'constant_name': 'teams_to_update'}, {'$set': {context: teams_in_context}})