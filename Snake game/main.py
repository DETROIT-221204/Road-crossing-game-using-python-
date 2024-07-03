import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

Starting_positions = [
    (250, 250), (250, -100), (250, 0), (100, 90), (-100, 45),
    (-150, -50), (40, 40), (-65, 160), (190, 150), (300, 230)
]


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! Final Score: {self.score}", align="center", font=("Arial", 24, "normal"))


class TURT(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.goto(position)
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


class Car(Turtle):
    def __init__(self, position, speed):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.goto(position)
        self.speed = speed

    def move(self):
        new_x = self.xcor() - self.speed
        if new_x < -300:
            new_x = 300
        self.goto(new_x, self.ycor())



turtle = TURT((0, -270))
scoreboard = Scoreboard()


cars = []


initial_speed = 10
for position in Starting_positions:
    car = Car(position, initial_speed)
    cars.append(car)


screen.listen()
screen.onkey(turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # Move cars
    for car in cars:
        car.move()
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


    if turtle.ycor() > 280:
        turtle.goto(0, -270)
        scoreboard.increase_score()

        for car in cars:
            car.speed += 2

    # Update screen
    screen.update()

screen.exitonclick()