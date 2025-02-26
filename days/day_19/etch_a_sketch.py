from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def forward():
    tim.forward(100)

def backward():
    tim.backward(100)

def clockwise():
    tim.right(15)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def counterclockwise():
    tim.left(15)
screen.listen()
screen.onkey(key="w", fun = forward)       
screen.onkey(key="s", fun = backward) 
screen.onkey(key="a", fun = counterclockwise) 
screen.onkey(key="d", fun = clockwise)

screen.onkey(key="c", fun = clear)
screen.exitonclick()    
