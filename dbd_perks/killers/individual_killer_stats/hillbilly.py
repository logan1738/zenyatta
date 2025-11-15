

from dbd_perks.items import SURVIVOR_ITEM_ADD_ON_NAMES, SURVIVOR_ITEM_NAMES
from dbd_perks.killers.killer_utils import get_all_add_on_names
from dbd_perks.offerings import KILLER_OFFERING_NAMES, SURVIVOR_OFFERING_NAMES


class HILLBILLY_ADD_ON_NAMES:

    COUNTERWEIGHT = "Counterweight"
    CRACKED_PRIMER_BULB = "Cracked Primer Bulb"
    DISCARDED_AIR_FILTER = "Discarded Air Filter"
    STEEL_TOE_BOOTS = "Steel Toe Boots"
    CLOGGED_INTAKE = "Clogged Intake"
    GREASED_THROTTLE = "Greased Throttle"
    HIGH_SPEED_IDLER_SCREW = "High-Speed Idler Screw"
    OFF_BRAND_MOTOR_OIL = "Off-Brand Motor Oil"
    THERMAL_CASTING = "Thermal Casting"
    BEGRIMED_CHAINS = "Begrimed Chains"
    DADS_BOOTS = "Dad's Boots"
    LOW_KICKBACK_CHAINS = "Low Kickback Chains"
    RAGGED_ENGINE = "Ragged Engine"
    THE_THOMPSONS_MIX = "The Thompsons' Mix"
    APEX_MUFFLER = "Apex Muffler"
    FILTHY_SLIPPERS = "Filthy Slippers"
    LOPRO_CHAINS = "LoPro Chains"
    SPIKED_BOOTS = "Spiked Boots"
    IRIDESCENT_ENGRAVINGS = "Iridescent Engravings"
    TUNED_CARBURETTOR = "Tuned Carburettor"



class HILLBILLY:

    NAME = "Hillbilly"

    TIER = 1

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
            'item': SURVIVOR_ITEM_NAMES.RANGER_MED_KIT,
            'add_ons': [
                SURVIVOR_ITEM_ADD_ON_NAMES.GEL_DRESSINGS,
                SURVIVOR_ITEM_ADD_ON_NAMES.BANDAGES
            ]
        },
        {
            'item': SURVIVOR_ITEM_NAMES.TOOLBOX,
            'add_ons': [
                SURVIVOR_ITEM_ADD_ON_NAMES.CLEAN_RAG,
                SURVIVOR_ITEM_ADD_ON_NAMES.SCRAPS,
                SURVIVOR_ITEM_ADD_ON_NAMES.INSTRUCTIONS
            ]
        },
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

    ALL_KILLER_ADD_ONS = get_all_add_on_names(HILLBILLY_ADD_ON_NAMES)

    BANNED_KILLER_ADD_ONS = [
        HILLBILLY_ADD_ON_NAMES.LOPRO_CHAINS
    ]

    KILLER_OFFERINGS = [KILLER_OFFERING_NAMES.CUT_COIN]