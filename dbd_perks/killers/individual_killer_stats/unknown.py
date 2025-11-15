

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.offerings import SURVIVOR_OFFERING_NAMES
from dbd_perks.survivor_perk_names import SURVIVOR_PERK_NAMES


class UNKNOWN_ADD_ON_NAMES:

    BLURRY_PHOTO = "Blurry Photo"
    PUNCTURED_EYEBALL = "Punctured Eyeball"
    RABBITS_FOOT = "Rabbit's Foot"
    SKETCH_ATTEMPT = "Sketch Attempt"
    DEVICE_OF_UNDISCLOSED_ORIGIN = "Device of Undisclosed Origin"
    LAST_KNOWN_RECORDING = "Last Known Recording"
    NOTEBOOK_OF_THEORIES = "Notebook of Theories"
    SLASHED_BACKPACK = "Slashed Backpack"
    VICTIMS_MAP = "Victim's Map"
    B_MOVIE_POSTER = "B-Movie Poster"
    FOOTPRINT_CAST = "Footprint Cast"
    FRONT_PAGE_ARTICLE = "Front Page Article"
    HYPNOTISTS_WATCH = "Hypnotist's Watch"
    VANISHING_BOX = "Vanishing Box"
    DISCARDED_MILK_CARTON = "Discarded Milk Carton"
    HOMEMADE_MASK = "Homemade Mask"
    OBSCURE_GAME_CARTRIDGE = "Obscure Game Cartridge"
    SERUM_VIAL = "Serum Vial"
    CAPTURED_BY_THE_DARK = "Captured by the Dark"
    IRIDESCENT_OSS_REPORT = "Iridescent OSS Report"

class UNKNOWN:

    NAME = "Unknown"

    TIER = 3

    ALL_SURVIVOR_PERKS_BANNED = False

    BANNED_SURVIVOR_PERKS = [
        SURVIVOR_PERK_NAMES.SPRINT_BURST,
    ]

    BANNED_SURVIVOR_PERK_COMBOS = []

    SURVIVOR_OFFERINGS = {
        'offering1': [SURVIVOR_OFFERING_NAMES.SHROUD_OF_BINDING],
        'offering2': [SURVIVOR_OFFERING_NAMES.VIGOS_SHROUD],
        'offering3': [SURVIVOR_OFFERING_NAMES.ANNOTATED_BLUEPRINT],
        'offering4': [SURVIVOR_OFFERING_NAMES.BLOODIED_BLUEPRINT, SURVIVOR_OFFERING_NAMES.TORN_BLUEPRINT],
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