from src.ui.in_game_ui import point_roster_page
import src.ui.Point as Point
import src.csvFileCreators.throwing as Throw


def pick_point_roster(parent_frame):
    curr_point = Point.Point()
    curr_throw = Throw.Throw()
    point_roster_page(parent_frame, curr_point, curr_throw)
