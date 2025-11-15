

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES


class PIG_ADD_ON_NAMES:

    COMBAT_STRAPS = "Combat Straps"
    INTERLOCKING_RAZOR = "Interlocking Razor"
    JOHNS_MEDICAL_FILE = "John's Medical File"
    SHATTERED_SYRINGE = "Shattered Syringe"
    FACE_MASK = "Face Mask"
    LAST_WILL = "Last Will"
    RAZOR_WIRES = "Razor Wires"
    UTILITY_BLADES = "Utility Blades"
    WORKSHOP_GREASE = "Workshop Grease"
    BAG_OF_GEARS = "Bag of Gears"
    JIGSAWS_ANNOTATED_PLAN = "Jigsaw's Annotated Plan"
    RULES_SET_NO_2 = "Rules Set No. 2"
    RUSTY_ATTACHMENTS = "Rusty Attachments"
    SLOW_RELEASE_TOXIN = "Slow-Release Toxin"
    AMANDAS_SECRET = "Amanda's Secret"
    CRATE_OF_GEARS = "Crate of Gears"
    JIGSAWS_SKETCH = "Jigsaw's Sketch"
    TAMPERED_TIMER = "Tampered Timer"
    AMANDAS_LETTER = "Amanda's Letter"
    VIDEO_TAPE = "Video Tape"

class PIG:

    NAME = "Pig"

    TIER = 5

    ALL_SURVIVOR_PERKS_BANNED = False

    BANNED_SURVIVOR_PERKS = []

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

    ALL_KILLER_ADD_ONS = get_all_add_on_names(PIG_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = [
        PIG_ADD_ON_NAMES.AMANDAS_LETTER,
        PIG_ADD_ON_NAMES.BAG_OF_GEARS,
        PIG_ADD_ON_NAMES.CRATE_OF_GEARS,
        PIG_ADD_ON_NAMES.TAMPERED_TIMER,
        PIG_ADD_ON_NAMES.VIDEO_TAPE
    ]

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]