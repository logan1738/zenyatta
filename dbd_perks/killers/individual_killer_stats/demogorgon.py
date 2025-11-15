

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES
from dbd_perks.survivor_perk_names import SURVIVOR_PERK_NAMES

class DEMOGORGON_ADD_ON_NAMES:

    BLACK_HEART = "Black Heart"
    RAT_LIVER = "Rat Liver"
    RAT_TAIL = "Rat Tail"
    ROTTEN_PUMPKIN = "Rotten Pumpkin"
    BARBS_GLASSES = "Barb's Glasses"
    MEWS_GUTS = "Mews' Guts"
    ROTTEN_GREEN_TRIPE = "Rotten Green Tripe"
    STICKY_LINING = "Sticky Lining"
    VISCOUS_WEBBING = "Viscous Webbing"
    BRASS_CASE_LIGHTER = "Brass Case Lighter"
    DEER_LUNG = "Deer Lung"
    ELEVENS_SODA = "Eleven's Soda"
    THORNY_VINES = "Thorny Vines"
    VIOLET_WAXCAP = "Violet Waxcap"
    LIFEGUARD_WHISTLE = "Lifeguard Whistle"
    UNKNOWN_EGG = "Unknown Egg"
    UPSIDE_DOWN_RESIN = "Upside Down Resin"
    VERMILION_WEBCAP = "Vermilion Webcap"
    LEPROSE_LICHEN = "Leprose Lichen"
    RED_MOSS = "Red Moss"
    

class DEMOGORGON:

    NAME = "Demogorgon"

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

    ALL_KILLER_ADD_ONS = get_all_add_on_names(DEMOGORGON_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = [
        DEMOGORGON_ADD_ON_NAMES.LEPROSE_LICHEN
    ]

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]