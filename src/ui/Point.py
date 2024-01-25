class Point:
    def __init__(self):
        self.point_roster = []
        self.coordinates = []
        self.unscaled_coordinates = []

    def get_point_roster(self):
        return self.point_roster

    def set_point_roster(self, point_roster):
        self.point_roster = point_roster

    def get_point_coordinates(self):
        return self.coordinates

    def add_point_coordinates(self, coordinates):
        self.coordinates.append(coordinates)

    def remove_point_coordinates(self):
        self.coordinates.pop()

    def get_unscaled_point_coordinates(self):
        return self.unscaled_coordinates

    def add_unscaled_point_coordinates(self, coordinates):
        self.unscaled_coordinates.append(coordinates)

    def remove_unscaled_point_coordinates(self):
        self.unscaled_coordinates.pop()
