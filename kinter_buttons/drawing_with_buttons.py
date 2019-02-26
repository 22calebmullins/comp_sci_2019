import tkinter as tk
import turtle
t = turtle.Pen()
t.speed(100)

            
def draw_a_square():
    for x in range (1000):
                t.forward(x)
                t.left(91)

def draw_a_circle():
    for x in range (1000):
                t.forward(x)
                t.left(60)

def draw_a_tringle():
    for x in range (1000):
                t.forward(x)
                t.left(120)


                
def make_it_blue():
    t.pencolor("blue")

def make_it_red():
    t.pencolor("red")
def make_it_green():
    t.pencolor("green")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

###color buttons
blue_button = tk.Button(frame, 
                   text="Blue", 
                   fg="blue",
                   command=make_it_blue)
blue_button.pack(side=tk.LEFT)
red_button = tk.Button(frame, 
                   text="Red", 
                   fg="red",
                   command=make_it_red)
red_button.pack(side=tk.LEFT)

green_button = tk.Button(frame, 
                   text="green", 
                   fg="green",
                   command=make_it_green)
green_button.pack(side=tk.LEFT)

###shape buttons
square_button = tk.Button(frame, 
                   text="square", 
                   fg="green",
                   command=draw_a_square)
square_button.pack(side=tk.LEFT)

circle_button = tk.Button(frame, 
                   text="circle", 
                   fg="green",
                   command=draw_a_circle)
circle_button.pack(side=tk.LEFT)
tringle_button = tk.Button(frame, 
                   text="tringe", 
                   fg="green",
                   command=draw_a_tringle)
tringle_button.pack(side=tk.LEFT)

quit_button = tk.Button(frame,
                   text="Quit",
                   command=quit)
quit_button.pack(side=tk.LEFT)

root.mainloop()


