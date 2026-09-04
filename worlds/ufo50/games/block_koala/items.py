from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import ItemClassification as IC, Item
from worlds.sc2.item import item_groups

from ...constants import get_game_base_id
from .locations import sphere_1_locs

if TYPE_CHECKING:
    from ... import UFO50World


class ItemInfo(NamedTuple):
    id_offset: int
    classification: IC
    quantity: int = 1

item_table: dict[str, ItemInfo] = {
    "Start Gate": ItemInfo(0, IC.progression),
    "Bottom Left Gate": ItemInfo(1, IC.progression),
    "Centre Gate": ItemInfo(2, IC.progression),
    "Mid Left Gate": ItemInfo(3, IC.progression),
    "Top Right Gates": ItemInfo(4, IC.progression),
    "Boss Gate": ItemInfo(6, IC.progression),
    "Koala Fact": ItemInfo(101, IC.filler, quantity=44)
}


def get_items() -> dict[str, int]:
    return {f"Block Koala - {name}": data.id_offset + get_game_base_id("Block Koala") for name, data in item_table.items()}


def get_item_groups() -> dict[str, set[str]]:
    return {"Block Koala": {f"Block Koala - {item_name}" for item_name in item_table.keys()}}

def create_item(item_name: str, world: "UFO50World", item_class: IC = None) -> Item:
    base_id = get_game_base_id("Block Koala")
    if item_name.startswith("Block Koala - "):
        item_name = item_name.split(" - ", 1)[1]
    item_data = item_table[item_name]
    return Item(f"Block Koala - {item_name}", item_class or item_data.classification,
                base_id + item_data.id_offset, world.player)


def create_items(world: "UFO50World") -> list[Item]:
    items_to_create: dict[str, int] = {item_name: data.quantity for item_name, data in item_table.items()}
    block_koala_items: list[Item] = []
    if world.options.block_koala_early_start_gate:
        items_to_create["Start Gate"] = 0
        start_gate = create_item("Start Gate", world)
        loc = world.get_location("Block Koala - " + world.random.choice(sphere_1_locs))
        loc.place_locked_item(start_gate)

    for item_name, quantity in items_to_create.items():
        for _ in range(quantity):
            block_koala_items.append(create_item(item_name, world))
    return block_koala_items


def get_filler_item_name(world: "UFO50World") -> str:
    return "Block Koala - Koala Fact"

