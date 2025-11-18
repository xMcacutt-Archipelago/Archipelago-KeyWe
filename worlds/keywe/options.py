from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions

class RequiredLevelCompletions(Range):
    """
    Number of unique level completions required to unlock Stand Your Post (Winter 12)
    Compatible with required levels per week.
    """
    display_name = "Required Level Completions"
    range_start = 0
    range_end = 35
    default = 18


class RequiredLevelCompletionsPerWeek(Range):
    """
    Number of unique level completions per week required to unlock Stand Your Post (Winter 12)
    Compatible with required levels.
    Winter - Week 3 will only ever require maximum 3 (does not include Stand Your Post).
    """
    display_name = "Required Level Completions Per Week"
    range_start = 0
    range_end = 4
    default = 1


class RequiredCollectibles(Range):
    """
    Number of hidden collectibles required to unlock Stand Your Post (Winter 12)
    """
    display_name = "Required Collectibles"
    range_start = 0
    range_end = 15
    default = 0


class RequiredCollectibleChecks(Range):
    """
    Number of hidden collectible checks required to unlock Stand Your Post (Winter 12)
    """
    display_name = "Required Collectible Checks"
    range_start = 0
    range_end = 15
    default = 0


class RequiredOvertimeCompletions(Range):
    """
    Number of overtime shift completions required to unlock Stand Your Post (Winter 12)
    MUST HAVE "INCLUDE OVERTIME" ON
    """
    display_name = "Required Overtime Completions"
    range_start = 0
    range_end = 9
    default = 0


class RequiredTournamentCompletions(Range):
    """
    Number of Telepost Tournament completions required to unlock Stand Your Post (Winter 12)
    MUST HAVE "INCLUDE TOURNAMENT" ON
    """
    display_name = "Required Overtime Completions"
    range_start = 0
    range_end = 3
    default = 0


class StartingWeek(Range):
    """
    Choose which week will initially be unlocked.
    """
    display_name = "Starting Week"
    range_start = 1
    range_end = 9
    default = "random"


class LevelCompletionThreshold(Choice):
    """
    Minimum required rank required on level completion to send the level completion check.
    """
    display_name = "Level Completion Threshold"
    option_bronze = 1
    option_silver = 2
    option_gold = 3
    default = 2


class Challengesanity(Toggle):
    """
    Determines whether completing level challenges sends checks.
    """
    display_name = "Challengesanity"


class IncludeOvertime(Toggle):
    """
    Adds items and level completion checks for the Overtime missions.
    WARNING: On gold threshold, these level completion checks are very hard.
    """
    display_name = "Include Overtime"

class IncludeTournament(Toggle):
    """
    Adds challenmges and level completion checks for the Telepost Tournament DLC.
    ALL PLAYERS MUST OWN THE DLC
    """
    display_name = "Include Tournament"

keywe_options = [
    OptionGroup("Extra Content", [
        IncludeOvertime,
        IncludeTournament
    ]),
    OptionGroup("Goal Options", [
        RequiredLevelCompletions,
        RequiredLevelCompletionsPerWeek,
        RequiredCollectibles,
        RequiredCollectibleChecks,
        RequiredOvertimeCompletions,
        RequiredTournamentCompletions
    ]),
    OptionGroup("Logic Options", [
        StartingWeek
    ]),
    OptionGroup("Sanity Options", [
        Challengesanity
    ]),
    OptionGroup("Death Link", [
        DeathLink
    ]),
]


@dataclass
class KeyWeOptions(PerGameCommonOptions):
    include_overtime:                    IncludeOvertime
    include_tournament:                  IncludeTournament
    required_level_completions:          RequiredLevelCompletions
    required_level_completions_per_week: RequiredLevelCompletionsPerWeek
    required_collectibles:               RequiredCollectibles
    required_collectible_checks:         RequiredCollectibleChecks
    required_overtime_completions:       RequiredOvertimeCompletions
    required_tournament_completions:     RequiredTournamentCompletions
    starting_week:                       StartingWeek
    level_completion_check_threshold:    LevelCompletionThreshold
    challengesanity:                     Challengesanity
    death_link: DeathLink


