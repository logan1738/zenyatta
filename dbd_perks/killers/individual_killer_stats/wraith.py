

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.offerings import SURVIVOR_OFFERING_NAMES
from dbd_perks.survivor_perk_names import SURVIVOR_PERK_NAMES


class WRAITH_ADD_ON_NAMES:

    THE_BEAST_SOOT = '"The Beast" - Soot'
    THE_GHOST_SOOT = '"The Ghost" - Soot'
    THE_HOUND_SOOT = '"The Hound" - Soot'
    THE_SERPENT_SOOT = '"The Serpent" - Soot'
    BLIND_WARRIOR_MUD = '"Blind Warrior" - Mud'
    BLINK_MUD = '"Blink" - Mud'
    SWIFT_HUNT_MUD = '"Swift Hunt" - Mud'
    WINDSTORM_MUD = '"Windstorm" - Mud'
    BONE_CLAPPER = "Bone Clapper"
    BLIND_WARRIOR_WHITE = '"Blind Warrior" - White'
    BLINK_WHITE = '"Blink" - White'
    SHADOW_DANCE_WHITE = '"Shadow Dance" - White'
    SWIFT_HUNT_WHITE = '"Swift Hunt" - White'
    WINDSTORM_WHITE = '"Windstorm" - White'
    ALL_SEEING_BLOOD = '"All-Seeing" - Blood'
    SHADOW_DANCE_BLOOD = '"Shadow Dance" - Blood'
    SWIFT_HUNT_BLOOD = '"Swift Hunt" - Blood'
    WINDSTORM_BLOOD = '"Windstorm" - Blood'
    ALL_SEEING_SPIRIT = '"All-Seeing" - Spirit'
    COXCOMBED_CLAPPER = "Coxcombed Clapper"

class WRAITH:


    NAME = "Wraith"

    TIER = 5

    ALL_SURVIVOR_PERKS_BANNED = False

    BANNED_SURVIVOR_PERKS = [
        SURVIVOR_PERK_NAMES.BREAKOUT,
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

    ALL_KILLER_ADD_ONS = []

    BANNED_KILLER_ADD_ONS = []

    KILLER_OFFERINGS = []