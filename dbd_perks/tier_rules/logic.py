



from dbd_perks.tier_rules.tier1 import TIER_1_BANNED_KILLER_PERK_COMBOS, TIER_1_BANNED_KILLER_PERKS, TIER_1_BANNED_SURVIVOR_PERK_COMBOS, TIER_1_BANNED_SURVIVOR_PERKS
from dbd_perks.tier_rules.tier2 import TIER_2_BANNED_KILLER_PERK_COMBOS, TIER_2_BANNED_KILLER_PERKS, TIER_2_BANNED_SURVIVOR_PERK_COMBOS, TIER_2_BANNED_SURVIVOR_PERKS
from dbd_perks.tier_rules.tier3 import TIER_3_BANNED_KILLER_PERK_COMBOS, TIER_3_BANNED_KILLER_PERKS, TIER_3_BANNED_SURVIVOR_PERK_COMBOS, TIER_3_BANNED_SURVIVOR_PERKS
from dbd_perks.tier_rules.tier4 import TIER_4_BANNED_KILLER_PERK_COMBOS, TIER_4_BANNED_KILLER_PERKS, TIER_4_BANNED_SURVIVOR_PERK_COMBOS, TIER_4_BANNED_SURVIVOR_PERKS
from dbd_perks.tier_rules.tier5 import TIER_5_BANNED_KILLER_PERK_COMBOS, TIER_5_BANNED_KILLER_PERKS, TIER_5_BANNED_SURVIVOR_PERK_COMBOS, TIER_5_BANNED_SURVIVOR_PERKS


def get_survivor_perk_bans_for_tier(killer_tier):

    if killer_tier == 1:
        return TIER_1_BANNED_SURVIVOR_PERKS
    elif killer_tier == 2:
        return TIER_2_BANNED_SURVIVOR_PERKS
    elif killer_tier == 3:
        return TIER_3_BANNED_SURVIVOR_PERKS
    elif killer_tier == 4:
        return TIER_4_BANNED_SURVIVOR_PERKS
    elif killer_tier == 5:
        return TIER_5_BANNED_SURVIVOR_PERKS
    
    return []


def get_survivor_perk_combo_bans_for_tier(killer_tier):

    if killer_tier == 1:
        return TIER_1_BANNED_SURVIVOR_PERK_COMBOS
    elif killer_tier == 2:
        return TIER_2_BANNED_SURVIVOR_PERK_COMBOS
    elif killer_tier == 3:
        return TIER_3_BANNED_SURVIVOR_PERK_COMBOS
    elif killer_tier == 4:
        return TIER_4_BANNED_SURVIVOR_PERK_COMBOS
    elif killer_tier == 5:
        return TIER_5_BANNED_SURVIVOR_PERK_COMBOS

    return []


def get_killer_perk_bans_for_tier(killer_tier):

    if killer_tier == 1:
        return TIER_1_BANNED_KILLER_PERKS
    elif killer_tier == 2:
        return TIER_2_BANNED_KILLER_PERKS
    elif killer_tier == 3:
        return TIER_3_BANNED_KILLER_PERKS
    elif killer_tier == 4:
        return TIER_4_BANNED_KILLER_PERKS
    elif killer_tier == 5:
        return TIER_5_BANNED_KILLER_PERKS
    
    return []


def get_killer_perk_combo_bans_for_tier(killer_tier):

    if killer_tier == 1:
        return TIER_1_BANNED_KILLER_PERK_COMBOS
    elif killer_tier == 2:
        return TIER_2_BANNED_KILLER_PERK_COMBOS
    elif killer_tier == 3:
        return TIER_3_BANNED_KILLER_PERK_COMBOS
    elif killer_tier == 4:
        return TIER_4_BANNED_KILLER_PERK_COMBOS
    elif killer_tier == 5:
        return TIER_5_BANNED_KILLER_PERK_COMBOS

    return []
