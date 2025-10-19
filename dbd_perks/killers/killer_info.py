
from dbd_perks.killers.individual_killer_stats.spirit import SPIRIT

ALL_KILLERS = {
    'SPIRIT': SPIRIT
}

def get_killer_from_name(killer_name):
    return ALL_KILLERS.get(killer_name.upper(), None)