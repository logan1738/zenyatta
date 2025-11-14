

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES


class CANNIBAL_ADD_ON_NAMES:

    CHAINSAW_FILE = "Chainsaw File"
    SPARK_PLUG = "Spark Plug"
    SPEED_LIMITER = "Speed Limiter"
    VEGETABLE_OIL = "Vegetable Oil"
    CHILLI = "Chilli"
    HOMEMADE_MUFFLER = "Homemade Muffler"
    KNIFE_SCRATCHES = "Knife Scratches"
    LONG_GUIDE_BAR = "Long Guide Bar"
    PRIMER_BULB = "Primer Bulb"
    BEGRIMED_CHAINS = "Begrimed Chains"
    GRISLY_CHAINS = "Grisly Chains"
    SHOP_LUBRICANT = "Shop Lubricant"
    THE_BEASTS_MARKS = "The Beast's Marks"
    THE_GREASE = "The Grease"
    AWARD_WINNING_CHILLI = "Award-Winning Chilli"
    DEPTH_GAUGE_RAKE = "Depth Gauge Rake"
    LIGHT_CHASIS = "Light Chasis"
    RUSTED_CHAINS = "Rusted Chains"
    CARBURETTOR_TUNING_GUIDE = "Carburettor Tuning Guide"
    IRIDESCENT_FLESH = "Iridescent Flesh"


class CANNIBAL:

    NAME = "Cannibal"

    TIER = 4

    ALL_SURVIVOR_PERKS_BANNED = True

    BANNED_SURVIVOR_PERKS = []

    BANNED_SURVIVOR_PERK_COMBOS = []

    SURVIVOR_OFFERINGS = {
        'offering1': [SURVIVOR_OFFERING_NAMES.VIGOS_SHROUD],
        'offering2': [SURVIVOR_OFFERING_NAMES.ANNOTATED_BLUEPRINT],
        'offering3': [SURVIVOR_OFFERING_NAMES.BLOODIED_BLUEPRINT, SURVIVOR_OFFERING_NAMES.TORN_BLUEPRINT],
        'offering4': []
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

    BANNED_KILLER_PERKS = []

    BANNED_KILLER_PERK_COMBOS = []

    ALL_KILLER_ADD_ONS = get_all_add_on_names(CANNIBAL_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = [
        CANNIBAL_ADD_ON_NAMES.LIGHT_CHASIS
    ]

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]