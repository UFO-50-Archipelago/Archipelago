from dataclasses import dataclass
from Options import StartInventoryPool, Range, OptionSet, PerGameCommonOptions, OptionGroup
from .constants import game_ids


class AlwaysOnGames(OptionSet):
    """
    Choose which games you would like to enable.
    """
    internal_name = "always_on_games"
    display_name = "Always On Games"
    valid_keys = {game_name for game_name in game_ids.keys()}


class RandomChoiceGames(OptionSet):
    """
    Choose which games have a chance of being enabled.
    The number of games that will be enabled is based on the Random Choice Game Count option.
    """
    internal_name = "random_choice_games"
    display_name = "Random Choice Games"
    valid_keys = {game_name for game_name in game_ids.keys()}


class RandomChoiceGameCount(Range):
    """
    Choose how many Random Choice Games will be included alongside your Always On Games.
    If you do not have enough Random Choice Games selected, it will enable all your selected games.
    """
    internal_name = "random_choice_game_count"
    display_name = "Random Choice Game Count"
    range_start = 0
    range_end = 50
    default = 0


class StartingGameAmount(Range):
    """
    Choose how many games to have unlocked at the start.
    At least on of the starting games will always be one of the implemented games.
    If this value is higher than the number of games you selected, you will start with all of them unlocked.
    If you put a game in your start inventory from pool, it will count towards the amount from this option.
    """
    internal_name = "starting_game_amount"
    display_name = "Starting Game Amount"
    range_start = 1
    range_end = 50
    default = 1


class GoalGames(OptionSet):
    """
    Choose which games you may have to complete to achieve your goal.
    """
    internal_name = "goal_games"
    display_name = "Goal Games"
    valid_keys = {game_name for game_name in game_ids.keys()}
    default = {game_name for game_name in game_ids.keys()}


class GoalGameAmount(Range):
    """
    Choose how many games you need to goal to achieve your goal among your Goal Games.
    If this number is less than the number of Goal Games you have selected, it will choose some of them at random to be your Goal Games.
    If this number is greater than or equal to your number of Goal Games, then all of your games will be your Goal Games.
    """
    internal_name = "goal_game_amount"
    display_name = "Goal Game Amount"
    range_start = 1
    range_end = 50
    default = 50


class CherryAllowed(OptionSet):
    """
    Choose which games you want to include the Cherry goal in.
    If the game is set as your Goal Game, then you will need to Cherry that game to complete that goal.
    If the game is not set as a Goal Game, then Cherrying that game will be a check.
    """
    internal_name = "cherry_allowed_games"
    display_name = "Cherry-Allowed Games"
    valid_keys = {game_name for game_name in game_ids.keys()}
    # include the games where it makes sense to be Cherry by default
    default = {"Barbuta", "Night Manor"}


@dataclass
class UFO50Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    always_on_games: AlwaysOnGames
    random_choice_games: RandomChoiceGames
    random_choice_game_count: RandomChoiceGameCount
    starting_game_amount: StartingGameAmount
    goal_games: GoalGames
    goal_game_amount: GoalGameAmount
    cherry_allowed_games: CherryAllowed


ufo50_option_groups = [
    OptionGroup("General Options", [
        AlwaysOnGames,
        RandomChoiceGames,
        RandomChoiceGameCount,
        StartingGameAmount,
        GoalGames,
        GoalGameAmount,
        CherryAllowed,
    ])
]