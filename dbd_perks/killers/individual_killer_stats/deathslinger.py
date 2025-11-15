

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killer_perk_names import KILLER_PERK_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES
from dbd_perks.survivor_perk_names import SURVIVOR_PERK_NAMES

class DEATHSLINGER_ADD_ON_NAMES:

    MODDIFIED_AMMO_BELT = "Moddified Ammo Belt"
    RICKETY_CHAIN = "Rickety Chain"
    SNAKE_OIL = "Snake Oil"
    SPIT_POLISH_RAG = "Spit Polish Rag"
    CHEWING_TOBACCO = "Chewing Tobacco"
    JAW_SMASHER = "Jaw Smasher"
    MARSHALS_BADGE = "Marshal's Badge"
    POISON_OAK_LEAVES = "Poison Oak Leaves"
    RUSTED_SPIKE = "Rusted Spike"
    BAYSHORES_GOLD_TOOTH = "Bayshore's Gold Tooth"
    HONEY_LOCUST_THORN = "Honey Locust Thorn"
    TIN_OIL_CAN = "Tin Oil Can"
    WANTED_POSTER = "Wanted Poster"
    WARDENS_KEYS = "Warden's Keys"
    BARBED_WIRE = "Barbed Wire"
    BAYSHORES_CIGAR = "Bayshore's Cigar"
    GOLD_CREEK_WHISKEY = "Gold Creek Whiskey"
    PRISON_CHAIN = "Prison Chain"
    HELLSHIRE_IRON = "Hellshire Iron"
    IRIDESCENT_COIN = "Iridescent Coin"

class DEATHSLINGER:

    NAME = "Deathslinger"

    TIER = 3

    ALL_SURVIVOR_PERKS_BANNED = False

    BANNED_SURVIVOR_PERKS = [
        SURVIVOR_PERK_NAMES.LITHE
    ]

    BANNED_SURVIVOR_PERK_COMBOS = []

    SURVIVOR_OFFERINGS = {
        'offering1': [SURVIVOR_OFFERING_NAMES.SHROUD_OF_BINDING],
        'offering2': [SURVIVOR_OFFERING_NAMES.VIGOS_SHROUD],
        'offering3': [SURVIVOR_OFFERING_NAMES.ANNOTATED_BLUEPRINT],
        'offering4': [SURVIVOR_OFFERING_NAMES.BLOODIED_BLUEPRINT, SURVIVOR_OFFERING_NAMES.TORN_BLUEPRINT]
    }

    SURVIVOR_ITEMS = [
        {
            'item': SURVIVOR_ITEM_NAMES.SPORT_FLASHLIGHT,
            'add_ons': [
                SURVIVOR_ITEM_ADD_ON_NAMES.BATTERY,
                SURVIVOR_ITEM_ADD_ON_NAMES.LEATHER_GRIP,
                SURVIVOR_ITEM_ADD_ON_NAMES.POWER_BULB,
                SURVIVOR_ITEM_ADD_ON_NAMES.WIDE_LENS
            ]
        },
        {
            'item': SURVIVOR_ITEM_NAMES.CHINESE_FIRECRACKER,
            'add_ons': []
        }
    ]

    BANNED_KILLER_PERKS = [
        KILLER_PERK_NAMES.HUBRIS
    ]

    BANNED_KILLER_PERK_COMBOS = []

    ALL_KILLER_ADD_ONS = get_all_add_on_names(DEATHSLINGER_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = [
        DEATHSLINGER_ADD_ON_NAMES.HELLSHIRE_IRON,
        DEATHSLINGER_ADD_ON_NAMES.IRIDESCENT_COIN
    ]

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]