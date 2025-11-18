from __future__ import annotations

from enum import EnumType, Enum
from typing import TYPE_CHECKING, NamedTuple, Any

if TYPE_CHECKING:
    from worlds.keywe import KeyWeWorld

from BaseClasses import Location, Region, LocationProgressType
from worlds.keywe.options import KeyWeOptions
from worlds.keywe.data import *

class KeyWeLocation(Location):
    game: str = "KeyWe"

class LocData:
    def __init__(self, name: str, code: int, region: str, loc_type: LocType):
        self.code = code
        self.name = name
        self.region = region
        self.loc_type = loc_type

class LocType(Enum):
    COMPLETION    = 1
    OBJECTIVE     = 2
    COLLECTIBLE   = 3
    CHALLENGE     = 4
    OT_ITEM       = 5


def create_location(world: KeyWeWorld, reg: Region, name: str, code: int):
    location = KeyWeLocation(world.player, name, code, reg)
    reg.locations.append(location)

def create_locations(world: KeyWeWorld):
    for name, loc_data in location_table.items():
        if not world.options.include_tournament and loc_data.region in tournament_levels:
            continue
        if not world.options.include_overtime and loc_data.region in overtime_level_names:
            continue
        if not world.options.challengesanity.value and loc_data.loc_type == LocType.CHALLENGE:
            continue
        create_location(world, world.get_region(loc_data.region), name, loc_data.code)

def add_location(loc_dict: dict[str, LocData], loc_id: int, loc_name: str, region: str, loc_type: LocType):
    loc_dict[loc_name] = LocData(loc_name, loc_id, region, loc_type)
    # print(f"Adding Location Here: Name: {loc_name} ID: {hex(loc_id)} Region: {region}")

def generate_location_table() -> dict[str, LocData]:
    loc_dict: dict[str, LocData] = {}

    # Story
    # Location ids for each level:
    # 0x0        - level completion
    # 0x1 -> 0x8 - level objective checks
    # 0xA        - collectible
    # 0xB        - challenge
    loc_id = 0x100
    for week, level, data in iter_levels():
        base_loc_id = loc_id
        if level != WINTER_LVL_12:
            add_location(loc_dict, loc_id, level, level, LocType.COMPLETION)
            loc_id = base_loc_id + 0x1
            for objective_index in range(data.objective_count):
                add_location(loc_dict, loc_id, f"{level} - {data.level_type} {objective_index + 1}", level, LocType.OBJECTIVE)
                loc_id += 0x1
        loc_id = base_loc_id + 0xA
        if data.collectible is not None:
            add_location(loc_dict, loc_id, data.collectible, level, LocType.COLLECTIBLE)
        loc_id = base_loc_id + 0xB
        if data.has_challenge:
            add_location(loc_dict, loc_id, f"{level} - Challenge", level, LocType.CHALLENGE)
        loc_id = base_loc_id + 0x10

    # Overtime Shifts
    # Location ids for each overtime level:
    # 0x0        - level completion
    # 0x1        - item unlock
    # 0x2        - challenge
    # 0x3        - padding
    loc_id = 0x400
    for season, level_dict in overtime_levels.items():
        for level, data in level_dict.items():
            base_loc_id = loc_id
            add_location(loc_dict, loc_id, level, level, LocType.COMPLETION)
            loc_id = base_loc_id + 0x1
            add_location(loc_dict, loc_id, f"{level} - Item", level, LocType.OT_ITEM)
            loc_id = base_loc_id + 0x2
            if data.has_challenge:
                add_location(loc_dict, loc_id, f"{level} - Challenge", level, LocType.CHALLENGE)
            loc_id = base_loc_id + 0x4

    # Telepost Tournament
    # Location ids for each overtime level:
    # 0x0        - level completion
    # 0x1        - challenge 1
    # 0x2        - challenge 2
    # 0x3        - challenge 3
    loc_id = 0x500
    for level in tournament_levels:
        base_loc_id = loc_id
        add_location(loc_dict, loc_id, level, level, LocType.COMPLETION)
        loc_id = base_loc_id + 0x1
        add_location(loc_dict, loc_id, f"{level} - Herbert", level, LocType.CHALLENGE)
        loc_id = base_loc_id + 0x2
        add_location(loc_dict, loc_id, f"{level} - Mailflies", level, LocType.CHALLENGE)
        loc_id = base_loc_id + 0x3
        add_location(loc_dict, loc_id, f"{level} - Extra Obstacles", level, LocType.CHALLENGE)
        loc_id = base_loc_id + 0x4

    return loc_dict

location_table: dict[str, LocData] = generate_location_table()

