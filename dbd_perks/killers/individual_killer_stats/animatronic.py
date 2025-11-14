



from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES
from dbd_perks.survivor_perk_names import SURVIVOR_PERK_NAMES


class ANIMATRONIC_ADD_ON_NAMES:

    GREASY_PAPER_PLATE = "Greasy Paper Plate"
    HELP_WANTED_AD = "Help Wanted Ad"
    RESTAURANT_MENU = "Restaurant Menu"
    ROTTEN_PIZZA = "Rotten Pizza"
    OFFICE_PHONE = "Office Phone"
    PARTY_HAT = "Party Hat"
    RIPPED_CURTAIN = "Ripped Curtain"
    SECRUITY_GUARDS_BADGE = "Security Guard's Badge"
    STREAMERS = "Streamers"
    BONNIES_GUITAR_STRINGS = "Bonnie's Guitar Strings"
    CHICAS_BIB = "Chica's Bib"
    FOXYS_HOOK = "Foxy's Hook"
    FREDDY_HAT = "Freddy's Hat"
    PURPLE_GUY_DRAWING = "Purple Guy Drawing"
    ACCESS_PANEL = "Access Panel"
    CELEBRATE_POSTER = "Celebrate! Poster"
    ENDO_CPU = "Endo CPU"
    LOOT_BAG = "Loot Bag"
    FAZ_COIN = "Faz-Coin"
    IRIDESCENT_REMNANT = "Iridescent Remnant"



class ANIMATRONIC:

    NAME = "Animatronic"

    TIER = 3

    ALL_SURVIVOR_PERKS_BANNED = False

    BANNED_SURVIVOR_PERKS = [
        SURVIVOR_PERK_NAMES.BREAKOUT,
        SURVIVOR_PERK_NAMES.SPRINT_BURST,
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

    ALL_KILLER_ADD_ONS = get_all_add_on_names(ANIMATRONIC_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = [
        ANIMATRONIC_ADD_ON_NAMES.BONNIES_GUITAR_STRINGS,
        ANIMATRONIC_ADD_ON_NAMES.IRIDESCENT_REMNANT,
        ANIMATRONIC_ADD_ON_NAMES.PURPLE_GUY_DRAWING
    ]

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]