from src.ui.shared_ui import create_left_frame, create_point_roster_selector, clear_frames, create_right_frame, create_button, create_searchable_listbox, make_vert_radio_button, create_option_menu
import tkinter as tk
from Enums.wind import WindDirection
from Enums.throw import ThrowType, ThrowSubtype, ThrowForce, ThrowAspirations, ThrowDecision, ComingOutOfTimeout
import src.ui.Point as Point
import src.csvFileCreators.throwing as Throw
from src.ui.maintain_field import insert_field, delete_last_point, redraw_field


# page for picking the point roster and the wind direction and the starting line
def point_roster_page(parent_frame, curr_point, curr_throw):
    clear_frames(parent_frame)
    # create frame for the buttons
    right_frame = create_right_frame(parent_frame)

    # create selector for point roster
    create_point_roster_selector(right_frame, "C:\\Users\\jtscl\\PycharmProjects\\TUFF-Analytics-24\\Rosters\\tuff.csv", curr_point)
    # select wind direction for point as well as starting line
    wind_direction_options = [wind_direction.name for wind_direction in WindDirection]
    wind_direction_var = make_vert_radio_button(right_frame, wind_direction_options, "Wind Direction", 2, 2, 2, 1)

    # select Starting Line
    # REPLACE WITH THE ACTUAL ENUM
    starting_line_options = ["O-Line", "D-Line"]
    starting_line_var = make_vert_radio_button(right_frame, starting_line_options, "Starting Line", 0, 2, 2, 1)

    # should add this
    #  or curr_point.get_wind_direction() == "" or curr_point.get_starting_line() == ""
    def check_point_roster():
        # if (len(curr_point.get_point_roster()) < 7 or len(curr_point.get_point_roster()) > 8):
        #     donothing = 0
        # else:
        choose_point_and_thrower(parent_frame, curr_point, curr_throw)
    # if its the first time we are on this page for this game, we shouldn't have a back button
    # if its not the first time, we should have a back button that goes to the previous page
    create_button(right_frame, "Next", check_point_roster, 5, 2, 1, 1)

    # should only work if this is not the first point of the game
    back_button = create_button(right_frame, "Back", lambda: right_frame.destroy(), 5, 1, 1, 1)


# page where you choose the thrower and the point on the field where they throw from
def choose_point_and_thrower(parent_frame, curr_point, curr_throw):
    clear_frames(parent_frame)
    left_frame = create_left_frame(parent_frame)
    right_frame = create_right_frame(parent_frame)

    # put field on the left frame
    canvas, scalex, scaley = insert_field(left_frame, curr_point)
    redraw_field(canvas, curr_point)

    # create delete last point button
    create_button(left_frame, "Delete Last Point", lambda: delete_last_point(canvas, curr_point, scalex, scaley), 0, 1, 1, 1)

    # create selector for thrower
    thrower_options = curr_point.get_point_roster()
    if curr_throw.get_action_beginner() == "":
        default = "Thrower"
    else:
        default = curr_throw.get_action_beginner()
    create_option_menu(right_frame, thrower_options, default,
                       lambda selection: curr_throw.set_action_beginner(selection), 0, 0,
                       1, 2)

    # create go back button
    # TIME NEEDS TO BE RELATIVE TO THE POINT NUMBER WE ARE ON
    create_button(right_frame, "Back", lambda: point_roster_page(parent_frame, curr_point, curr_throw), 2, 0, 1, 1)

    def go_to_throw_info_page():
        if curr_throw.get_action_beginner() != "":
            throw_info_page(parent_frame, curr_point, curr_throw)


    # create next button
    create_button(right_frame, "Next", go_to_throw_info_page, 2, 1, 1, 1)


# page where you describe the throw information
def throw_info_page(parent_frame, curr_point, curr_throw):
    clear_frames(parent_frame)
    right_frame = create_right_frame(parent_frame)

    # select throw subtype
    throw_subtype_options = [throw_subtype.name for throw_subtype in ThrowSubtype]
    throw_subtype_var = make_vert_radio_button(right_frame, throw_subtype_options, "Throw Subtype", 0, 2, 2, 1)

    # select throw type
    throw_type_options = [throw_type.name for throw_type in ThrowType]
    throw_type_var = make_vert_radio_button(right_frame, throw_type_options, "Throw Type", 0, 1, 2, 1)

    # select throw force
    throw_force_options = [throw_force.name for throw_force in ThrowForce]
    throw_force_var = make_vert_radio_button(right_frame, throw_force_options, "Throw Force", 0, 3, 2, 1)

    # select throw aspirations
    throw_aspirations_options = [throw_aspirations.name for throw_aspirations in ThrowAspirations]
    throw_aspirations_var = make_vert_radio_button(right_frame, throw_aspirations_options, "Throw Aspirations", 0, 4, 2, 1)

    # select throw decision
    throw_decision_options = [throw_decision.name for throw_decision in ThrowDecision]
    throw_decision_var = make_vert_radio_button(right_frame, throw_decision_options, "Throw Decision", 0, 5, 2, 1)

    # select coming out of timeout
    coming_out_of_timeout_options = [coming_out_of_timeout.name for coming_out_of_timeout in ComingOutOfTimeout]
    coming_out_of_timeout_var = make_vert_radio_button(right_frame, coming_out_of_timeout_options, "Coming Out of Timeout", 0, 6, 2, 1)

    # create back button
    create_button(right_frame, "Back", lambda: choose_point_and_thrower(parent_frame, curr_point, curr_throw), 2, 1, 1, 1)

