



from constants import DBD_DATA_VERSION
from dbd_perks.killers.killer_info import ALL_KILLERS
from dbd_perks.survivor_base_banned_perks import SURVIVOR_BASE_BANNED_PERKS
from dbd_perks.survivor_perk_names import get_all_survivor_perk_names
from dbd_perks.tier_rules.logic import get_survivor_perk_bans_for_tier, get_survivor_perk_combo_bans_for_tier
from helpers import get_constant_value, set_constant_value
from safe_send import safe_send


def generate_allowed_survivor_perks(killer):

    all_perk_array = get_all_survivor_perk_names()

    allowed_perks = []

    base_banned_perks = SURVIVOR_BASE_BANNED_PERKS
    tier_banned_perks = get_survivor_perk_bans_for_tier(killer.TIER)
    killer_specific_banned_perks = killer.BANNED_SURVIVOR_PERKS

    banned_perks = set(base_banned_perks + tier_banned_perks + killer_specific_banned_perks)

    for perk in all_perk_array:
        if perk not in banned_perks:
            allowed_perks.append(perk)

    return allowed_perks


def combine_banned_survivor_perk_combos(killer):

    killer_specific_banned_combos = killer.BANNED_SURVIVOR_PERK_COMBOS
    tier_specific_banned_combos = get_survivor_perk_combo_bans_for_tier(killer.TIER)

    combined_banned_combos = tier_specific_banned_combos + killer_specific_banned_combos

    return combined_banned_combos


def generate_allowed_killer_add_ons(killer):

    all_add_ons = killer.ALL_KILLER_ADD_ONS

    banned_add_ons = set(killer.BANNED_KILLER_ADD_ONS)

    allowed_add_ons = []

    for add_on in all_add_ons:
        if add_on not in banned_add_ons:
            allowed_add_ons.append(add_on)

    return allowed_add_ons


def generate_killer_list():

    killer_list = []

    for killer_key in ALL_KILLERS:
        killer = ALL_KILLERS[killer_key]
        killer_list.append({
            'name': killer.NAME,
            'tier': killer.TIER,
            'all_survivor_perks_banned': killer.ALL_SURVIVOR_PERKS_BANNED,
            'allowed_survivor_perks': generate_allowed_survivor_perks(killer),
            'forbidden_perk_combos': combine_banned_survivor_perk_combos(killer),
            'survivor_items': killer.SURVIVOR_ITEMS,
            'survivor_offerings': killer.SURVIVOR_OFFERINGS,
            'allowed_killer_add_ons': generate_allowed_killer_add_ons(killer),
            'killer_offerings': killer.KILLER_OFFERINGS
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