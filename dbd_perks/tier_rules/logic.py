

from dbd_perks.tier_rules.tier1.tier1_banned_survivor_perks import TIER1_BANNED_SURVIVOR_PERKS


def get_survivor_perk_bans_for_tier(killer_tier):

    if killer_tier == 1:
        return TIER1_BANNED_SURVIVOR_PERKS

