from shared_ui import create_right_frame, create_button, create_searchable_listbox, make_radio_button
from Enums.wind import WindSpeed
from Enums.game import Bracket_Teams, Tournament, Studied_Teams


# method to create the start page with the load button and new game button
def load_new_game_page():
    # create frame for the buttons
    right_frame = create_right_frame()
    # create button to load game
    button_load_game = create_button(right_frame, "Load Game", load_game_page, 0, 0)

    # create button to start new game
    button_new_game = create_button(right_frame, "New Game", new_game_page, 1, 0)


# method to create the load game page
def load_game_page():
    # create load page
    right_frame = create_right_frame()
    # NEED TO MAKE THIS HAVE THE GAMES THAT HAVE BEEN SAVED
    games = [games.name for games in Bracket_Teams]
    # make a search box of all the games that have been saved
    entry_var_opponent, selected_opponent_var = create_searchable_listbox(right_frame, "Game", games, 0, 0)

    # create back button to go back to the start page
    create_button(right_frame, "Back", load_new_game_page, 1, 0)

    return selected_opponent_var

# method to create the new game page
def new_game_page():
    # create new game page
    right_frame = create_right_frame()

    # entry list for tournament
    tournaments = [tournaments.name for tournaments in Tournament]
    # make a search box of all Tournaments
    entry_var_tournament, selected_tournament_var = create_searchable_listbox(right_frame, "Tournament", tournaments, 0, 0)

    # entry list for team we are scouting
    studied_teams = [teams.name for teams in Studied_Teams]
    # make a search box for the team we are scouting
    entry_var_scouted, selected_scouted_var = create_searchable_listbox(right_frame, "Scouted Team", studied_teams, 1, 0)

    # entry list for team scouted team is playing
    opponents = [teams.name for teams in Bracket_Teams]
    # make a search box for the team scouted team is playing
    entry_var_opponent, selected_opponent_var = create_searchable_listbox(right_frame, "Opponent", opponents, 2, 0)

    # radio button for wind level
    wind_level_options = [wind.name for wind in WindSpeed]
    # make a radio button for the wind level
    wind_speed_var = make_radio_button(right_frame, "Wind Speed", wind_level_options, 3, 0)

    # create back button to go back to the start page
    create_button(right_frame, "Back", load_new_game_page, 4, 0)

    return [selected_tournament_var, selected_scouted_var, selected_opponent_var, wind_speed_var]
