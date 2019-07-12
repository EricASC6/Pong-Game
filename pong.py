# Pong Game OPP

import turtle

# Window
class Window():
    '''Creates a window for the game'''
    def __init__(self, color, title, width, height):
        self.color = color
        self.title = title
        self.width = int(width)
        self.height = int(height)
        self.screen = turtle.Screen()

    def display_screen(self):
        '''Displays the screen object'''
        self.screen.bgcolor(self.color)
        self.screen.title(self.title)
        self.screen.setup(width = self.width, height = self.height)
        self.screen.tracer(0)

    def end_game(self):
        wn.screen.bye()



wn = Window("black", "Pong", 800, 600)
wn.display_screen()

# Paddle Class
class Paddle(turtle.Turtle):
    '''Creates the paddles for the game'''
    def __init__(self, x, y, color, window, name):
        super().__init__()
        self.x = x
        self.y = y 
        self.color = color
        self.window = window
        self.name = name
        self.paddle = turtle.Turtle()

    def draw_paddle(self):
        '''Displays the paddle object'''
        self.paddle.speed(0)
        self.paddle.color(self.color)
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle.penup()
        self.paddle.goto(self.x, self.y)

    def paddle_up(self):
        '''Method to move paddle up'''
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def paddle_down(self):
        '''Method to move paddle down'''
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)


# Paddle A
paddle_a = Paddle(-350, 0, "white", wn, "Paddle A")
paddle_a.draw_paddle()


# Paddle B
paddle_b = Paddle(350, 0, "white", wn, "Paddle B")
paddle_b.draw_paddle()



# Ball
class Ball(turtle.Turtle):
    '''Creates the ball for the game'''
    def __init__(self, color, *paddles):
        super().__init__()
        self.color = color
        self.shape = "square"
        self.initx = 0
        self.inity = 0
        self.dx = 2
        self.dy = 2
        self.ball = turtle.Turtle()
        self.paddles = paddles
        
    def display_ball(self):
        '''Displays ball object on screen'''
        self.ball.speed(0)
        self.ball.color(self.color)
        self.ball.shape(self.shape)
        self.ball.penup()
        self.ball.goto(self.initx, self.inity)
    
    def move_ball(self):
        '''Moves the ball object'''
        x = self.ball.xcor()
        y = self.ball.ycor()
        x += self.dx
        y += self.dy
        self.ball.setx(x)
        self.ball.sety(y)

    def check_border_collision(self):
        '''Checks for any border collisions and if there is, causes the ball to bounce off the border'''
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.dy *= -1
        elif self.ball.xcor() > 390:
            self.ball.goto(self.initx, self.inity)
        elif self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.dy *= -1
        elif self.ball.xcor() < -390:
            self.ball.goto(self.initx, self.inity)

    def check_paddle_collision(self):
        '''Checks for paddle collison and if there is, causes the ball to bounce off the paddle'''
        paddle_coordinates = {}
        for paddle in self.paddles:
            paddle_coordinates[paddle.name] = (paddle.paddle.xcor(), paddle.paddle.ycor())
       
        for coordinates in paddle_coordinates.values():
            if (self.ball.xcor() > 340 and self.ball.xcor() < coordinates[0] and self.ball.ycor() < coordinates[1] + 50 and self.ball.ycor() > coordinates[1] - 50) or (self.ball.xcor() < -340 and self.ball.xcor() > coordinates[0] and self.ball.ycor() < coordinates[1] + 50 and self.ball.ycor() > coordinates[1] - 50):
                self.dx *= -1



game_ball = Ball("white", paddle_a, paddle_b)
game_ball.display_ball()


# Pen
class Score(turtle.Turtle):
    '''Score keeper'''
    def __init__(self, color, ball):
        super().__init__()
        self.pen = turtle.Turtle()
        self.color = color
        self.paddle_a_score = 0
        self.paddle_b_score = 0
        self.ball = ball

    def display_score(self):
        score = "Player A: {}, Player B: {}".format(self.paddle_a_score, self.paddle_b_score)
        self.pen.speed(0)
        self.pen.color(self.color)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write(score, align = "center", font = ("Courier", 24, "normal"))

    def update_score(self):
        if self.ball.ball.xcor() > 350:
            self.ball.ball.goto(0,0)
            self.paddle_a_score += 1
            self.pen.clear()
            score = "Player A: {}, Player B: {}".format(self.paddle_a_score, self.paddle_b_score)
            self.pen.write(score, align = "center", font = ("Courier", 24, "normal"))
    
        elif self.ball.ball.xcor() < -350:
            self.ball.ball.goto(0,0)
            self.paddle_b_score += 1
            self.pen.clear()
            score = "Player A: {}, Player B: {}".format(self.paddle_a_score, self.paddle_b_score)
            self.pen.write(score, align = "center", font = ("Courier", 24, "normal"))
    


score = Score("white", game_ball)
score.display_score()

# Keyboard binding
wn.screen.listen()
paddle_a.window.screen.onkeypress(paddle_a.paddle_up, "w")
paddle_a.window.screen.onkeypress(paddle_a.paddle_down, "s")
paddle_b.window.screen.onkeypress(paddle_b.paddle_up, "Up")
paddle_b.window.screen.onkeypress(paddle_b.paddle_down, "Down")


# Main Game Loop
run_game = True
while run_game:
    wn.screen.update() # Updates the screen 
    

    game_ball.move_ball() # Moves the ball
    game_ball.check_border_collision() # Checks border collision
    game_ball.check_paddle_collision() # Checks paddle collision

    score.update_score()

    wn.screen.onkeypress(wn.end_game, "q")

