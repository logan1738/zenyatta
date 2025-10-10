
from dbd_perks.killers.individual_killer_stats.spirit import SPIRIT

KILLERS = {
    'SPIRIT': SPIRIT
}

def get_killer_from_name(killer_name):
    return KILLERS.get(killer_name.upper(), None)