import constants

def get_context(message):

    context = 'OW'
    message_channel = message.channel

    if message_channel.category_id == constants.RIVALS_CATEGORY_ID or message_channel.category_id == constants.RIVALS_TEAMS_CATEGORY_ID or message_channel.id == constants.MARVEL_RIVALS_MATCH_COMMANDS_CHANNEL or message.channel.id == constants.MARVEL_ADMIN_COMMAND_CHANNEL:
        context = 'MR'

    elif message_channel.category_id == constants.DBD_CATEGORY_ID or message.channel.id == constants.DBD_ADMIN_COMMAND_CHANNEL:
        context = 'DB'
        
    return context