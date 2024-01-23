class CoordinatesResults:
    def __init__(self, coordinates_list, event_list):
        self.coordinates_list = coordinates_list
        self.event_list = event_list

    def get_coordinates_list(self):
        return self.coordinates_list

    def set_coordinates_list(self, value):
        self.coordinates_list = value

    def get_event_list(self):
        return self.event_list

    def set_event_list(self, value):
        self.event_list = value

    def check_kaching(self):
        # return true if the coordinates list contains both an x value less than 10 and an x
        # value greater than 30
        if len(self.get_coordinates_list()) < 2:
            return False
        x_values = [coordinate[0] for coordinate in self.coordinates_list]
        if min(x_values) < 10 and max(x_values) > 30:
            return True
        else:
            return False

    def calculate_ho_distance(self):
        x1, y1 = self.get_coordinates_list()[-2]
        x2, y2 = self.get_coordinates_list()[-1]
        return round(abs(x2 - x1), 1)

    def calculate_vert_distance(self):
        x1, y1 = self.get_coordinates_list()[-2]
        x2, y2 = self.get_coordinates_list()[-1]
        return round(y2 - y1, 1)

    def calculate_total_distance(self):
        # return the distance between the last two points in the coordinates list
        x1, y1 = self.get_coordinates_list()[-2]
        x2, y2 = self.get_coordinates_list()[-1]
        return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5, 1)

    # calculate the row of the most recent coordinate
    def calculate_row(self):
        # checking to see what section the last y coordinate is in
        if self.get_coordinates_list()[-1][1] <= 0:
            return '1'
        elif self.get_coordinates_list()[-1][1] <= 20:
            return '2'
        elif self.get_coordinates_list()[-1][1] <= 35:
            return '3'
        elif self.get_coordinates_list()[-1][1] <= 50:
            return '4'
        elif self.get_coordinates_list()[-1][1] <= 70:
            return '5'
        elif self.get_coordinates_list()[-1][1] <= 90:
            return '6'

    # calculate the column of the most recent coordinate
    def calculate_column(self, num_sections):
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        for i in range(num_sections):
            # checking to see what section the last x coordinate is in
            if self.get_coordinates_list()[-1][0] <= (i + 1) * 40 / num_sections:
                return letters[i]
