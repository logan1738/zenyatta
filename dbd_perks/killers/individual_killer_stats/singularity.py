

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES


class SINGULARITY_ADD_ON_NAMES:

    BROKEN_SECURITY_KEY = "Broken Security Key"
    DIAGNOSTIC_TOOL_REPAIR = "Diagnostic Tool (Repair)"
    HEAVY_WATER = "Heavy Water"
    NUTRITIONAL_SLURRY = "Nutritional Slurry"
    ANDROID_ARM = "Android Arm"
    CREMATED_REMAINS = "Cremated Remains"
    CRYO_GEL = "Cryo Gel"
    KIDS_BALL_GLOVE = "Kid's Ball Glove"
    ULTRASONIC_SENSOR = "Ultrasonic Sensor"
    HOLOGRAM_GENERATOR = "Hologram Generator"
    HYPERWARENESS_SPRAY = "Hyperawareness Spray"
    LIVE_WIRES = "Live Wires"
    NANOMACHINE_GEL = "Nanomachine Gel"
    SPENT_OXYGEN_TANK = "Spent Oxygen Tank"
    CREW_MANIFEST = "Crew Manifest"
    DIAGNOSTIC_TOOL_CONSTRUCTION = "Diagnostic Tool (Construction)"
    FOREIGN_PLANT_FIBERS = "Foreign Plant Fibers"
    SOMA_FAMILY_PHOTO = "Soma Family Photo"
    DENIED_REQUISITION_FORM = "Denied Requisition Form"
    IRIDESCENT_CRYSTAL_SHARD = "Iridescent Crystal Shard"


class SINGULARITY:

    NAME = "Singularity"

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

    ALL_KILLER_ADD_ONS = get_all_add_on_names(SINGULARITY_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = [
        SINGULARITY_ADD_ON_NAMES.CREW_MANIFEST,
        SINGULARITY_ADD_ON_NAMES.DENIED_REQUISITION_FORM,
        SINGULARITY_ADD_ON_NAMES.DIAGNOSTIC_TOOL_CONSTRUCTION,
        SINGULARITY_ADD_ON_NAMES.IRIDESCENT_CRYSTAL_SHARD,
        SINGULARITY_ADD_ON_NAMES.SPENT_OXYGEN_TANK
    ]

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]