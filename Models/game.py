from pydantic import BaseModel
from typing import List

from team import Player, Team
from offense import OffensivePossession
from ..Enums.possession import DefensiveResult

class Point (BaseModel):
    point_roster: List[Player]
    offensive_possessions: List[OffensivePossession]
    defensive_possessions: List[DefensiveResult]
    score: (int, int)
    def validate_point (self) -> bool:
        if self.offensive_possessions < 1 and self.defensive_possessions < 1:
            return False
        state = True
        for possession in self.offensive_possessions:
            state = state and possession.validate_possession(self.point_roster)
        for possession in self.defensive_possessions:
            state = state and possession.validate_possession(self.point_roster)
        return state
    
class Game (BaseModel):
    tournament: str
    team1: Team
    team2: Team
    points: List[Point]
    def validate_game (self) -> bool:
        state = True
        for point in self.points:
            state = state and point.validate_point()
        return True