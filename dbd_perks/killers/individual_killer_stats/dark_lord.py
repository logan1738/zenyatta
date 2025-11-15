

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES



class DARK_LORD_ADD_ON_NAMES:

    CERBERUS_TALON = "Cerberus Talon"
    CLOCK_TOWER_GEAR = "Clock Tower Gear"
    RUBY_CIRCLET = "Ruby Circlet"
    TRAVELLERS_HAT = "Traveller's Hat"
    BLOOD_FILLED_GOBLET = "Blood-Filled Goblet"
    MAGICAL_TICKET = "Magical Ticket"
    MOONSTONE_NECKLACE = "Moonstone Necklace"
    WHITE_WOLF_MEDALLION = "White Wolf Medallion"
    WINGED_BOOTS = "Winged Boots"
    FORCE_OF_ECHO = "Force of Echo"
    KILLER_DOLL = "Killer Doll"
    POCKET_WATCH = "Pocket Watch"
    SUNGLASSES = "Sunglasses"
    SYLPH_FEATHER = "Sylph Feather"
    CUBE_OF_ZOE = "Cube of Zoe"
    LAPIS_LAZULI = "Lapis Lazuli"
    MEDUSAS_HAIR = "Medusa's Hair"
    WARGS_FANG = "Warg's Fang"
    ALUCARDS_SHIELD = "Alucard's Shield"
    IRIDESCENT_RING_OF_VLAD = "Iridescent Ring of Vlad"



class DARK_LORD:

    NAME = "Dark Lord"

    TIER = 2

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

    ALL_KILLER_ADD_ONS = get_all_add_on_names(DARK_LORD_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = [
        DARK_LORD_ADD_ON_NAMES.IRIDESCENT_RING_OF_VLAD,
        DARK_LORD_ADD_ON_NAMES.MEDUSAS_HAIR,
        DARK_LORD_ADD_ON_NAMES.WARGS_FANG
    ]

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]