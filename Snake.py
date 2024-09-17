import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game with Details and Restart")
wn.bgcolor("grey")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Tongue (triangle shape)
tongue = turtle.Turtle()
tongue.speed(0)
tongue.shape("triangle")
tongue.color("red")
tongue.penup()
tongue.shapesize(stretch_wid=0.2, stretch_len=0.5)  # Small triangle for tongue
tongue.hideturtle()

# Eyes
eye_left = turtle.Turtle()
eye_left.speed(0)
eye_left.shape("circle")
eye_left.color("white")
eye_left.penup()
eye_left.shapesize(stretch_wid=0.2, stretch_len=0.2)  # Small circles for eyes
eye_left.hideturtle()

eye_right = turtle.Turtle()
eye_right.speed(0)
eye_right.shape("circle")
eye_right.color("white")
eye_right.penup()
eye_right.shapesize(stretch_wid=0.2, stretch_len=0.2)  # Small circles for eyes
eye_right.hideturtle()

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Restart message turtle
restart_message = turtle.Turtle()
restart_message.speed(0)
restart_message.shape("square")
restart_message.color("white")
restart_message.penup()
restart_message.hideturtle()

# Functions to control direction
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Function to move the tongue in sync with the head
def move_tongue():
    tongue.showturtle()
    tongue.goto(head.xcor(), head.ycor())  # Place tongue at head position
    if head.direction == "up":
        tongue.setheading(90)  # Tongue pointing up
        tongue.sety(head.ycor() + 15)  # Slightly ahead of the head
    elif head.direction == "down":
        tongue.setheading(270)  # Tongue pointing down
        tongue.sety(head.ycor() - 15)
    elif head.direction == "left":
        tongue.setheading(180)  # Tongue pointing left
        tongue.setx(head.xcor() - 15)
    elif head.direction == "right":
        tongue.setheading(0)  # Tongue pointing right
        tongue.setx(head.xcor() + 15)

# Function to move the eyes in sync with the head
def move_eyes():
    eye_left.showturtle()
    eye_right.showturtle()
    if head.direction == "up":
        eye_left.goto(head.xcor() - 5, head.ycor() + 10)
        eye_right.goto(head.xcor() + 5, head.ycor() + 10)
    elif head.direction == "down":
        eye_left.goto(head.xcor() - 5, head.ycor() - 10)
        eye_right.goto(head.xcor() + 5, head.ycor() - 10)
    elif head.direction == "left":
        eye_left.goto(head.xcor() - 10, head.ycor() + 5)
        eye_right.goto(head.xcor() - 10, head.ycor() - 5)
    elif head.direction == "right":
        eye_left.goto(head.xcor() + 10, head.ycor() + 5)
        eye_right.goto(head.xcor() + 10, head.ycor() - 5)

# Function to add dark stripes to the snake's body
def add_stripes(segment):
    segment.penup()
    segment.color("green")  # Base color of the segment
    segment.goto(segment.xcor() - 10, segment.ycor())  # Position for the stripes
    segment.pendown()
    segment.color("darkgreen")
    segment.goto(segment.xcor() + 20, segment.ycor())  # Horizontal stripe
    segment.penup()
    segment.goto(segment.xcor() - 10, segment.ycor() - 5)
    segment.pendown()
    segment.goto(segment.xcor() + 20, segment.ycor())  # Another horizontal stripe
    segment.penup()

# Function to display restart message
def display_restart_message():
    restart_message.clear()
    restart_message.goto(0, 0)
    restart_message.write(f"Game Over\nScore: {score}\nPress Enter to Restart", align="center", font=("Courier", 24, "normal"))

# Function to restart the game
def restart_game():
    global score, delay
    score = 0
    delay = 0.1
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    pen.clear()
    pen.write("Score: 0  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    restart_message.clear()

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(restart_game, "Return")  # Restart the game with "Enter"

# Main game loop
while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        display_restart_message()

        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

   
    if head.distance(food) < 20:
        
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Add stripes to the new segment
        add_stripes(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    move_tongue()
    move_eyes()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            display_restart_message()

            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

    time.sleep(delay)

wn.mainloop()
