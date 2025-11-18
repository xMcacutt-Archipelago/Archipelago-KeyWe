from dataclasses import dataclass

@dataclass
class KeyWeLevelData:
    """
    Holds Data on KeyWe Levels.
    level_type goal_count collectible_name has_challenge
    """
    level_type: str
    objective_count: int
    has_challenge: bool = False
    collectible: str = None

@dataclass
class KeyWeOvertimeLevelData:
    has_challenge: bool = False


SUMMER_WEEK_1 = "Summer - Week 1"
SUMMER_WEEK_2 = "Summer - Week 2"
SUMMER_WEEK_3 = "Summer - Week 3"
FALL_WEEK_1 = "Fall - Week 1"
FALL_WEEK_2 = "Fall - Week 2"
FALL_WEEK_3 = "Fall - Week 3"
WINTER_WEEK_1 = "Winter - Week 1"
WINTER_WEEK_2 = "Winter - Week 2"
WINTER_WEEK_3 = "Winter - Week 3"

OT_SUMMER = "Overtime - Summer"
OT_FALL = "Overtime - Fall"
OT_WINTER = "Overtime - Winter"

SUMMER_LVL_1 = "The Telegraph Desk"
SUMMER_LVL_2 = "The Transcription Room"
SUMMER_LVL_3 = "The Shipping Floor"
SUMMER_LVL_4 = "The Dropoff Depot"
SUMMER_LVL_5 = "Marauding Mailflies"
SUMMER_LVL_6 = "Covert Decoders"
SUMMER_LVL_7 = "Postal Pest Problems"
SUMMER_LVL_8 = "Vegetation Vexation"
SUMMER_LVL_9 = "Devilish Dust-Up"
SUMMER_LVL_10 = "A Sinking Feeling"
SUMMER_LVL_11 = "Bouncing Boxes (and Blimps)"
SUMMER_LVL_12 = "Creepin' Kudzu"

SUMMER_OT_1 = "Kiwis In Harmony"
SUMMER_OT_2 = "Conveyor Belt Chaos"
SUMMER_OT_3 = "Lunch Break"

FALL_LVL_1 = "Shipping Shake-Up"
FALL_LVL_2 = "Transcription Turmoil"
FALL_LVL_3 = "Keyboard Commotion"
FALL_LVL_4 = "Parcel Panel Puzzle"
FALL_LVL_5 = "The Night Post"
FALL_LVL_6 = "Electrical Interference"
FALL_LVL_7 = "Bobbing for Boxes"
FALL_LVL_8 = "Mechanical Mayhem"
FALL_LVL_9 = "Tricks and Telegrams"
FALL_LVL_10 = "Zoey's Tracks of Terror"
FALL_LVL_11 = "Casso-scary"
FALL_LVL_12 = "Mail from Beyond"

FALL_OT_1 = "Tank Trouble"
FALL_OT_2 = "Cassowary Courier Course"
FALL_OT_3 = "Bubble Wrap Testing"

WINTER_LVL_1 = "Trapdoors and Tentacles"
WINTER_LVL_2 = "Assembly-Line Scramble"
WINTER_LVL_3 = "Dueling Crates"
WINTER_LVL_4 = "Switchboard Syncrhony"
WINTER_LVL_5 = "Bungalow Basin Bake-Off"
WINTER_LVL_6 = "Parts and Crafts"
WINTER_LVL_7 = "The Hollyjostle Tinkertrack"
WINTER_LVL_8 = "That's a Wrap"
WINTER_LVL_9 = "An Approaching Storm"
WINTER_LVL_10 = "Bitter Cold"
WINTER_LVL_11 = "Emergency Relief"
WINTER_LVL_12 = "Stand Your Post"

WINTER_OT_1 = "Snowball Fight!"
WINTER_OT_2 = "The Sorting Room"
WINTER_OT_3 = "Cashing Out"

TPT_GROVE = "Gumtree Grove"
TPT_CLIFFS = "Painted Cliffs"
TPT_LAKE = "Lake Bessy"

MSG = "Message"
LTR = "Letter"
PKG = "Package"
SRT = "Sort"
OVT = "Overtime"
TPT = "Telepost Tournament"

#Collectibles
SECRET_SPICE_SHAKER = "Secret Spice Shaker"
GLIMMERING_SHELL = "Glimmering Shell"
EMPTY_CHRYSALIS = "Empty Chrysalis"
TEMPERED_LENS = "Tempered Lens"
WAYFARERS_COMPASS = "Wayfarer's Compass"
PRICKLY_SEED_POD = "Prickly Seed Pod"
ANCIENT_TOOTH = "Ancient Tooth"
COSMIC_FRIENDSHIP_ROCK = "Cosmic Friendship Rock"
CHARGED_FEATHER = "Charged Feather"
SALTY_SCALE = "Salty Scale"
GLOWING_WISHBONE = "Glowing Wishbone"
Z39_SOARING_AUK = "Z39 Soaring Auk"
PAPA_MOON_FIGURINE = "Papa Moon Figurine"
MOUNTAINEERS_PITON = "Mountaineers Piton"
LOST_LETTER = "Lost Letter"

levels = {
    SUMMER_WEEK_1: {
        SUMMER_LVL_1: KeyWeLevelData(MSG, 3),
        SUMMER_LVL_2: KeyWeLevelData(LTR, 3, has_challenge=True, collectible=SECRET_SPICE_SHAKER),
        SUMMER_LVL_3: KeyWeLevelData(PKG, 3),
        SUMMER_LVL_4: KeyWeLevelData(SRT, 3, collectible=GLIMMERING_SHELL)
    },
    SUMMER_WEEK_2: {
        SUMMER_LVL_5: KeyWeLevelData(LTR, 3, has_challenge=True, collectible=EMPTY_CHRYSALIS),
        SUMMER_LVL_6: KeyWeLevelData(MSG, 3, collectible=TEMPERED_LENS),
        SUMMER_LVL_7: KeyWeLevelData(PKG, 3),
        SUMMER_LVL_8: KeyWeLevelData(SRT, 3),
    },
    SUMMER_WEEK_3: {
        SUMMER_LVL_9: KeyWeLevelData(LTR, 3),
        SUMMER_LVL_10: KeyWeLevelData(PKG, 3, has_challenge=True, collectible=WAYFARERS_COMPASS),
        SUMMER_LVL_11: KeyWeLevelData(SRT, 3),
        SUMMER_LVL_12: KeyWeLevelData(MSG, 3, collectible=PRICKLY_SEED_POD),
    },
    FALL_WEEK_1: {
        FALL_LVL_1: KeyWeLevelData(PKG, 4, collectible=ANCIENT_TOOTH),
        FALL_LVL_2: KeyWeLevelData(LTR, 4),
        FALL_LVL_3: KeyWeLevelData(MSG, 4),
        FALL_LVL_4: KeyWeLevelData(SRT, 3),
    },
    FALL_WEEK_2:{
        FALL_LVL_5: KeyWeLevelData(LTR, 4, collectible=COSMIC_FRIENDSHIP_ROCK),
        FALL_LVL_6: KeyWeLevelData(MSG, 4, collectible=CHARGED_FEATHER),
        FALL_LVL_7: KeyWeLevelData(SRT, 3, collectible=SALTY_SCALE),
        FALL_LVL_8: KeyWeLevelData(PKG, 4),
    },
    FALL_WEEK_3: {
        FALL_LVL_9: KeyWeLevelData(MSG, 3, has_challenge=True),
        FALL_LVL_10: KeyWeLevelData(SRT, 6),
        FALL_LVL_11: KeyWeLevelData(LTR, 4, has_challenge=True),
        FALL_LVL_12: KeyWeLevelData(PKG, 4, has_challenge=True, collectible=GLOWING_WISHBONE),
    },
    WINTER_WEEK_1: {
        WINTER_LVL_1: KeyWeLevelData(SRT, 3),
        WINTER_LVL_2: KeyWeLevelData(LTR, 4),
        WINTER_LVL_3: KeyWeLevelData(PKG, 6, has_challenge=True, collectible=Z39_SOARING_AUK),
        WINTER_LVL_4: KeyWeLevelData(MSG, 4),
    },
    WINTER_WEEK_2: {
        WINTER_LVL_5: KeyWeLevelData(LTR, 4),
        WINTER_LVL_6: KeyWeLevelData(PKG, 4),
        WINTER_LVL_7: KeyWeLevelData(MSG, 4, has_challenge=True, collectible=PAPA_MOON_FIGURINE),
        WINTER_LVL_8: KeyWeLevelData(SRT, 3),
    },
    WINTER_WEEK_3: {
        WINTER_LVL_9: KeyWeLevelData(MSG, 4),
        WINTER_LVL_10: KeyWeLevelData(LTR, 4, has_challenge=True, collectible=MOUNTAINEERS_PITON),
        WINTER_LVL_11: KeyWeLevelData(PKG, 6),
        WINTER_LVL_12: KeyWeLevelData(SRT, 1, collectible=LOST_LETTER),
    }
}

overtime_levels = {
    OT_SUMMER: {
        SUMMER_OT_1: KeyWeOvertimeLevelData(),
        SUMMER_OT_2: KeyWeOvertimeLevelData(),
        SUMMER_OT_3: KeyWeOvertimeLevelData(has_challenge=True),
    },
    OT_FALL: {
        FALL_OT_1: KeyWeOvertimeLevelData(),
        FALL_OT_2: KeyWeOvertimeLevelData(),
        FALL_OT_3: KeyWeOvertimeLevelData(has_challenge=True),
    },
    OT_WINTER: {
        WINTER_OT_1: KeyWeOvertimeLevelData(has_challenge=True),
        WINTER_OT_2: KeyWeOvertimeLevelData(),
        WINTER_OT_3: KeyWeOvertimeLevelData(),
    },
}

overtime_level_names = [
    SUMMER_OT_1, SUMMER_OT_2, SUMMER_OT_3,
    FALL_OT_1, FALL_OT_2, FALL_OT_3,
    WINTER_OT_1, WINTER_OT_2, WINTER_OT_3
]

tournament_levels = [ TPT_GROVE, TPT_CLIFFS, TPT_LAKE ]

weeks = [
    SUMMER_WEEK_1,
    SUMMER_WEEK_2,
    SUMMER_WEEK_3,
    FALL_WEEK_1,
    FALL_WEEK_2,
    FALL_WEEK_3,
    WINTER_WEEK_1,
    WINTER_WEEK_2,
    WINTER_WEEK_3,
]


collectibles = [
    SECRET_SPICE_SHAKER,
    GLIMMERING_SHELL,
    EMPTY_CHRYSALIS,
    TEMPERED_LENS,
    WAYFARERS_COMPASS,
    PRICKLY_SEED_POD,
    ANCIENT_TOOTH,
    COSMIC_FRIENDSHIP_ROCK,
    CHARGED_FEATHER,
    SALTY_SCALE,
    GLOWING_WISHBONE,
    Z39_SOARING_AUK,
    PAPA_MOON_FIGURINE,
    MOUNTAINEERS_PITON,
    LOST_LETTER,
]

def iter_levels():
    for week_name, level_dict in levels.items():
        for level_name, level_data in level_dict.items():
            yield week_name, level_name, level_data
