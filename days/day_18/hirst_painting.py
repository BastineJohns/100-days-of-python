import colorgram
import turtle as t
import random

t.colormode(255)
colors = colorgram.extract(r'days\day_18\image.avif', 12)
tim = t.Turtle()

color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))
tim.penup()

filtered_colors = [color for color in color_list if not all(value>235 for value in color)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

for j in range(10):
    for i in range(10):

        tim.dot(20, random.choice(filtered_colors))
        
        tim.forward(50)

    
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()