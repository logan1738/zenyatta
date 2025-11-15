

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.offerings import SURVIVOR_OFFERING_NAMES
from dbd_perks.survivor_perk_names import SURVIVOR_PERK_NAMES


class HUNTRESS_ADD_ON_NAMES:

    AMANITA_TOXIN = "Amanita Toxin"
    BANDAGED_HAFT = "Bandaged Haft"
    COARSE_STONE = "Coarse Stone"
    YELLOWED_CLOTH = "Yellowed Cloth"
    LEATHER_LOOP = "Leather Loop"
    MANNA_GRASS_BRAID = "Manna Grass Braid"
    OAK_HAFT = "Oak Haft"
    SHINY_PIN = "Shiny Pin"
    WEIGHTED_HEAD = "Weighted Head"
    DEERSKIN_GLOVES = "Deerskin Gloves"
    FLOWER_BABUSHKA = "Flower Babushka"
    ROSE_ROOT = "Rose Root"
    RUSTY_HEAD = "Rusty Head"
    VENOMOUS_CONCOCTION = "Venomous Concoction"
    BEGRIMED_HEAD = "Begrimed Head"
    GLOWING_CONCOCTION = "Glowing Concoction"
    INFANTRY_BELT = "Infantry Belt"
    WOODEN_FOX = "Wooden Fox"
    IRIDESCENT_HEAD = "Iridescent Head"
    SOLDIERS_PUTTEE = "Soldier's Puttee"

class HUNTRESS:

    NAME = "Huntress"

    TIER = 3

    ALL_SURVIVOR_PERKS_BANNED = False

    BANNED_SURVIVOR_PERKS = [
        SURVIVOR_PERK_NAMES.SPRINT_BURST
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

    ALL_KILLER_ADD_ONS = []

    BANNED_KILLER_ADD_ONS = []

    KILLER_OFFERINGS = []