from typing import TYPE_CHECKING, Dict, NamedTuple, List, Set
from BaseClasses import ItemClassification as IC, Item

from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World


class ItemInfo(NamedTuple):
    id_offset: int
    classification: IC
    quantity: int


item_table: Dict[str, ItemInfo] = {
    "Torpedo Upgrade": ItemInfo(0, IC.progression, 20),
    "Fuel Tank": ItemInfo(1, IC.progression, 20),
    "Egg": ItemInfo(2, IC.progression, 20),
    # modules
    # the glowy things
}


# this is for filling out item_name_to_id, it should be static regardless of yaml options
def get_items() -> Dict[str, int]:
    return {f"Porgy - {name}": data.id_offset + get_game_base_id("Porgy") for name, data in item_table.items()}


# this should return the item groups for this game, independent of yaml options
def get_item_groups() -> Dict[str, Set[str]]:
    item_groups: Dict[str, Set[str]] = {"Porgy": {f"Porgy - {item_name}" for item_name in item_table.keys()}}
    return item_groups


# for when the world needs to create an item at random (like with random filler items)
def create_item(item_name: str, world: "UFO50World", item_class: IC = None) -> Item:
    base_id = get_game_base_id("Porgy")
    if item_name.startswith("Porgy - "):
        item_name = item_name.split(" - ", 1)[1]
    item_data = item_table[item_name]
    return Item(f"Porgy - {item_name}", item_class or item_data.classification,
                base_id + item_data.id_offset, world.player)


# for when the world is getting the items to place into the multiworld's item pool
def create_items(world: "UFO50World") -> List[Item]:
    items_to_create: Dict[str, int] = {item_name: data.quantity for item_name, data in item_table.items()}
    porgy_items: List[Item] = []
    for item_name, quantity in items_to_create.items():
        for _ in range(quantity):
            porgy_items.append(create_item(item_name, world))
    return porgy_items


filler_items = ["Porgy - Fuel Tank", "Porgy - Missile Upgrade"]


def get_filler_item_name(world: "UFO50World") -> str:
    return world.random.choice(filler_items)