



from constants import DBD_DATA_VERSION
from dbd_perks.killers.killer_info import ALL_KILLERS
from helpers import get_constant_value, set_constant_value
from safe_send import safe_send




def generate_killer_list():

    killer_list = []

    for killer_key in ALL_KILLERS:
        killer = ALL_KILLERS[killer_key]
        killer_list.append({
            'name': killer.NAME,
            'tier': killer.TIER,
        })

    return killer_list



def copy_dbd_data_to_database(db):

    dbd_data = {
        'killer_list': generate_killer_list()
    }

    set_constant_value(db, 'dbd_data', dbd_data)
    set_constant_value(db, 'dbd_data_version', DBD_DATA_VERSION)
    

async def update_dbd_data(db, channel):

    current_dbd_data_version = get_constant_value(db, 'dbd_data_version')

    if current_dbd_data_version == DBD_DATA_VERSION:
        await safe_send(channel, 'DBD data is already up to date.')
        return
    
    copy_dbd_data_to_database(db)

    await safe_send(channel, f'DBD data updated to version {DBD_DATA_VERSION}.')