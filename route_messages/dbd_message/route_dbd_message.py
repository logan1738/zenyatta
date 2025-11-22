

from dbd.base_commands.username import dbd_username_handler
from dbd.swf.admin.swf_cancel import swf_cancel_handler
from dbd.swf.admin.swf_pick import swf_pick_handler
from dbd.swf.admin.swf_replace import swf_replace_handler
from dbd.swf.admin.swf_result import swf_result_handler
from dbd.swf.admin.swf_start import swf_start_handler
from dbd.swf.user.swf_leaderboard import swf_leaderboard_handler
from dbd.swf.user.swf_stats import swf_stats_handler
from safe_send import safe_send

async def route_dbd_message(client, db, message, lower_message, is_admin):

    if lower_message.startswith('!username'):
        await dbd_username_handler(db, message, client)

    elif lower_message == '!swfstats':
        await swf_stats_handler(db, message)

    elif lower_message == '!swfleaderboard':
        await swf_leaderboard_handler(db, message)

    elif lower_message == '!swfstart' and is_admin:
        await swf_start_handler(client, db, message)

    elif lower_message == '!swfcancel' and is_admin:
        await swf_cancel_handler(client, db, message)
    
    elif lower_message == '!swfpick' and is_admin:
        await swf_pick_handler(client, db, message)

    elif lower_message.startswith('!swfreplace ') and is_admin:
        await swf_replace_handler(client, db, message)

    elif lower_message == '!swfwin' and is_admin:
        await swf_result_handler(client, db, message, True)

    elif lower_message == '!swfloss' and is_admin:
        await swf_result_handler(client, db, message, False)

    else:
        await safe_send(message.channel, 'Invalid command. Please see **!help** for a list of commands.')