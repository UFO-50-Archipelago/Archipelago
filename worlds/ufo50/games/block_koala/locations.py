from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Region, Location, Item, ItemClassification
from worlds.generic.Rules import add_rule

from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World


class LocationInfo(NamedTuple):
    id_offset: int
    region_name: str


location_table: dict[str, LocationInfo] = {
    # Start (Level 1)
    "Level 1": LocationInfo(1, "Start"),

    # Bottom Left (Levels 2-6)
    "Level 2": LocationInfo(2, "Bottom Left"),
    "Level 3": LocationInfo(3, "Bottom Left"),
    "Level 4": LocationInfo(4, "Bottom Left"),
    "Level 5": LocationInfo(5, "Bottom Left"),
    "Level 6": LocationInfo(6, "Bottom Left"),

    # Mid Left (Levels 7-14)
    "Level 7": LocationInfo(7, "Mid Left"),
    "Level 8": LocationInfo(8, "Mid Left"),
    "Level 9": LocationInfo(9, "Mid Left"),
    "Level 10": LocationInfo(10, "Mid Left"),
    "Level 11": LocationInfo(11, "Mid Left"),
    "Level 12": LocationInfo(12, "Mid Left"),
    "Level 13": LocationInfo(13, "Mid Left"),
    "Level 14": LocationInfo(14, "Mid Left"),

    # Bottom Right (Levels 15-27)
    "Level 15": LocationInfo(15, "Bottom Right"),
    "Level 16": LocationInfo(16, "Bottom Right"),
    "Level 17": LocationInfo(17, "Bottom Right"),
    "Level 18": LocationInfo(18, "Bottom Right"),
    "Level 19": LocationInfo(19, "Bottom Right"),
    "Level 20": LocationInfo(20, "Bottom Right"),
    "Level 21": LocationInfo(21, "Bottom Right"),
    "Level 22": LocationInfo(22, "Bottom Right"),
    "Level 23": LocationInfo(23, "Bottom Right"),
    "Level 24": LocationInfo(24, "Bottom Right"),
    "Level 25": LocationInfo(25, "Bottom Right"),
    "Level 26": LocationInfo(26, "Bottom Right"),
    "Level 27": LocationInfo(27, "Bottom Right"),

    # Top (Levels 28-40)
    "Level 28": LocationInfo(28, "Top"),
    "Level 29": LocationInfo(29, "Top"),
    "Level 30": LocationInfo(30, "Top"),
    "Level 31": LocationInfo(31, "Top"),
    "Level 32": LocationInfo(32, "Top"),
    "Level 33": LocationInfo(33, "Top"),
    "Level 34": LocationInfo(34, "Top"),
    "Level 35": LocationInfo(35, "Top"),
    "Level 36": LocationInfo(36, "Top"),
    "Level 37": LocationInfo(37, "Top"),
    "Level 38": LocationInfo(38, "Top"),
    "Level 39": LocationInfo(39, "Top"),
    "Level 40": LocationInfo(40, "Top"),

    # Mid Right (Levels 41-49)
    "Level 41": LocationInfo(41, "Mid Right"),
    "Level 42": LocationInfo(42, "Mid Right"),
    "Level 43": LocationInfo(43, "Mid Right"),
    "Level 44": LocationInfo(44, "Mid Right"),
    "Level 45": LocationInfo(45, "Mid Right"),
    "Level 46": LocationInfo(46, "Mid Right"),
    "Level 47": LocationInfo(47, "Mid Right"),
    "Level 48": LocationInfo(48, "Mid Right"),
    "Level 49": LocationInfo(49, "Mid Right"),

    # Boss (Level 50)
    "Level 50": LocationInfo(50, "Boss"),

    # Goal locations
    "Garden": LocationInfo(997, "Start"),
    "Gold": LocationInfo(998, "Boss"),
    "Cherry": LocationInfo(999, "Boss")
}


sphere_1_locs: list[str] = ["Level 1", "Garden"]


def get_locations() -> dict[str, int]:
    return {f"Block Koala - {name}": data.id_offset + get_game_base_id("Block Koala") for name, data in location_table.items()}


def get_location_groups() -> dict[str, set[str]]:
    location_groups: dict[str, set[str]] = {"Block Koala": {f"Block Koala - {loc_name}"
                                                             for loc_name in location_table.keys()}}
    return location_groups


def create_locations(world: "UFO50World", regions: dict[str, Region]) -> None:
    for loc_name, loc_data in location_table.items():
        if loc_name == "Cherry" and "Block Koala" not in world.options.cherry_allowed_games:
            break
        if loc_name in ["Gold", "Cherry"] and "Block Koala" in world.goal_games:
            if (loc_name == "Gold" and "Block Koala" not in world.options.cherry_allowed_games) or loc_name == "Cherry":
                loc = Location(world.player, f"Block Koala - {loc_name}", None, regions[loc_data.region_name])
                loc.place_locked_item(Item("Completed Block Koala", ItemClassification.progression, None, world.player))
                add_rule(world.get_location("Completed All Games"), lambda state: state.has("Completed Block Koala", world.player))
                regions[loc_data.region_name].locations.append(loc)
                break

        loc = Location(world.player, f"Block Koala - {loc_name}", get_game_base_id("Block Koala") + loc_data.id_offset,
                       regions[loc_data.region_name])
        regions[loc_data.region_name].locations.append(loc)
