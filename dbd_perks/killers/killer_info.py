
from dbd_perks.killers.individual_killer_stats.animatronic import ANIMATRONIC
from dbd_perks.killers.individual_killer_stats.blight import BLIGHT
from dbd_perks.killers.individual_killer_stats.cannibal import CANNIBAL
from dbd_perks.killers.individual_killer_stats.dark_lord import DARK_LORD
from dbd_perks.killers.individual_killer_stats.deathslinger import DEATHSLINGER
from dbd_perks.killers.individual_killer_stats.demogorgon import DEMOGORGON
from dbd_perks.killers.individual_killer_stats.executioner import EXECUTIONER
from dbd_perks.killers.individual_killer_stats.ghost_face import GHOST_FACE
from dbd_perks.killers.individual_killer_stats.hillbilly import HILLBILLY
from dbd_perks.killers.individual_killer_stats.huntress import HUNTRESS
from dbd_perks.killers.individual_killer_stats.legion import LEGION
from dbd_perks.killers.individual_killer_stats.mastermind import MASTERMIND
from dbd_perks.killers.individual_killer_stats.oni import ONI
from dbd_perks.killers.individual_killer_stats.pig import PIG
from dbd_perks.killers.individual_killer_stats.singularity import SINGULARITY
from dbd_perks.killers.individual_killer_stats.spirit import SPIRIT
from dbd_perks.killers.individual_killer_stats.unknown import UNKNOWN
from dbd_perks.killers.individual_killer_stats.wraith import WRAITH

ALL_KILLERS = {
    'ANIMATRONIC': ANIMATRONIC,
    'BLIGHT': BLIGHT,
    'CANNIBAL': CANNIBAL,
    'DARK_LORD': DARK_LORD,
    'DEATHSLINGER': DEATHSLINGER,
    'DEMOGORGON': DEMOGORGON,
    'EXECUTIONER': EXECUTIONER,
    'GHOST_FACE': GHOST_FACE,
    'HILLBILLY': HILLBILLY,
    'HUNTRESS': HUNTRESS,
    'LEGION': LEGION,
    'MASTERMIND': MASTERMIND,
    'ONI': ONI,
    'PIG': PIG,
    'SINGULARITY': SINGULARITY,
    'SPIRIT': SPIRIT,
    'UNKNOWN': UNKNOWN,
    'WRAITH': WRAITH,
}

def get_killer_from_name(killer_name):
    return ALL_KILLERS.get(killer_name.upper(), None)

