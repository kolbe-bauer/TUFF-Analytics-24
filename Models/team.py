from pydantic import BaseModel
from typing import Dict


class Player (BaseModel):
    first_name: str
    last_name: str
    number: int

    def get_player(this) -> str:
        return '#' + str(this.number) + ' ' + this.first_name + ' ' + this.last_name


class Team (BaseModel):
    players: Dict[str, Player]
