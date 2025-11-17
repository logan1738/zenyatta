



from api import get_member
from discord_actions import get_guild

import constants
from safe_send import safe_send
from user.user import get_user_vouchers, user_exists


async def v_end_auction(db, client):
    auction = db['auction']
    auction.update_one({"auction_id": 2}, {"$set": {'is_open': False}})
    data = auction.find_one({'auction_id': 2})

    guild = await get_guild(client)
    auction_channel = guild.get_channel(constants.VOUCHER_AUCTION_CHANNEL)
    redemptions_channel = guild.get_channel(constants.OFFER_REDEMPTIONS_CHANNEL_ID)

    won_string = 'No one bid on the item!'
    if data['highest_bidder_id'] != 0:

        player_mention = '[PLAYER NOT FOUND]'
        member = get_member(guild, data['highest_bidder_id'], 'End Auction')
        if member:
            player_mention = member.mention

        user_bid = data['highest_bid']

        if member:
            user = user_exists(db, member.id)
            if user:
                users = db['users']
                user_vouchers = get_user_vouchers(user)

                if user_vouchers >= user_bid:
                    users.update_one({'discord_id': user['discord_id']}, {"$set": {'vouchers': user_vouchers - user_bid}})
                    won_string = player_mention+' won '+data['item_name']+' with a bid of '+str(user_bid)+' Vouchers!'
                else:
                    won_string = 'The user who won the auction does not have enough vouchers to cover their bid. Staff will handle the auction from here.'

    final_string = '--------------------------------\n'
    final_string += 'Auction Ended!\n'
    final_string += won_string

    await safe_send(redemptions_channel, won_string)
    await safe_send(auction_channel, final_string)



async def v_end_auction_handler(db, message, client):

    auction = db['auction']
    data = auction.find_one({'auction_id': 2})

    if not data['is_open']:
        await safe_send(message.channel, 'There is no current voucher auction.')
        return
    
    await v_end_auction(db, client)

    await safe_send(message.channel, 'Voucher auction ended.')