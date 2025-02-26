import turtle as t
import random

tim = t.Turtle()
tim.shape("circle")
tim.color("black")
t.colormode(255)

colors = ["blue", "lime green", "navy", "dark red", "peru", "chartreuse", "olive drab", "deep pink", "dim gray", "black"]
direction = [0,90,180,90,90,90,45]

def dashed_lines():
   for i in range(15):
        tim.forward(10)
        tim.color("white")
        tim.forward(10)
        tim.color("black")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def shape_drawer(n_sides):
    for i in range(n_sides):
        tim.forward(100)
        tim.right(360/n_sides)
tim.pensize(1)        
"""for i in range(100):
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(direction))"""
"""for i in range(3,11):
    tim.color(random.choice(colors))
    shape_drawer(i)"""
"""tim.speed("fastest")
tim.color(random_color())
tim.circle(100)
current_heading = tim.heading()
tim.circle(100)
print(tim.heading())"""

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.speed("fastest")
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(1)


screen = t.Screen()
screen.exitonclick()

   
