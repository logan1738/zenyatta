

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES


class GHOST_FACE_ADD_ON_NAMES:

    PHILLY = '"Philly"'
    CHEAP_COLOGNE = "Cheap Cologne"
    HEADLINE_CUT_OUTS = "Headline Cut-Outs"
    WALLEYES_MATCHBOOK = "Walleye's Matchbook"
    CINCH_STRAPS = "Cinch Straps"
    MARKED_MAP = "Marked Map"
    OLSENS_ADDRESS_BOOK = "Olsen's Address Book"
    OLSENS_JOURNAL = "Olsen's Journal"
    TELEPHOTO_LENS = "Telephoto Lens"
    CHEWED_PEN = "Chewed Pen"
    KNIFE_BELT_CLIP = "Knife Belt Clip"
    LASTING_PERFUME = "Lasting Perfume"
    LEATHER_KNIFE_SHEATH = "Leather Knife Sheath"
    OLSENS_WALLET = "Olsen's Wallet"
    DRIVERS_LICENSE = "Driver's License"
    DROP_LEG_KNIFE_SHEATH = "Drop-Leg Knife Sheath"
    NIGHT_VISION_MONOCULAR = "Night Vision Monocular"
    VICTIMS_DETAILED_ROUTINE = "Victim's Detailed Routine"
    GHOST_FACE_CAUGHT_ON_TAPE = '"Ghost Face Caught on Tape"'
    OUTDOOR_SECURITY_CAMERA = "Outdoor Security Camera"


class GHOST_FACE:

    NAME = "Ghost Face"

    TIER = 5

    ALL_SURVIVOR_PERKS_BANNED = False

    BANNED_SURVIVOR_PERKS = []

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

    BANNED_KILLER_PERKS = []

    BANNED_KILLER_PERK_COMBOS = []

    ALL_KILLER_ADD_ONS = get_all_add_on_names(GHOST_FACE_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = []

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]