import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"

screen.addshape(img)
turtle.shape(img)

user_guess = 0

state_data = pandas.read_csv("50_states.csv")
all_states = state_data["state"].to_list()
guessed_state = []

game_is_on = True

while game_is_on:
    answer_box = screen.textinput(title=f"{user_guess}/50 States", prompt="What's another states name?").title()
    answer_state = state_data[state_data["state"] == answer_box]
    state_name = answer_state["state"]
    state_x = answer_state["x"]
    state_y = answer_state["y"]
    for state in all_states:
        if state == answer_box:
            guessed_state.append(state)
            user_guess += 1
            turtle2 = turtle.Turtle()
            turtle2.ht()
            turtle2.up()
            turtle2.goto(int(state_x), int(state_y))
            turtle2.write(f"{state}")

    if user_guess == 50:
        game_is_on = False
    elif answer_box == "Exit":
        game_is_on = False
        missing_states = []

        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
screen.exitonclick()
