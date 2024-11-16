from typing import TYPE_CHECKING, Dict, NamedTuple, Set
from BaseClasses import Region, Location, Item, ItemClassification
from worlds.generic.Rules import add_rule

from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World


class LocationInfo(NamedTuple):
    id_offset: int
    region_name: str
    fuel_tanks: int = 0  # how many tanks it took to get there and back to a base


location_table: Dict[str, LocationInfo] = {
    # Shallows
    "Shallows Upper Left - Ceiling Torpedo Upgrade": LocationInfo(0, "Shallows"),
    "Shallows Lower Left - Fuel Tank between some Coral": LocationInfo(1, "Shallows"),
    "Shallows Upper Left - Fuel Tank next to Coral": LocationInfo(2, "Shallows"),
    "Shallows Lower Left - Fuel Tank above Breakable Rocks": LocationInfo(3, "Shallows"),
    "Shallows Upper Mid - Torpedo Upgrade at Surface": LocationInfo(4, "Shallows"),
    "Shallows Upper Mid - Fuel Tank on Coral": LocationInfo(5, "Shallows"),
    "Shallows Uppper Mid - Fuel Tank behind ! Blocks": LocationInfo(6, "Shallows"),
    "Shallows Upper Mid - Egg on Coral": LocationInfo(7, "Shallows"),
    "Shallows Upper Mid - Fuel Tank in Floor": LocationInfo(8, "Shallows"),
    "Shallows Mid - Torpedo Upgrade above Breakable Rocks": LocationInfo(9, "Shallows"),
    "Shallows Sunken Ship - Cargo Hold Egg": LocationInfo(10, "Shallows"),
    "Shallows Sunken Ship - Bow Egg": LocationInfo(11, "Shallows"),
    "Shallows Sunken Ship - Bow Hidden Torpedo Upgrade": LocationInfo(12, "Shallows"),
    "Shallows Sunken Ship - Depth Charge Module": LocationInfo(13, "Shallows"),
    "Shallows Lower Mid - Super Booster Module": LocationInfo(14, "Shallows"),
    "Shallows Lower Mid - Fuel Tank on Coral": LocationInfo(15, "Shallows"),
    "Shallows Lower Mid - Egg on Coral": LocationInfo(16, "Shallows"),
    "Shallows Lower Mid - Lower Ceiling Torpedo Upgrade": LocationInfo(17, "Shallows"),
    "Shallows Lower Mid - Upper Ceiling Torpedo Upgrade": LocationInfo(18, "Shallows"),
    "Shallows Lower Mid - Fuel Tank in Floor": LocationInfo(19, "Shallows"),
    "Shallows Lower Mid - Torpedo Upgrade on Coral": LocationInfo(20, "Shallows"),
    "Shallows Upper Right - Fuel Tank under Breakable Rocks": LocationInfo(21, "Shallows"),
    "Shallows Upper Right - Fuel Tank in Coral Maze": LocationInfo(22, "Shallows"),
    "Shallows Upper Right - Torpedo Upgrade in Coral Maze": LocationInfo(23, "Shallows"),
    "Shallows Upper Right - Egg in Coral Maze": LocationInfo(24, "Shallows"),
    "Shallows Lower Right - Fuel Tank under Breakable Rocks": LocationInfo(25, "Shallows"),
    "Shallows Lower Right - Buster Torpedoes Module": LocationInfo(26, "Shallows"),
    "Shallows Lower Right - Egg behind ! Blocks": LocationInfo(27, "Shallows"),
    "Shallows Lower Right - Egg in Coral": LocationInfo(28, "Shallows"),
    "Shallows Lower Right - Drill Module": LocationInfo(29, "Shallows"),

    # Deeper
    "Deeper Upper Left - Torpedo Upgrade in Wall": LocationInfo(30, "Deeper"),
    "Deeper Upper Left - Egg by Urchins": LocationInfo(31, "Deeper"),
    "Deeper Upper Left - Fuel Tank on Coral": LocationInfo(32, "Deeper"),
    "Deeper Upper Left - Fuel Tank behind ! Blocks": LocationInfo(33, "Deeper"),
    "Deeper Upper Mid - Torpedo Upgrade on Coral": LocationInfo(34, "Deeper"),
    "Deeper Upper Mid - Torpedo Upgrade in Ceiling": LocationInfo(35, "Deeper"),
    "Deeper Upper Mid - Egg in Dirt": LocationInfo(36, "Deeper"),
    "Deeper Upper Mid - Spotlight Module": LocationInfo(37, "Deeper"),
    "Deeper Upper Mid - Fuel Tank in Collapsed Structure": LocationInfo(38, "Deeper"),
    "Deeper Upper Right - Fuel Tank in Collapsed Structure": LocationInfo(39, "Deeper"),
    "Deeper Upper Right - Egg on Coral": LocationInfo(40, "Deeper"),
    "Deeper Upper Right - Torpedo Upgrade in Wall": LocationInfo(41, "Deeper"),
    "Deeper Right - Torpedo Upgrade on Coral": LocationInfo(42, "Deeper"),
    "Deeper Upper Right - Targeting System Module": LocationInfo(43, "Deeper"),
    "Deeper Lower Right - Egg behind Urchins": LocationInfo(44, "Deeper"),
    "Deeper Lower Right - Fuel Tank in Ceiling": LocationInfo(45, "Deeper"),
    "Deeper Lower Right - Egg on Coral": LocationInfo(46, "Deeper"),
    "Deeper Lower Mid - Missile System Module": LocationInfo(47, "Deeper"),
    "Deeper Lower Mid - Torpedo Upgrade on Coral": LocationInfo(48, "Deeper"),
    "Deeper Lower Mid - Fuel Tank in Floor": LocationInfo(49, "Deeper"),
    "Deeper Lower Left - Egg in Wall": LocationInfo(50, "Deeper"),

    # Abyss
    "Abyss Upper Left - Egg on Seaweed near Urchins": LocationInfo(51, "Abyss"),
    "Abyss Upper Left - Fuel Tank on Seaweed": LocationInfo(52, "Abyss"),
    "Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade": LocationInfo(53, "Abyss"),
    "Abyss Upper Left - Torpedo Upgrade in Seaweed": LocationInfo(54, "Abyss"),
    "Abyss Lower Left - Egg in Facility": LocationInfo(55, "Abyss"),
    "Abyss Lower Left - Torpedo Upgrade in Facility": LocationInfo(56, "Abyss"),
    "Abyss Lower Left - Fuel Tank in Facility Floor": LocationInfo(57, "Abyss"),
    "Abyss Upper Mid - Torpedo Upgrade in Wall": LocationInfo(58, "Abyss"),
    "Abyss Upper Mid - Torpedo Upgrade in Cave": LocationInfo(59, "Abyss"),
    "Abyss Upper Mid - Egg on Seaweed": LocationInfo(60, "Abyss"),
    "Abyss Upper Mid - Efficient Fuel Module": LocationInfo(61, "Abyss"),
    "Abyss Upper Mid - Egg in Seaweed": LocationInfo(62, "Abyss"),
    "Abyss Upper Mid - Torpedo Upgrade behind Seaweed": LocationInfo(63, "Abyss"),
    "Abyss Upper Right - Egg by Seaweed": LocationInfo(64, "Abyss"),
    "Abyss Upper Right - Torpedo Upgrade in Wall": LocationInfo(65, "Abyss"),
    "Abyss Lower Right - Fuel Tank in Floor": LocationInfo(66, "Abyss"),
    "Abyss Lower Right - Egg": LocationInfo(67, "Abyss"),
    "Abyss Lower Right - Radar System Module": LocationInfo(68, "Abyss"),
    "Abyss Lower Right - Armor Plating Module": LocationInfo(69, "Abyss"),

    # Bosses
    "Lamia": LocationInfo(100, "Shallows"),
    "Second Boss": LocationInfo(101, "Shallows"),
    "Eel": LocationInfo(102, "Deeper"),
    "Big shell thing": LocationInfo(103, "Deeper"),
    "Whatever was in the Abyss": LocationInfo(104, "Abyss"),

    "Garden": LocationInfo(997, "Menu"),
    "Gold": LocationInfo(998, "Abyss"),
    "Cherry": LocationInfo(999, "Boss Area")
}


# this is for filling out location_name_to_id, it should be static regardless of yaml options
def get_locations() -> Dict[str, int]:
    return {f"Porgy - {name}": data.id_offset + get_game_base_id("Porgy") for name, data in location_table.items()}


# this should return the location groups for this game, independent of yaml options
# you should include a group that contains all location for this game that is called the same thing as the game
def get_location_groups() -> Dict[str, Set[str]]:
    location_groups: Dict[str, Set[str]] = {"Porgy": {f"Porgy - {loc_name}" for loc_name in location_table.keys()}}
    return location_groups


# this is not a required function, but a recommended one -- the world class does not call this function
def create_locations(world: "UFO50World", regions: Dict[str, Region]) -> None:
    for loc_name, loc_data in location_table.items():
        if loc_name == "Cherry" and "Porgy" not in world.options.cherry_allowed_games:
            break
        if loc_name in ["Gold", "Cherry"] and "Porgy" in world.goal_games:
            if (loc_name == "Gold" and "Porgy" not in world.options.cherry_allowed_games) or loc_name == "Cherry":
                loc = Location(world.player, f"Porgy - {loc_name}", None, regions[loc_data.region_name])
                loc.place_locked_item(Item("Completed Porgy", ItemClassification.progression, None, world.player))
                add_rule(world.get_location("Completed All Games"), lambda state: state.has("Completed Porgy", world.player))
                regions[loc_data.region_name].locations.append(loc)
                break

        loc = Location(world.player, f"Porgy - {loc_name}", get_game_base_id("Porgy") + loc_data.id_offset,
                       regions[loc_data.region_name])
        regions[loc_data.region_name].locations.append(loc)