

import asyncio
from api import get_member
from command_handlers.auction.start_auction import start_auction
from discord_actions import get_guild

import constants
from rewards import change_tokens
from safe_send import safe_send
from user.user import user_exists


async def end_auction(db, client):
    auction = db['auction']
    auction.update_one({"auction_id": 1}, {"$set": {'is_open': False}})
    data = auction.find_one({'auction_id': 1})

    guild = await get_guild(client)
    auction_channel = guild.get_channel(constants.DAILY_AUCTION_CHANNEL)
    redemptions_channel = guild.get_channel(constants.OFFER_REDEMPTIONS_CHANNEL_ID)

    won_string = 'No one bid on the item!'
    if data['highest_bidder_id'] != 0:

        player_mention = '[PLAYER NOT FOUND]'
        member = get_member(guild, data['highest_bidder_id'], 'End Auction')
        if member:
            player_mention = member.mention

        user_bid = data['highest_bid']

        won_string = player_mention+' won '+data['item_name']+' with a bid of '+str(user_bid)+' Tokens!'

        if member:
            user = user_exists(db, member.id)
            if user:

                users = db['users']
                users.update_one({'discord_id': user['discord_id']}, {"$set": {'tokens': user['tokens'] - user_bid, 'vouchers': user['vouchers'] + 20}})

    final_string = '--------------------------------\n'
    final_string += 'Auction Ended!\n'
    final_string += won_string

    await safe_send(redemptions_channel, won_string)
    await safe_send(auction_channel, final_string)

    await asyncio.sleep(5)

    await start_auction(client, db, '<:spicy_voucher:1371334935557963910> **20 Vouchers** <:spicy_voucher:1371334935557963910>')


async def end_auction_handler(db, message, client):

    auction = db['auction']
    data = auction.find_one({'auction_id': 1})

    if not data['is_open']:
        await safe_send(message.channel, 'There is no current auction.')
        return
    
    await end_auction(db, client)

    await safe_send(message.channel, 'Auction ended.')