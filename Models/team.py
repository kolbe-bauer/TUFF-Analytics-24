from pydantic import BaseModel
from typing import Dict


class Player (BaseModel):
    first_name: str
    last_name: str
    number: int

    def get_player(self) -> str:
        return '#' + str(self.number) + ' ' + self.first_name + ' ' + self.last_name


class Team (BaseModel):
    players: Dict[str, Player]
