from __future__ import annotations
from typing import Dict, Optional, TYPE_CHECKING

from worlds.keywe.data import *

if TYPE_CHECKING:
    from worlds.keywe import KeyWeWorld

from BaseClasses import Item, ItemClassification

class KeyWeItem(Item):
    game: str = "KeyWe"


def get_junk_item_names(rand, k: int, weights) -> str:
    items = rand.choices(
        list(weights.keys()),
        weights=list(weights.values()),
        k=k)
    return items


def create_single(name: str, world: KeyWeWorld, item_class: ItemClassification = None) -> None:
    classification = keywe_item_table[name].classification if item_class is None else item_class
    world.itempool.append(KeyWeItem(name, classification, keywe_item_table[name].code, world.player))


def create_multiple(name: str, amount: int, world: KeyWeWorld, item_class: ItemClassification = None):
    for i in range(amount):
        create_single(name, world, item_class)


def create_items(world: KeyWeWorld):
    total_location_count: int = len(world.multiworld.get_unfilled_locations(world.player))

    for i in range(9):
        if world.options.starting_week.value != i + 1:
            create_single(f"{weeks[i]} Unlock", world)
        else:
            world.multiworld.push_precollected (
                KeyWeItem (
                    f"{weeks[i]} Unlock",
                    ItemClassification.progression,
                    keywe_item_table[f"{weeks[i]} Unlock"].code,
                    world.player
                )
            )

    if world.options.include_overtime:
        create_single(f"{OT_SUMMER} Unlock", world)
        create_single(f"{OT_FALL} Unlock", world)
        create_single(f"{OT_WINTER} Unlock", world)

    create_multiple("Dash+", 5, world)
    create_multiple("Movement+", 5, world)
    create_multiple("Swim+", 5, world)
    create_multiple("Jump+", 5, world)
    create_multiple("Respawn+", 5, world)
    create_multiple("Chirp+", 5, world)
    create_multiple("Peck+", 5, world)

    effective_junk_weights = junk_weights.copy()
    if world.options.include_tournament:
        create_single(f"{TPT} Unlock", world)
        for key, add in junk_weight_additions_tournament.items():
            effective_junk_weights[key] += add

    if world.options.required_collectibles > 0:
        for collectible in collectibles:
            create_single(collectible, world)

    # Junk
    remaining_locations: int = total_location_count - len(world.itempool)
    # trap_count: int = round(remaining_locations * options.trap_fill_percentage / 100)
    junk_count: int = remaining_locations# - trap_count
    junk = get_junk_item_names(world.random, junk_count, effective_junk_weights)
    for name in junk:
        create_single(name, world)
    # traps = get_trap_item_names(world, world.random, trap_count)
    # for name in traps:
    #     create_single(name, world)
    world.multiworld.itempool += world.itempool

class ItemData:
    def __init__(self, code: Optional[int], classification: Optional[ItemClassification]):
        self.code = code
        self.classification = classification

keywe_summer_week_unlocks = {
    f"{SUMMER_WEEK_1} Unlock": ItemData(0x1, ItemClassification.progression),
    f"{SUMMER_WEEK_2} Unlock": ItemData(0x2, ItemClassification.progression),
    f"{SUMMER_WEEK_3} Unlock": ItemData(0x3, ItemClassification.progression),
}

keywe_fall_week_unlocks = {
    f"{FALL_WEEK_1} Unlock": ItemData(0x4, ItemClassification.progression),
    f"{FALL_WEEK_2} Unlock": ItemData(0x5, ItemClassification.progression),
    f"{FALL_WEEK_3} Unlock": ItemData(0x6, ItemClassification.progression),
}

keywe_winter_week_unlocks = {
    f"{WINTER_WEEK_1} Unlock": ItemData(0x7, ItemClassification.progression),
    f"{WINTER_WEEK_2} Unlock": ItemData(0x8, ItemClassification.progression),
    f"{WINTER_WEEK_3} Unlock": ItemData(0x9, ItemClassification.progression),
}

keywe_overtime_unlocks = {
    f"{OT_SUMMER} Unlock": ItemData(0xA, ItemClassification.progression),
    f"{OT_FALL} Unlock": ItemData(0xB, ItemClassification.progression),
    f"{OT_WINTER} Unlock": ItemData(0xC, ItemClassification.progression),
}

keywe_telepost_unlocks = {
    f"{TPT} Unlock": ItemData(0xD, ItemClassification.progression),
}

keywe_cosmetic_items = {
    "Random Facewear": ItemData(0x100, ItemClassification.filler),
    "Random Hat": ItemData(0x101, ItemClassification.filler),
    "Random Skin": ItemData(0x102, ItemClassification.filler),
    "Random Backwear": ItemData(0x103, ItemClassification.filler),
    "Random Hairstyle": ItemData(0x104, ItemClassification.filler),
    "Random Footwear": ItemData(0x105, ItemClassification.filler),
    "Random Arms": ItemData(0x106, ItemClassification.filler),  # Required TPT DLC and Include Tournament
}

keywe_ability_items = {
    "Dash+": ItemData(0x200, ItemClassification.useful),
    "Movement+": ItemData(0x201, ItemClassification.useful),
    "Swim+": ItemData(0x202, ItemClassification.useful),
    "Jump+": ItemData(0x203, ItemClassification.useful),
    "Respawn+": ItemData(0x204, ItemClassification.useful),
    "Chirp+": ItemData(0x205, ItemClassification.useful),
    "Peck+": ItemData(0x206, ItemClassification.useful),
}

keywe_collectible_items = {
    SECRET_SPICE_SHAKER: ItemData(0x300, ItemClassification.progression),
    GLIMMERING_SHELL: ItemData(0x301, ItemClassification.progression),
    EMPTY_CHRYSALIS: ItemData(0x302, ItemClassification.progression),
    TEMPERED_LENS: ItemData(0x303, ItemClassification.progression),
    WAYFARERS_COMPASS: ItemData(0x304, ItemClassification.progression),
    PRICKLY_SEED_POD: ItemData(0x305, ItemClassification.progression),
    ANCIENT_TOOTH: ItemData(0x306, ItemClassification.progression),
    COSMIC_FRIENDSHIP_ROCK: ItemData(0x307, ItemClassification.progression),
    CHARGED_FEATHER: ItemData(0x308, ItemClassification.progression),
    SALTY_SCALE: ItemData(0x309, ItemClassification.progression),
    GLOWING_WISHBONE: ItemData(0x30A, ItemClassification.progression),
    Z39_SOARING_AUK: ItemData(0x30B, ItemClassification.progression),
    PAPA_MOON_FIGURINE: ItemData(0x30C, ItemClassification.progression),
    MOUNTAINEERS_PITON: ItemData(0x30D, ItemClassification.progression),
    LOST_LETTER: ItemData(0x30E, ItemClassification.progression),
}

keywe_item_table: Dict[str, ItemData] = {
    **keywe_summer_week_unlocks,
    **keywe_fall_week_unlocks,
    **keywe_winter_week_unlocks,
    **keywe_ability_items,
    **keywe_collectible_items,
    **keywe_cosmetic_items,
    **keywe_overtime_unlocks,
    **keywe_telepost_unlocks
}

keywe_item_groups = {
    "Weeks - Summer": set(keywe_summer_week_unlocks.keys()),
    "Weeks - Fall": set(keywe_fall_week_unlocks.keys()),
    "Weeks - Winter": set(keywe_winter_week_unlocks.keys()),
    "Overtime": set(keywe_overtime_unlocks.keys()),
    "Tournament": set(keywe_telepost_unlocks.keys()),
    "Cosmetics": set(keywe_cosmetic_items.keys()),
    "Collectibles": set(keywe_collectible_items.keys()),
    "Upgrades": set(keywe_ability_items.keys()),
    "Weeks": (
        set(keywe_summer_week_unlocks.keys())
        | set(keywe_fall_week_unlocks.keys())
        | set(keywe_winter_week_unlocks.keys())
    )
}

junk_weights = {
    "Random Facewear": 14,
    "Random Hat": 22,
    "Random Skin": 23,
    "Random Backwear": 11,
    "Random Hairstyle": 5,
    "Random Footwear": 3,
    "Random Arms" : 0,
}

junk_weight_additions_tournament = {
    "Random Facewear": 0,
    "Random Hat": 3,
    "Random Skin": 0,
    "Random Backwear": 2,
    "Random Hairstyle": 0,
    "Random Footwear": 4,
    "Random Arms" : 4,
}