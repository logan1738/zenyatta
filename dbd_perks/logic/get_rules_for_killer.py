
from dbd_perks.
from dbd_perks.killers.killer_info import KILLERS, get_killer_from_name

async def get_rules_for_killer(killer_name):

    killer_class = get_killer_from_name(killer_name)
    if not killer_class:
        raise ValueError(f"Killer '{killer_name}' not found.")
    

    base_banned_survivor_perks = 


    killer_banned_survivor_perks = killer_class.BANNED_SURVIVOR_PERKS
    killer_banned_killer_perks = killer_class.BANNED_KILLER_PERKS

    return {
        'banned_survivor_perks': [],
        'banned_killer_perks': []
    }