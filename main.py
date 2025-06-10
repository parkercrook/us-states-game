import turtle
from score_manager import ScoreManager
from writer import Writer
from csv_helper import CsvHelper

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)
score_manager = ScoreManager()
writer = Writer()
csv_helper = CsvHelper()

while not score_manager.game_won():

    # Convert guess to title case
    answer = turtle.textinput(title=f"{score_manager.score}/50 States Correct", prompt="What's another state name?").title()

    # Check player exit
    if answer == "Exit":
        break

    # Check if the guess is among the 50 states
    if csv_helper.state_exists(answer):
        # Check if correct guess is already guessed
        if answer not in score_manager.correct_guesses:
            # Write correct guesses on to the map
            score_manager.add_point(answer)
            writer.write_answer(answer)

csv_helper.create_missing_states_csv(score_manager.correct_guesses)
