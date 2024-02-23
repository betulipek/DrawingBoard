import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)
def turtle_angle_right():
    #turtle_instance.right(90)
    turtle_instance.setheading(turtle_instance.heading()-10)
def turtle_angle_left():
    turtle_instance.left(90)

def clear_screen():
    turtle_instance.clear()

def turtle_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()



drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=turtle_angle_right, key="Up")
drawing_board.onkey(fun=turtle_angle_left, key="Down")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=turtle_home, key="Home")
drawing_board.onkey(fun=turtle_pen_up, key="A")
drawing_board.onkey(fun=turtle_pen_down, key="K")

turtle.mainloop()
#turtle.done()