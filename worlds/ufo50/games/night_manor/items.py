from typing import TYPE_CHECKING, Dict, NamedTuple, List, Set
from BaseClasses import ItemClassification as IC, Item

from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World


class ItemInfo(NamedTuple):
    id_offset: int
    classification: IC
    quantity: int = 1


# TODO: Add conditional item classification based on if victory type needed is gift, gold, cherry.
item_table: Dict[str, ItemInfo] = {
    "Spoon": ItemInfo(0, IC.progression),
    "Bowl": ItemInfo(1, IC.progression),
    "Yellow Note": ItemInfo(2, IC.filler),
    "Hairpin": ItemInfo(3, IC.progression),
    "Tweezers": ItemInfo(4, IC.progression),
    "Hook": ItemInfo(7, IC.progression),
    "Batteries": ItemInfo(8, IC.progression),
    "Coins": ItemInfo(10, IC.progression),
    "Matches": ItemInfo(11, IC.progression),
    "Kitchen Knife": ItemInfo(14, IC.progression),
    "Drain Cleaner": ItemInfo(15, IC.progression),
    "Oil Can": ItemInfo(16, IC.progression),
    "Flashlight": ItemInfo(17, IC.progression),
    "Duct Tape": ItemInfo(18, IC.progression),
    "Gas Can": ItemInfo(20, IC.progression),
    "Crowbar": ItemInfo(21, IC.progression),
    "Ornamental Egg": ItemInfo(22, IC.progression),
    "Pool Cue": ItemInfo(25, IC.progression),
    "Sheet Music": ItemInfo(27, IC.progression),
    "Screwdriver": ItemInfo(29, IC.progression),
    "Wrench": ItemInfo(31, IC.progression),
    "Hedge Shears": ItemInfo(32, IC.progression),
    "Shovel": ItemInfo(33, IC.progression),
    "Motor": ItemInfo(36, IC.progression),
    "Hacksaw": ItemInfo(38, IC.progression),
    "Ring": ItemInfo(40, IC.progression),
    "Gear": ItemInfo(42, IC.progression),
    "Magnifying Glass": ItemInfo(47, IC.progression),
    "Tea Tree Oil": ItemInfo(48, IC.progression),
    "Hydrogen Peroxide": ItemInfo(49, IC.progression),
    "Safe Combination": ItemInfo(50, IC.progression),
    "Cigar Butt": ItemInfo(52, IC.progression),
    "Computer Password": ItemInfo(55, IC.progression),
    "Piano Wire": ItemInfo(57, IC.progression),
    "Crossbow": ItemInfo(58, IC.progression),
    "Doll": ItemInfo(59, IC.progression),
    "Fungicide Recipe": ItemInfo(62, IC.progression),
    "Fungicide": ItemInfo(63, IC.progression),
    "Glasses": ItemInfo(65, IC.progression),
    "Maze Directions": ItemInfo(66, IC.progression),
    "Crossbow Bolt": ItemInfo(67, IC.progression),

    "Red Gemstone": ItemInfo(23, IC.progression),
    "Green Gemstone": ItemInfo(43, IC.progression),
    "Yellow Gemstone": ItemInfo(53, IC.progression),
    "White Gemstone": ItemInfo(64, IC.progression),

    "Copper Key": ItemInfo(28, IC.progression),
    "Bronze Key": ItemInfo(34, IC.progression),
    "Gold Key": ItemInfo(35, IC.progression),
    "Steel Key": ItemInfo(37, IC.progression),
    "Silver Key": ItemInfo(39, IC.progression),
    "Brass Key": ItemInfo(41, IC.progression),
    "Aluminum Key": ItemInfo(60, IC.progression),
    "Iron Key": ItemInfo(68, IC.progression),

    "Journal Entry 1": ItemInfo(9, IC.filler),
    "Journal Entry 2": ItemInfo(5, IC.filler),
    "Journal Entry 3": ItemInfo(56, IC.filler),
    "Journal Entry 4": ItemInfo(12, IC.filler),
    "Journal Entry 5": ItemInfo(6, IC.filler),
    "Journal Entry 6": ItemInfo(46, IC.filler),
    "Journal Entry 7": ItemInfo(13, IC.filler),
    "Journal Entry 8": ItemInfo(19, IC.filler),
    "Journal Entry 9": ItemInfo(24, IC.filler),
    "Journal Entry 10": ItemInfo(26, IC.filler),
    "Journal Entry 11": ItemInfo(30, IC.filler),
    "Journal Entry 12": ItemInfo(44, IC.filler),
    "Journal Entry 13": ItemInfo(54, IC.filler),
    "Journal Entry 14": ItemInfo(61, IC.filler),
    "Journal Entry 15": ItemInfo(45, IC.filler),
    "Journal Entry 16": ItemInfo(51, IC.filler),
    "Journal Entry 17": ItemInfo(69, IC.filler)

}


# this is for filling out item_name_to_id, it should be static regardless of yaml options
def get_items() -> Dict[str, int]:
    return {f"Night Manor - {name}": data.id_offset + get_game_base_id("Night Manor") for name, data in item_table.items()}

# this should return the item groups for this game, independent of yaml options
# you should include a group that contains all items for this game that is called the same thing as the game


def get_item_groups() -> Dict[str, Set[str]]:
    item_groups: Dict[str, Set[str]] = {"Night Manor": {
        f"Night Manor - {item_name}" for item_name in item_table.keys()}}
    item_groups.update({
        "Night Manor - Journal Entries": {"Night Manor - Journal Entry 1",
                            "Night Manor - Journal Entry 2",
                            "Night Manor - Journal Entry 3",
                            "Night Manor - Journal Entry 4",
                            "Night Manor - Journal Entry 5",
                            "Night Manor - Journal Entry 6",
                            "Night Manor - Journal Entry 7",
                            "Night Manor - Journal Entry 8",
                            "Night Manor - Journal Entry 9",
                            "Night Manor - Journal Entry 10",
                            "Night Manor - Journal Entry 11",
                            "Night Manor - Journal Entry 12",
                            "Night Manor - Journal Entry 13",
                            "Night Manor - Journal Entry 14",
                            "Night Manor - Journal Entry 15",
                            "Night Manor - Journal Entry 16",
                            "Night Manor - Journal Entry 17"},
        "Night Manor - Gems": {"Night Manor - Red Gemstone",
                 "Night Manor - Green Gemstone",
                 "Night Manor - Yellow Gemstone",
                 "Night Manor - White Gemstone"},
        "Night Manor - Keys": {"Night Manor - Copper Key",
                 "Night Manor - Bronze Key",
                 "Night Manor - Gold Key",
                 "Night Manor - Steel Key",
                 "Night Manor - Silver Key",
                 "Night Manor - Brass Key",
                 "Night Manor - Aluminum Key",
                 "Night Manor - Iron Key"}
    })
    return item_groups

# for when the world needs to create an item at random (like with random filler items)
# the first argument must be the item name. It must be able to handle the world giving it an actual item name
# the second argument must be the world class
# the third argument can optionally be an item classification, `item_class: ItemClassification = None`


def create_item(item_name: str, world: "UFO50World") -> Item:
    base_id = get_game_base_id("Night Manor")
    if item_name.startswith("Night Manor - "):
        item_name = item_name.split(" - ", 1)[1]
    item_data = item_table[item_name]
    return Item(f"Night Manor - {item_name}", item_data.classification, base_id + item_data.id_offset, world.player)

# for when the world is getting the items to place into the multiworld's item pool
# you must pass in the world class as the argument


def create_items(world: "UFO50World") -> List[Item]:
    items_to_create: Dict[str, int] = {
        item_name: data.quantity for item_name, data in item_table.items()}
    night_manor_items: List[Item] = []
    for item_name, quantity in items_to_create.items():
        for _ in range(quantity):
            night_manor_items.append(create_item(item_name, world))
    return night_manor_items


def get_filler_item_name() -> str:
    return "Night Manor - Yellow Note"