from Enums.game import Tournament, Opponents, StudiedTeams
from Enums.wind import WindSpeed, WindDirection
from Enums.possession import StartingLine, PossessionStarter, DefensiveResult, GoingAgainstZone
from Enums.defense import BlockType


class Possession:
    def __init__(self, tournament: Tournament, wind_speed: WindSpeed, wind_direction: WindDirection,
                 studied_team: StudiedTeams, opponent: Opponents, starting_line: StartingLine,
                 possession_beginner: PossessionStarter, defense_playing_zone: GoingAgainstZone,
                 defensive_result: DefensiveResult, defensive_player,
                 block_type: BlockType, kaching):
        self.tournament = tournament
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.studied_team = studied_team
        self.opponent = opponent
        self.starting_line = starting_line
        self.possession_beginner = possession_beginner
        self.defense_playing_zone = defense_playing_zone
        self.defensive_result = defensive_result
        self.defensive_player = defensive_player
        self.block_type = block_type
        self.kaching = kaching

    def get_tournament(self):
        return self.tournament

    def set_tournament(self, value):
        self.tournament = value

    def get_wind_speed(self):
        return self.wind_speed

    def set_wind_speed(self, value):
        self.wind_speed = value

    def get_wind_direction(self):
        return self.wind_direction

    def set_wind_direction(self, value):
        self.wind_direction = value

    def get_studied_team(self):
        return self.studied_team

    def set_studied_team(self, value):
        self.studied_team = value

    def get_opponent(self):
        return self.opponent

    def set_opponent(self, value):
        self.opponent = value

    def get_starting_line(self):
        return self.starting_line

    def set_starting_line(self, value):
        self.starting_line = value

    def get_possession_beginner(self):
        return self.possession_beginner

    def set_possession_beginner(self, value):
        self.possession_beginner = value

    def get_defense_playing_zone(self):
        return self.defense_playing_zone

    def set_defense_playing_zone(self, value):
        self.defense_playing_zone = value

    def get_defensive_result(self):
        return self.defensive_result

    def set_defensive_result(self, value):
        self.defensive_result = value

    def get_defensive_player(self):
        return self.defensive_player

    def set_defensive_player(self, value):
        self.defensive_player = value

    def get_block_type(self):
        return self.block_type

    def set_block_type(self, value):
        self.block_type = value

    def get_kaching(self):
        return self.kaching

    def set_kaching(self, value):
        self.kaching = value
