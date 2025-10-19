



from constants import DBD_DATA_VERSION
from helpers import get_constant_value
from safe_send import safe_send


def copy_dbd_data_to_database():

    print('This function is not implemented yet')


async def update_dbd_data(db, channel):

    current_dbd_data_version = get_constant_value(db, 'dbd_data_version')

    if current_dbd_data_version == DBD_DATA_VERSION:
        await safe_send(channel, 'DBD data is already up to date.')
        return
    
    copy_dbd_data_to_database()

    await safe_send(channel, f'DBD data updated to version {DBD_DATA_VERSION}.')