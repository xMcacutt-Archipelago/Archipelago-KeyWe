from __future__ import annotations
from typing import Dict, Optional, TYPE_CHECKING

from worlds.keywe.data import *

if TYPE_CHECKING:
    from worlds.keywe import KeyWeWorld

import enum
from typing import Dict

from BaseClasses import CollectionState

def get_rules(world: KeyWeWorld):
    rules = {
        "locations": {

        },
        "entrances": {

        }
    }
    return rules

def create_events(world: KeyWeWorld):
    for week, level, data in iter_levels():
        if level != WINTER_LVL_12:
            world.create_event(level, f"{level} Complete", "Level Complete")
            world.create_event(level, f"{week} {level} Complete", f"{week} Level Complete")
            if data.collectible is not None and world.options.required_collectible_checks > 0:
                world.create_event(level, f"{data.collectible} Event", f"Collectible Collected")
    for season, level_dict in overtime_levels.items():
        for level, data in level_dict.items():
            if world.options.required_overtime_completions:
                world.create_event(level, f"{level} Complete", "Overtime Level Complete")
    for level in tournament_levels:
        if world.options.required_tournament_completions:
            world.create_event(level, f"{level} Complete", "Tournament Level Complete")
    world.create_event(WINTER_LVL_12, "Victory", "Victory")

def set_rules(world: KeyWeWorld):
    rules_lookup = get_rules(world)
    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError:
            pass
    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError:
            pass

    for week_name in levels.keys():
        rule = lambda state, week=week_name: state.has(f"{week} Unlock", world.player)
        world.get_entrance(f"Menu -> {week_name}").access_rule = rule

    if world.options.include_overtime:
        rule = lambda state: state.has(f"{OT_SUMMER} Unlock", world.player)
        world.get_entrance(f"Menu -> {OT_SUMMER}").access_rule = rule
        rule = lambda state: state.has(f"{OT_FALL} Unlock", world.player)
        world.get_entrance(f"Menu -> {OT_FALL}").access_rule = rule
        rule = lambda state: state.has(f"{OT_WINTER} Unlock", world.player)
        world.get_entrance(f"Menu -> {OT_WINTER}").access_rule = rule

    if world.options.include_tournament:
        rule = lambda state: state.has(f"{TPT} Unlock", world.player)
        world.get_entrance(f"Menu -> {TPT}").access_rule = rule

    goal_dict = {}
    goal_dict["Level Complete"] = world.options.required_level_completions.value
    for week_name in levels.keys():
        key = f"{week_name} Level Complete"
        goal_dict[key] = world.options.required_level_completions_per_week.value
        if week_name == "Winter - Week 3":
            goal_dict[key] = min(goal_dict[key], 3)
    goal_dict["Collectible Collected"] = world.options.required_collectible_checks.value
    if world.options.include_overtime:
        goal_dict["Overtime Level Complete"] = world.options.required_overtime_completions
    if world.options.include_tournament:
        goal_dict["Tournament Level Complete"] = world.options.required_tournament_completions

    world.get_entrance(f"{WINTER_WEEK_3} -> {WINTER_LVL_12}").access_rule = \
        lambda state: (state.has_all_counts(goal_dict, world.player) and
                       state.has_from_list_unique(collectibles, world.player, world.options.required_collectibles.value))

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)