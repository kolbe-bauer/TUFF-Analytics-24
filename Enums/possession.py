from enum import Enum
from typing import List

from ..Models.defense import Block
from ..Models.team import Player

class OffensiveResult (Enum):
    Score = "score"
    Turn = "turn"

class StartingLine (Enum):
    OLine = "O-Line"
    DLine = "D-Line"

class PossessionStarter (Enum):
    Caught_Pull = "caught pull"
    Picking_Up = "picking up"
    Fast_Break = "fast break"
    Callahan = "callahan"
    From_Brick = "from brick"

class DefensiveResult (Enum):
    Block = Block
    Turn = "turn"
    Score = "Score"
    def validate_possession(self, point_roster: List[Player]) -> bool:
        if self.isinstance(Block):
            return self.validate_block(point_roster)
        return True

class GoingAgainstZone (Enum):
    Yes = "yes"
    No = "no"
