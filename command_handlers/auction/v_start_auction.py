

from common_messages import invalid_number_of_params
import constants
from discord_actions import get_guild
from helpers import make_string_from_word_list
from safe_send import safe_send
from time_helpers import get_current_day_est


async def start_voucher_auction(client, db, item_name):

    auction = db['auction']

    auction.update_one({"auction_id": 2}, {"$set": 
        {
        'item_name': item_name,
        'is_open': True,
        'highest_bid': 1,
        'highest_bidder_id': 0
        }
    })

    guild = await get_guild(client)
    auction_channel = guild.get_channel(constants.VOUCHER_AUCTION_CHANNEL)

    final_string = '--------------------------------\n'
    final_string += 'NEW VOUCHER AUCTION STARTED FOR: **'+item_name+'**\n'
    final_string += 'Starting bid is **1 Voucher**\n'
    final_string += 'To bid on this item use the command **!vbid [number of vouchers]**'

    constants_db = db['constants']
    today_number = get_current_day_est()
    constants_db.update_one({'name': 'vbid_day'}, {"$set": { 'value': today_number } })

    await safe_send(auction_channel, final_string)


async def v_start_auction_handler(db, message, client):

    word_parts = message.content.split()
    if len(word_parts) < 2:
        await invalid_number_of_params(message)
        return

    auction = db['auction']
    data = auction.find_one({'auction_id': 2})

    if data['is_open']:
        await safe_send(message.channel, 'A voucher auction is currently open. Please end the current auction first.')
        return
    
    item_name = make_string_from_word_list(word_parts, 1)

    await start_voucher_auction(client, db, item_name)
    
    await safe_send(message.channel, 'Voucher auction started.')