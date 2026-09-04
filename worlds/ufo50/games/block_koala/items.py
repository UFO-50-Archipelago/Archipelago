from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import ItemClassification as IC, Item

from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World


class ItemInfo(NamedTuple):
    id_offset: int
    classification: IC
    quantity: int = 1


gate_items: list[str] = [
    "Start Gate",
    "Bottom Left Gate",
    "Centre Gate",
    "Mid Left Gate",
    "Mid Right Gate",
    "Boss Gate",
    "Top Right Gate",
]

item_table: dict[str, ItemInfo] = {
    gate: ItemInfo(idx, IC.progression) for idx, gate in enumerate(gate_items)
}
item_table["Koala Fact"] = ItemInfo(len(gate_items), IC.filler, quantity=43)


def get_items() -> dict[str, int]:
    return {f"Block Koala - {name}": data.id_offset + get_game_base_id("Block Koala") for name, data in item_table.items()}


def get_item_groups() -> dict[str, set[str]]:
    item_groups: dict[str, set[str]] = {
        "Block Koala": {f"Block Koala - {item_name}" for item_name in item_table.keys()},
        "Block Koala - Gates": {f"Block Koala - {gate}" for gate in gate_items},
    }
    return item_groups


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
    for item_name, quantity in items_to_create.items():
        for _ in range(quantity):
            block_koala_items.append(create_item(item_name, world))
    return block_koala_items


def get_filler_item_name(world: "UFO50World") -> str:
    return "Block Koala - Koala Fact"

