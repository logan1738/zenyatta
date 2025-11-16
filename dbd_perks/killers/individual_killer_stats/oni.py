

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES
from dbd_perks.survivor_perk_names import SURVIVOR_PERK_NAMES


class ONI_ADD_ON_NAMES:

    BLACKENED_TOENAIL = "Blackened Toenail"
    CRACKED_SAKAZUKI = "Cracked Sakazuki"
    PAPER_LANTERN = "Paper Lantern"
    ROTTING_ROPE = "Rotting Rope"
    BLOODY_SASH = "Bloody Sash"
    CHILDS_WOODEN_SWORD = "Child's Wooden Sword"
    CHIPPED_SAIHAI = "Chipped Saihai"
    INK_LION = "Ink Lion"
    POLISHED_MAEDATE = "Polished Meadate"
    KANAI_ANZEN_TALISMAN = "Kanai-Anzen Talisman"
    SCALPED_TOPKNOT = "Scalped Topknot"
    SHATTERED_WAKIZASHI = "Shattered Wakizashi"
    WOODEN_ONI_MASK = "Wooden Oni Mask"
    YAMAOKA_SASHIMONO = "Yamaoka Sashimono"
    AKITOS_CRUTCH = "Akito's Crutch"
    LION_FANG = "Lion Fang"
    SPLINTERED_HULL = "Splintered Hull"
    TEAR_SOAKED_TENUGUI = "Tear-Soaked Tenugui"
    IRIDESCENT_FAMILY_CREST = "Iridescent Family Crest"
    RENJIROS_BLOODY_GLOVE = "Renjiro's Bloody Glove"



class ONI:

    NAME = "Oni"

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

    ALL_KILLER_ADD_ONS = get_all_add_on_names(ONI_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = [
        ONI_ADD_ON_NAMES.IRIDESCENT_FAMILY_CREST,
        ONI_ADD_ON_NAMES.RENJIROS_BLOODY_GLOVE
    ]

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]