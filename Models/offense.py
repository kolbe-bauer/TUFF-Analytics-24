import math

from pydantic import BaseModel
from typing import List, Optional

from team import Player
from ..Enums.possession import OffensiveResult
from ..Enums.throw import ThrowForce, ThrowType, ThrowSubtype, ThrowOutcome, ThrowDecision
from ..Enums.wind import WindSpeed, WindDirection

class DiscPosition (BaseModel):
    x: int
    y: int
    def get_polygon_id(self) -> str:
        #TODO: implement this logic
        return 'c4'
    def validate_disc_position(self) -> bool:
        #TODO: implement this logic
        return True

class FieldPosition (DiscPosition):
    player: Player
    def validate_field_position(self, point_roster: List[Player]) -> bool:
        return self.validate_disc_position and self.player in point_roster
    
class ThrowData (BaseModel):
    throw_force: ThrowForce
    throw_type: ThrowType
    throwing_motion: ThrowSubtype
    wind_speed: Optional[WindSpeed]
    wind_direction: Optional[WindDirection]

class Throw (ThrowData):
    thrower: FieldPosition
    receiver: FieldPosition
    throw_outcome: ThrowOutcome
    throw_decision: ThrowDecision
    def validate_throw(self, point_roster: List[Player]) -> bool:
        return self.thrower.validate_field_position(point_roster) and self.receiver.validate_field_position(point_roster)
    def get_vertical_yards(self) -> int:
        return self.receiver.y - self.thrower.y
    def get_horizontal_yards(self) -> int:
        return self.receiver.x - self.thrower.x
    def get_total_throwing_yards(self) -> int:
        return math.sqrt(self.get_horizontal_yards ** 2 + self.get_vertical_yards ** 2)
    def is_reset_throw(self) -> bool:
        return self.receiver <= self.thrower
    def is_swing_throw(self) -> bool:
        return self.get_horizontal_yards > self.get_vertical_yards

class OffensivePossession (BaseModel):
    throws: List[Throw]
    possession_result: OffensiveResult
    def validate_possession(self, point_roster: List[Player]) -> bool:
        state = True
        for throw in self.throws:
            state = state and throw.validate_throw(point_roster)
        return state
    def get_length_to_result(self) -> int:
        return len(self.throws)