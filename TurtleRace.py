import turtle as t
import random

race_on = True
turtle_list = []
screen = t.Screen()
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
y = -150
tur_color = ["green", "purple", "blue", "red", "pink", "orange"]
for tur in range(6):
    new_turtle = t.Turtle("turtle")
    new_turtle.color(tur_color[tur])
    new_turtle.up()
    new_turtle.goto(-230, y)
    y += 60
    turtle_list.append(new_turtle)

if user_bet:
    race_on = True

x = -230
while race_on:
    if x > 230:
        winner = new_turtle.fillcolor()
        print(f"The {winner} turtle wins!")
        print(f"You chose the {user_bet} turtle.")
        if user_bet == winner:
            print("Your turtle won!")
        else:
            print("You lose.")
        race_on = False
    new_turtle = random.choice(turtle_list)
    new_turtle.forward(random.randint(0,10))
    x = new_turtle.xcor()

screen.exitonclick()
