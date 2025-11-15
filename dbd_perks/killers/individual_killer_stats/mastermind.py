

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES
from dbd_perks.survivor_perk_names import SURVIVOR_PERK_NAMES

class MASTERMIND_ADD_ON_NAMES:

    JEWEL_BEETLE = "Jewel Beetle"
    RPD_SHOULDER_WALKIE = "R.P.D. Shoulder Walkie"
    UNICORN_MEDALLION = "Unicorn Medallion"
    UROBOROS_TENDRIL = "Uroboros Tendril"
    BULLHORN = "Bullhorn"
    CHALICE_GOLD = "Chalice (Gold)"
    LEATHER_GLOVES = "Leather Gloves"
    LION_MEDALLION = "Lion Medallion"
    LOOSE_CRANK = "Loose Crank"
    EGG_GOLD = "Egg (Gold)"
    MAIDEN_MEDALLION = "Maiden Medallion"
    PORTABLE_SAFE = "Portable Safe"
    RED_HERB = "Red Herb"
    VIDEO_CONFERENCE_DEVICE = "Video Conference Device"
    DARK_SUNGLASSES = "Dark Sunglasses"
    GREEN_HERB = "Green Herb"
    HELICOPTER_STICK = "Helicopter Stick"
    UROBOROS_VIRUS = "Uroboros Virus"
    IRIDESCENT_UROBOROS_VIAL = "Iridescent Uroboros Vial"
    LAB_PHOTO = "Lab Photo"



class MASTERMIND:

    NAME = "Mastermind"

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

    BANNED_KILLER_PERKS = []

    BANNED_KILLER_PERK_COMBOS = []

    ALL_KILLER_ADD_ONS = get_all_add_on_names(MASTERMIND_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = []

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]