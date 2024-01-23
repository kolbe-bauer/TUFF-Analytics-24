class Shared:
    def __init__(self, point_number: int, possession_number: int, throw_number: int):
        self.point_number = point_number
        self.possession_number = possession_number
        self.throw_number = throw_number

    def add_point_number(self):
        self.point_number = self.get_point_number() + 1

    def get_point_number(self):
        return self.point_number

    def add_possession_number(self, value):
        self.possession_number = self.get_possession_number() + 1

    def get_possession_number(self):
        return self.possession_number

    def add_throw_number(self, value):
        self.throw_number = self.get_throw_number() + 1

    def get_throw_number(self):
        return self.throw_number
