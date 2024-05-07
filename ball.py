from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("firebrick2")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Ball doesn't change direction on x-axis on the y-axis it goes opposite hence 10 *-1 = -10
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.7
    #     increases the speed by decreasing the input on main.py time.sleep(self.move_speed)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

