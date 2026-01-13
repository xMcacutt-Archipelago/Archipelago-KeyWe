from __future__ import annotations
from typing import List, TYPE_CHECKING

from worlds.keywe.data import *

if TYPE_CHECKING:
    from worlds.keywe import KeyWeWorld

from BaseClasses import Region, Entrance

class KeyWeRegion(Region):
    subregions: List[Region] = []

def connect_regions(world: KeyWeWorld, from_name: str, to_name: str, entrance_name: str) -> Entrance:
    entrance_region = world.multiworld.get_region(from_name, world.player)
    exit_region = world.multiworld.get_region(to_name, world.player)
    return entrance_region.connect(exit_region, entrance_name)

def create_region(world: KeyWeWorld, name: str):
    reg = Region(name, world.player, world.multiworld)
    world.multiworld.regions.append(reg)

def create_regions(world: KeyWeWorld):
    create_region(world, "Menu")
    for week, levels_dict in levels.items():
        create_region(world, week)
        for level, data in levels_dict.items():
            create_region(world, level)
    if world.options.include_overtime:
        for season, levels_dict in overtime_levels.items():
            create_region(world, season)
            for level, data in levels_dict.items():
                create_region(world, level)
    if world.options.include_tournament:
        create_region(world, TPT)
        for level in tournament_levels:
            create_region(world, level)

def connect_all_regions(world: KeyWeWorld):
    for week, level_dict in levels.items():
        connect_regions(world,"Menu", week, f"Menu -> {week}")
        for level, data in level_dict.items():
            connect_regions(world, week, level, f"{week} -> {level}")
    if world.options.include_overtime:
        for season, level_dict in overtime_levels.items():
            connect_regions(world, "Menu", season, f"Menu -> {season}")
            for level, data in level_dict.items():
                connect_regions(world, season, level, f"{season} -> {level}")
    if world.options.include_tournament:
        connect_regions(world, "Menu", TPT, f"Menu -> {TPT}")
        for level in tournament_levels:
            connect_regions(world, TPT, level, f"{TPT} -> {level}")