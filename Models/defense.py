from pydantic import BaseModel
from typing import List, Optional

from team import Player
from ..Enums.defense import BlockType

class Block (BaseModel):
    player: Player
    block_type: BlockType
    def validate_block (self, point_roster: List[Player]) -> bool:
        return self.player in point_roster