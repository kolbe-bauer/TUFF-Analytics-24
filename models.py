import math
from pydantic import BaseModel
import string
from typing import Array

import enums

class FieldPosition(BaseModel):
    x: int
    y: int

class Player(BaseModel):
    first_name: string
    last_name: string
    number: int
    def get_player_name(this) -> string:
        return this.first_name + ' ' + this.last_name

class OffensiveThrow(BaseModel):
    thrower: Player
    receiver: Player
    thrower_position: FieldPosition
    receiver_position: FieldPosition
    throwing_motion: enums.ThrowMotion
    throw_type: enums.ThrowType
    throw_force: enums.ThrowForce
    completion: bool
    throwing_grade: bool
    def get_vertical_yards(self) -> int:
        return self.receiver_position.y - self.thrower_position.y
    def get_horizontal_yards(self) -> int:
        return self.receiver_position.x - self.thrower_position.x
    def get_total_throwing_yards(self) -> int:
        return math.sqrt(self.get_horizontal_yards ** 2 + self.get_vertical_yards ** 2)
    def is_reset_throw(self) -> bool:
        return self.receiver_position <= self.thrower_position
    def is_swing_throw(self) -> bool:
        return self.get_horizontal_yards > self.get_vertical_yards
    
class OffensivePossession(BaseModel):
    throwing_sequence: Array(OffensiveThrow)
    possession_result: enums.PossessionResult
    def get_length_to_result(self) -> int:
        return len(self.throwing_sequence)
    
class PointPlayed(BaseModel):
    players: Array(Player)
    offensive_possessions: Array(OffensivePossession)
    defensive_possessions: bool # todo: I don't really know how to take notes on defense but fill this in
    
class GamePlayed(BaseModel):
    points_sequence: Array(PointPlayed)
