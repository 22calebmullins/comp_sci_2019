
import turtle
t = turtle.Pen()
t.speed(100)
def left_spiral():
    for x in range (200):
        t.pencolor("black")
        t.forward(x)
        t.left(91)

def right_spiral():
    for x in range (200):
        t.pencolor("purple")
        t.forward(x)
        t.right(91)


while True:
    drawing = input("""What would you like to draw?
    1 a left spiral 
    2 a right spiral""")
    if drawing == "1":
        left_spiral()
    if drawing == "2":
        right_spiral()
