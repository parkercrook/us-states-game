import turtle
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)
score = 0
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
correct_guesses = []
game_is_on = True

while game_is_on:

    # Convert guess to title case
    answer = turtle.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()

    # Check if the guess is among the 50 states
    data = pandas.read_csv("50_states.csv")
    if data.state.isin([answer]).any():
        # Check if correct guess is already guessed
        if answer not in correct_guesses:
            # Write correct guesses on to the map
            score += 1
            x = data[data["state"] == answer]["x"].item()
            y = data[data["state"] == answer]["y"].item()
            writer.goto(x, y)
            writer.write(arg=answer, align="center")
            correct_guesses.append(answer)

    # Check game end
    if len(correct_guesses) == 50:
        game_is_on = False

screen.exitonclick()