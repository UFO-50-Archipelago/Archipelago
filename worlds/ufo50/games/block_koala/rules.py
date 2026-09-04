from typing import TYPE_CHECKING

from BaseClasses import Region
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from ... import UFO50World

gate_start_bottom_left = "Block Koala - Start Gate"
gate_bottom_left_mid_left = "Block Koala - Bottom Left Gate"
gate_mid_left_bottom_right = "Block Koala - Centre Gate"
gate_mid_left_top = "Block Koala - Mid Left Gate"
gate_bottom_right_boss = "Block Koala - Boss Gate"
gate_mid_right_top = "Block Koala - Top Right Gates"

def create_rules(world: "UFO50World", regions: dict[str, Region]) -> None:
    player = world.player

    regions["Menu"].connect(regions["Start"])

    regions["Start"].connect(regions["Bottom Left"], rule=lambda state: state.has(gate_start_bottom_left, player))
    regions["Bottom Left"].connect(regions["Mid Left"], rule=lambda state: state.has(gate_bottom_left_mid_left, player))

    regions["Mid Left"].connect(regions["Bottom Right"], rule=lambda state: state.has(gate_mid_left_bottom_right, player))
    regions["Mid Left"].connect(regions["Top"], rule=lambda state: state.has(gate_mid_left_top, player))

    regions["Bottom Right"].connect(regions["Boss"], rule=lambda state: state.has(gate_bottom_right_boss, player))
    regions["Bottom Right"].connect(regions["Mid Right"], rule=lambda state: state.has(gate_mid_right_top, player))

    regions["Mid Right"].connect(regions["Top"], rule=lambda state: state.has(gate_mid_right_top, player))


    set_rule(world.get_location("Block Koala - Garden"), rule=lambda state: True)

    # Gold Goal: Access Boss region (Level 50)
    set_rule(world.get_location("Block Koala - Gold"), rule=lambda state: True)

    # Cherry Goal: Complete all 50 levels (access to all regions)
    if "Block Koala" in world.options.cherry_allowed_games:
        all_gates = [
            gate_start_bottom_left,
            gate_bottom_left_mid_left,
            gate_mid_left_bottom_right,
            gate_mid_left_top,
            gate_mid_right_top,
            gate_bottom_right_boss,
        ]
        set_rule(world.get_location("Block Koala - Cherry"), rule=lambda state: state.has_all(all_gates, player))
