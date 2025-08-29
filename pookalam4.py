import math
import turtle

# ---------- Setup ----------
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle for sunflower
tina = turtle.Turtle()
tina.shape("turtle")
tina.color("white")
tina.speed(0)

# Turtle for spiral square + text
t = turtle.Turtle()
t.speed(0)
t.pencolor("orange")

# ---------- Draw Petal ----------
def drawPetal(t, color, size):
    t.fillcolor(color)
    t.begin_fill()
    t.right(20)
    t.forward(size)
    t.left(40)
    t.forward(size)
    t.left(140)
    t.forward(size)
    t.left(40)
    t.forward(size)
    t.end_fill()

# ---------- Draw Sunflower ----------
def sunflower(t, numseeds, numpetals, angle, cspread, petal_size, petal_color, start_offset=0):
    phi = angle * (math.pi / 180.0)
    max_r = 0
    for i in range(numseeds + numpetals):
        r = cspread * math.sqrt(i + start_offset)
        theta = (i + start_offset) * phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        t.penup()
        t.goto(x, y)
        t.setheading(i * angle)
        t.pendown()

        if i < numseeds:
            t.stamp()
        else:
            drawPetal(t, petal_color, petal_size)

        if r + petal_size > max_r:
            max_r = r + petal_size

    return max_r  # return outermost radius

# ---------- Draw Square Spiral ----------
def square(size, angle):
    for _ in range(4):
        t.forward(size)
        t.right(angle)

def draw_spiral_centered(radius, steps=300):
    max_radius = radius
    for i in range(steps):
        t.penup()
        t.goto(0,0)  # center at same point as sunflower
        t.pendown()
        square(170, 90)
        t.right(5)
        t.circle(50)
        t.right(50)
        dist = t.distance(0,0)
        if dist > max_radius:
            max_radius = dist
    return max_radius

# ---------- Main Design ----------

# 1. Inner sunflower
inner_radius = sunflower(tina, numseeds=160, numpetals=40, angle=137.5, cspread=4, petal_size=70, petal_color="red")

# 2. Spiral square (centered on same point)
spiral_radius = draw_spiral_centered(inner_radius)

# 3. Outer sunflower (continuation of inner, around spiral)
outer_radius = sunflower(tina, numseeds=0, numpetals=22, angle=130.5, cspread=10, petal_size=90, petal_color="maroon", start_offset=160)

# 4. Greeting text
t.penup()
t.goto(0, -outer_radius - 50)
t.color("white")
t.write("🌸 Happy Onam 2025 🌸", align="center", font=("Arial", 22, "bold"))

# Hide turtles
tina.hideturtle()
t.hideturtle()
turtle.done()
