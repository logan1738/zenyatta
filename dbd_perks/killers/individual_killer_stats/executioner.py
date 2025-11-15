

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES
from dbd_perks.survivor_perk_names import SURVIVOR_PERK_NAMES

class EXECUTIONER_ADD_ON_NAMES:

    BLACK_STRAP = "Black Strap"
    COPPER_RING = "Copper Ring"
    DEAD_BUTTERFLY = "Dead Butterfly"
    LEAD_RING = "Lead Ring"
    CINDERELLA_MUSIC_BOX = "Cinderella Music Box"
    FORGOTTEN_VIDEOTAPE = "Forgotten Videotape"
    LEOPARD_PRINT_FABRIC = "Leopard-Print Fabric"
    SPEARHEAD = "Spearhead"
    WAX_DOLL = "Wax Doll"
    BURNING_MAN_PAINTING = "Burning Man Painting"
    MANNEQUIN_FOOT = "Mannequin Foot"
    MISTY_DAY_REMAINS_OF_JUDGEMENT = "Misty Day, Remains of Judgment"
    TABLET_OF_THE_OPPRESSOR = "Tablet of the Oppressor"
    VALTIEL_SECT_PHOTOGRAPH = "Valtiel Sect Photograph"
    CRIMSON_CEREMONY_BOOK = "Crimson Ceremony Book"
    RUST_COLOURED_EGG = "Rust-Coloured Egg"
    SCARLET_EGG = "Scarlet Egg"
    IRIDESCENT_SEAL_OF_METATRON = "Iridescent Seal of Metatron"
    OBSIDIAN_GOBLET = "Obsidian Goblet"

class EXECUTIONER:

    NAME = "Executioner"

    TIER = 3

    ALL_SURVIVOR_PERKS_BANNED = False

    BANNED_SURVIVOR_PERKS = [
        SURVIVOR_PERK_NAMES.LITHE,
    ]

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

    ALL_KILLER_ADD_ONS = get_all_add_on_names(EXECUTIONER_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = [
        EXECUTIONER_ADD_ON_NAMES.BLACK_STRAP,
        EXECUTIONER_ADD_ON_NAMES.BURNING_MAN_PAINTING,
        EXECUTIONER_ADD_ON_NAMES.MANNEQUIN_FOOT,
        EXECUTIONER_ADD_ON_NAMES.MISTY_DAY_REMAINS_OF_JUDGEMENT,
        EXECUTIONER_ADD_ON_NAMES.OBSIDIAN_GOBLET
    ]

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]