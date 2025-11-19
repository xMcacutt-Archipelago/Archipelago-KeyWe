import dataclasses
from typing import List, Dict, Optional, Any
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region, Location
from Options import OptionError, PerGameCommonOptions
from worlds.AutoWorld import WebWorld, World

from .items import KeyWeItem, keywe_item_table, create_items, ItemData
from .locations import KeyWeLocation, generate_location_table, location_table, create_locations, LocType
from .options import KeyWeOptions, keywe_options
from .regions import create_regions, connect_regions, connect_all_regions
from .rules import set_rules, create_events

class KeyWeWeb(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the KeyWe randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["xMcacutt"]
    )

    tutorials = [setup_en]
    option_groups = keywe_options


class KeyWeWorld(World):
    """
    KeyWe is a co-op puzzle game where the players control Jeff and Debra,
    two Kiwis tasked with manning the stations at a post office.
    """
    game = "KeyWe"
    options_dataclass = KeyWeOptions
    options: KeyWeOptions
    topology_present = True
    item_name_to_id = {name: item.code for name, item in keywe_item_table.items()}
    location_name_to_id ={name: loc_data.code for name, loc_data in location_table.items()}
    trap_weights = {}
    web = KeyWeWeb()
    # ut_can_gen_without_yaml = True

    def __init__(self, multiworld: MultiWorld, player: int):
        self.active_shop_tabs = []
        super().__init__(multiworld, player)

        self.itempool = []


    def fill_slot_data(self) -> id:
        from Utils import visualize_regions
        state = self.multiworld.get_all_state(False)
        state.update_reachable_regions(self.player)
        visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml",
                          show_entrance_names=True, regions_to_highlight=state.reachable_regions[self.player])
        return {
            "ModVersion": "1.0.1",
            "TournamentIncluded": self.options.include_tournament.value,
            "OvertimeIncluded": self.options.include_overtime.value,
            "RequiredLevelCompletions": self.options.required_level_completions.value,
            "RequiredLevelCompletionsPerWeek": self.options.required_level_completions_per_week.value,
            "RequiredCollectibles": self.options.required_collectibles.value,
            "RequiredCollectibleChecks": self.options.required_collectible_checks.value,
            "RequiredOvertimeCompletions": self.options.required_overtime_completions.value,
            "RequiredTournamentCompletions": self.options.required_tournament_completions.value,
            "StartingWeek": self.options.starting_week.value,
            "LevelCompletionCheckThreshold": self.options.level_completion_check_threshold.value,
            "DeathLink": self.options.death_link.value
        }


    def generate_early(self) -> None:
        # UT Stuff Here
        #self.handle_ut_yamless(None)
        if not self.options.include_overtime.value and self.options.required_overtime_completions.value > 0:
            print("[KeyWe] Overtime completions required was set without overtime included. Setting requirements to 0.")
            self.options.required_overtime_completions.value = 0
        if not self.options.include_tournament.value and self.options.required_tournament_completions.value > 0:
            print("[KeyWe] Tournament completions required was set without tournament included. Setting requirements to 0.")
            self.options.required_tournament_completions.value = 0
        pass


    def create_item(self, name: str) -> Item:
        item_info = keywe_item_table[name]
        return KeyWeItem(name, item_info.classification, item_info.code, self.player)

    def create_items(self):
        create_items(self)

    def create_event(self, region_name: str, event_loc_name: str, event_item_name: str) -> None:
        region: Region = self.multiworld.get_region(region_name, self.player)
        loc: KeyWeLocation = KeyWeLocation(self.player, event_loc_name, None, region)
        loc.place_locked_item(KeyWeItem(event_item_name, ItemClassification.progression, None, self.player))
        region.locations.append(loc)

    def create_regions(self):
        create_regions(self)
        create_locations(self)
        create_events(self)
        connect_all_regions(self)

    def set_rules(self):
        set_rules(self)

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        new_hint_data = {}
        for key, data in location_table.items():
            try:
                location: Location = self.multiworld.get_location(key, self.player)
            except KeyError:
                continue
            if data.loc_type is LocType.COLLECTIBLE or data.loc_type is LocType.CHALLENGE:
                new_hint_data[location.address] = f"{data.region} in {location.parent_region.entrances[0].parent_region.name}"
            if data.loc_type is LocType.COMPLETION or data.loc_type is LocType.OBJECTIVE:
                new_hint_data[location.address] = location.parent_region.entrances[0].parent_region.name
        hint_data[self.player] = new_hint_data

    # def handle_ut_yamless(self, slot_data: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    #
    #     if not slot_data \
    #             and hasattr(self.multiworld, "re_gen_passthrough") \
    #             and isinstance(self.multiworld.re_gen_passthrough, dict) \
    #             and self.game in self.multiworld.re_gen_passthrough:
    #         slot_data = self.multiworld.re_gen_passthrough[self.game]
    #
    #     if not slot_data:
    #         return None
    #
    #     # fill in options
    #     self.options.goal.value = slot_data["Goal"]
    #     self.options.progressive_elementals.value = slot_data["ProgressiveElementals"]
    #
    #     return slot_data