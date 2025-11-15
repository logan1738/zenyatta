

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES


class LEGION_ADD_ON_NAMES:

    FRIENDSHIP_BRACELET = "Friendship Bracelet"
    MISCHIEF_LIST = "Mischief List"
    SCRATCHED_RULER = "Scratched Ruler"
    SMILEY_FACE_PIN = "Smiley Face Pin"
    DEFACED_SMILEY_PIN = "Defaced Smiley Pin"
    ETCHED_RULER = "Etched Ruler"
    JULIES_MIX_TAPE = "Julie's Mix Tape"
    MURAL_SKETCH = "Mural Sketch"
    NEVER_SLEEP_PILLS = "Never-Sleep Pills"
    JOEYS_MIX_TAPE = "Joey's Mix Tape"
    STOLEN_SKETCH_BOOK = "Stolen Sketch Book"
    STYLISH_SUNGLASSES = "Stylish Sunglasses"
    SUSIES_MIX_TAPE = "Susie's Mix Tape"
    THE_LEGION_PIN = "The Legion Pin"
    BFFS = "BFFs"
    FILTHY_BLADE = "Filthy Blade"
    FRANKS_MIX_TAPE = "Frank's Mix Tape"
    STAB_WOUNDS_STUDY = "Stab Wounds Study"
    FUMING_MIX_TAPE = "Fuming Mix Tape"
    IRIDESCENT_BUTTON = "Iridescent Button"

class LEGION:

    NAME = "Legion"

    TIER = 4

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

    ALL_KILLER_ADD_ONS = get_all_add_on_names(LEGION_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = []

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]