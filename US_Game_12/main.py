import turtle
import pandas

#create background gif
screen=turtle.Screen()
screen.title("U.S. States Game")
image="./day_25/US_Game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#find coordinats x,y
'''
def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
'''

#convert csv to list
data=pandas.read_csv("./day_25/US_Game/50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while(len(guessed_states) < 50):
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                prompt="What's another state's name?").title()
    #If you want to exit,csv which include unguessed states, are created
    if(answer_state=="Exit"):
        unguessed_states=[]
        for state in all_states:
            if state not in guessed_states:
                unguessed_states.append(state)
        new_data=pandas.DataFrame(unguessed_states)
        new_data.to_csv("./day_25/US_Game/states_to_learn.csv")
        break
    #If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[answer_state == data.state]
        t.goto(int(state_data.x),int(state_data.y))
        # t.write(state_data.state.item())
        # or use this
        t.write(answer_state)


screen.exitonclick()




