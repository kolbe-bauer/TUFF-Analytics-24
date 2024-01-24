class Point:
    def __init__(self, point_roster: list, coordinates: list):
        self.point_roster = point_roster
        self.coordinates = coordinates

    def get_point_roster(self):
        return self.point_roster

    def set_point_roster(self, point_roster):
        self.point_roster = point_roster

    def get_point_coordinates(self):
        return self.coordinates

    def set_point_coordinates(self, coordinates):
        self.coordinates = coordinates


