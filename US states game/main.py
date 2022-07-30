import turtle
import pandas
from StateText import StateText

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_text = StateText()

coord_data = pandas.read_csv("50_states.csv")
score = 0
guessed_states = []
state_answer = screen.textinput("Guess the state: ", "What's another state's name ?").title()
while len(guessed_states) < 50:
    if state_answer == "Exit":
        missed_states = coord_data["state"].tolist()
        for state in guessed_states:
            if state in missed_states:
                missed_states.remove(state)
        study_dict = {
            "Missed States": missed_states
        }
        study_csv = pandas.DataFrame(study_dict)
        study_csv.to_csv("Missed_States.csv")
        break

    curr_row = coord_data[coord_data.state == state_answer]
    if not curr_row.empty:
        curr_state = curr_row["state"].tolist()
        curr_x = curr_row["x"].tolist()
        curr_y = curr_row["y"].tolist()
        score += 1
        state_text.write_state(curr_state[0], curr_x[0], curr_y[0])
        guessed_states.append(curr_state[0])
    state_answer = screen.textinput(f"{score}/50 states guessed", "What's another state's name ?").title()

screen.bye()








