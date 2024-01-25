from src.ui.in_game_ui import point_roster_page
import src.ui.Point as Point


def pick_point_roster(parent_frame):
    curr_point = Point.Point()
    point_roster_page(parent_frame, 1, curr_point)
