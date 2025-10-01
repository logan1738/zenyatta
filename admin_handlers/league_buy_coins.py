

from helpers import can_be_int, get_constant_value, set_constant_value, valid_number_of_params
from safe_send import safe_send


async def league_buy_coins(db, message):

    valid_params, params = valid_number_of_params(message.content, 2)
    if not valid_params:
        await safe_send(message.channel, "Usage: !leaguebuycoins <number_of_coins>")
        return
    
    num_coins = params[1]
    if not can_be_int(num_coins):
        await safe_send(message.channel, "The number of coins must be an integer.")
        return

    num_coins = int(num_coins)
    if num_coins <= 0:
        await safe_send(message.channel, "The number of coins must be a positive integer.")
        return
    
    free_vouchers = get_constant_value(db, 'free_vouchers')

    free_vouchers += num_coins

    set_constant_value(db, 'free_vouchers', free_vouchers)

    await safe_send(message.channel, f'Successfully recorded that the league purchased {num_coins} coins from the market.')

    

    
