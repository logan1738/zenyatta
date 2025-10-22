from safe_send import safe_send

async def init_auction_handler(db, message):
    auction = db['auction']
    new_auction = {
        'auction_id': 1,
        'is_open': False,
        'item_name': 'NONE',
        'highest_bid': 0,
        'highest_bidder_id': 0
    }
    auction.insert_one(new_auction)
    
    await safe_send(message.channel, 'auction data initated')