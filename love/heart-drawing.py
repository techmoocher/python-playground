# Importing necessary modules (packages)
import turtle
import time
import random
from math import sin, cos, pi, log
from tkinter import *


# Preparing for shining heart
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480
CANVAS_CENTER_X = CANVAS_WIDTH / 2
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2
IMAGE_ENLARGE = 11
HEART_COLOR = "#8A2BE2"

# Creating turtle screen
screen = turtle.Screen()

# Setting the Back Ground color
screen.bgcolor('black')

# Creating a turtle object (pen)
pen = turtle.Turtle()

# Setting turtle (pen) speed
pen.speed(10)

# Setting the fill color to pink and border color to Red
pen.color('red', 'purple')
screen.setup(width = 780, height = 500, startx = 200, starty = 100)

# Defining a method to draw curve
def curve():
    for i in range(200):
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)

# Defining method to draw a full heart
def heart():

    # Set the fill color to red
    pen.fillcolor('pink')

    # Start filling the color
    pen.begin_fill()

    # Draw the left line
    pen.left(140)
    pen.speed(5)
    pen.forward(113)

    # Draw the left curve
    curve()
    pen.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    pen.speed(5)
    pen.forward(112)

    # Ending the filling of the color
    pen.end_fill()

# Defining method to write text
def txt():
    # Move turtle to air
    pen.up()

    # Move turtle to a given position
    pen.setpos(-68, 95)

    # Move the turtle to the ground
    pen.down()

    # Set the text color to lightgreen
    pen.color('black')

    # Write the specified text in 
    # Specifying font style and size
    pen.write("I LOVE YOU", align = 'center', font=(
    "Verdana", 12, "bold"))

# Draw a heart
heart()
# Write text
txt()
# Hiding turtle
pen.ht()
time.sleep(0.5)



# Code for shining heart

def heart_function(t, shrink_ratio: float = IMAGE_ENLARGE):
    x = 16 * (sin(t) ** 3)
    y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))

    x *= shrink_ratio
    y *= shrink_ratio

    x += CANVAS_CENTER_X
    y += CANVAS_CENTER_Y

    return int(x), int(y)


def scatter_inside(x, y, beta=0.15):
  
    ratio_x = - beta * log(random.random())
    ratio_y = - beta * log(random.random())

    dx = ratio_x * (x - CANVAS_CENTER_X)
    dy = ratio_y * (y - CANVAS_CENTER_Y)

    return x - dx, y - dy


def shrink(x, y, ratio):
    
    force = -1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.6) 
    dx = ratio * force * (x - CANVAS_CENTER_X)
    dy = ratio * force * (y - CANVAS_CENTER_Y)
    return x - dx, y - dy


def curve(p):
    
    return 2 * (2 * sin(4 * p)) / (2 * pi)


class Heart:

    def __init__(self, generate_frame=20):
        self._points = set() 
        self._edge_diffusion_points = set()  
        self._center_diffusion_points = set() 
        self.all_points = {} 
        self.build(2000)

        self.random_halo = 1000

        self.generate_frame = generate_frame
        for frame in range(generate_frame):
            self.calc(frame)

    def build(self, number):
        for _ in range(number):
            t = random.uniform(0, 2 * pi) 
            x, y = heart_function(t)
            self._points.add((x, y))

        for _x, _y in list(self._points):
            for _ in range(3):
                x, y = scatter_inside(_x, _y, 0.05)
                self._edge_diffusion_points.add((x, y))

        point_list = list(self._points)
        for _ in range(4000):
            x, y = random.choice(point_list)
            x, y = scatter_inside(x, y, 0.17)
            self._center_diffusion_points.add((x, y))

    @staticmethod
    def calc_position(x, y, ratio):
        force = 1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.520)  

        dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)
        dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)

        return x - dx, y - dy

    def calc(self, generate_frame):
        ratio = 10 * curve(generate_frame / 10 * pi) 

        halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))

        all_points = []

        heart_halo_point = set()  
        for _ in range(halo_number):
            t = random.uniform(0, 2 * pi) 
            x, y = heart_function(t, shrink_ratio=11.6)  
            x, y = shrink(x, y, halo_radius)
            if (x, y) not in heart_halo_point:
                heart_halo_point.add((x, y))
                x += random.randint(-14, 14)
                y += random.randint(-14, 14)
                size = random.choice((1, 2, 2))
                all_points.append((x, y, size))

        for x, y in self._points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 3)
            all_points.append((x, y, size))

        for x, y in self._edge_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        for x, y in self._center_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        self.all_points[generate_frame] = all_points

    def render(self, render_canvas, render_frame):
        for x, y, size in self.all_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=HEART_COLOR)


def draw(main: Tk, render_canvas: Canvas, render_heart: Heart, render_frame=0):
    render_canvas.delete('all')
    render_heart.render(render_canvas, render_frame)
    main.after(160, draw, main, render_canvas, render_heart, render_frame + 1)

def center_window(width, height):
    # Getting screen width and height
    screen_width = root.winfo_screenwidth() # Width of the screen
    screen_height = root.winfo_screenheight() # Height of the screen

    # Calculating x and y coordinates to find where to place the Tk root window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    # Setting the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

if __name__ == '__main__':
    root = Tk()  
    canvas = Canvas(root, bg = 'black', height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
    canvas.pack()

    center_window(860, 650)

    heart = Heart()
    draw(root, canvas, heart)
    root.mainloop()