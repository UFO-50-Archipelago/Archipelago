from typing import NamedTuple, TYPE_CHECKING

from BaseClasses import Region

from .locations import create_locations
from .rules import create_rules

if TYPE_CHECKING:
    from ... import UFO50World


regions: list[str] = [
    "Menu",
    "Start",
    "Bottom Left",
    "Bottom Right",
    "Mid Left",
    "Mid Right",
    "Top",
    "Boss"
]


def create_regions_and_rules(world: "UFO50World") -> dict[str, Region]:
    block_koala_regions: dict[str, Region] = {}
    for region_name in regions:
        block_koala_regions[region_name] = Region(f"Block Koala - {region_name}", world.player, world.multiworld)

    create_locations(world, block_koala_regions)
    create_rules(world, block_koala_regions)

    return block_koala_regions
