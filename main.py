import turtle
import pandas
import os
import string

"""Check if the file exists and remove it"""
if os.path.exists("states_to_learn.csv"):
    os.remove("states_to_learn.csv")

image = "./mx.gif"
screen = turtle.Screen()
screen.addshape(image)
screen.title("MX States Game")
screen.setup(width=1000, height=750)
turtle.shape(image)
guessed_states: list[str] = []

data = pandas.read_csv("./32_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 32:
    if len(guessed_states) == 0:
        title = "Guess the State"
        prompt = "Take a guess"
    else:
        title = f"{len(guessed_states)}/32 States Correct"
        prompt = "What's another state's name?"

    answer_state = screen.textinput(title, prompt)
    if answer_state:
        capitalized_answer = string.capwords(answer_state)
        if capitalized_answer == "Exit":
            break
        answer = data[data.state == capitalized_answer]
        if not answer.empty and capitalized_answer not in guessed_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(answer.x.item()), int(answer.y.item()))
            t.write(capitalized_answer)
            guessed_states.append(capitalized_answer)

# Write down a new file with the missing states
states_to_learn: list[str] = []
for state in all_states:
    if state not in guessed_states:
        states_to_learn.append(state)

data_dict = {"states": states_to_learn}
pandas.DataFrame(data_dict).to_csv("states_to_learn.csv")
