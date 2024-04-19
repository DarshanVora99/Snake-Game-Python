from turtle import *
import time
import random

score = 0
# Creating game window
gamewindow = Screen()
gamewindow.setup(width=800, height=800)

# Giving tittle to our game

gamewindow.title("Snake Game Pbl ")
gamewindow.tracer(False)


# Background colour
gamewindow.bgcolor('white')

# Adding images for our game
gamewindow.addshape('upmouth.gif')
gamewindow.addshape('downmouth.gif')
gamewindow.addshape('leftmouth.gif')
gamewindow.addshape('rightmouth.gif')
gamewindow.addshape('body.gif')
gamewindow.addshape('appple.gif')
gamewindow.addshape('background.gif')

background = Turtle()
background.shape('background.gif')
background.forward(10)
# Creating head of our snake

snk_head = Turtle()
snk_head.penup()
snk_head.goto(0, 100)
snk_head.direction = 'stop'
snk_head.shape('upmouth.gif')


snk_food = Turtle()
snk_food.shape('appple.gif')
snk_food.penup()



# food_x = snk_food.xcor()
# food_y = snk_food.ycor()

food_x = random.randint(-250 , 250)
food_y = random.randint(-250 , 250)
snk_food.goto(food_x,food_y)

text = Turtle()
text.penup()
text.goto(-50,370)
# text.write('score:', font=('courier',25,'bold'))
text.hideturtle()

lost = Turtle()
lost.penup()
lost.hideturtle()



def move_snake():
    if snk_head.direction=='Up':
        #This retyurns Y co-ordinate of snake head
        y=snk_head.ycor()
        y=y+20
        snk_head.sety(y)

    if snk_head.direction=='Down':
        #This retyurns Y co-ordinate of snake head
        y=snk_head.ycor()
        y=y-20
        snk_head.sety(y)

    if snk_head.direction == 'Right':

        #This returns X co-ordinate of snake head

        x = snk_head.xcor()
        x=x+20
        snk_head.setx(x)

    if snk_head.direction == 'Left':
        #This returns X co-ordinate of snake head
        x = snk_head.xcor()
        x = x - 20
        snk_head.setx(x)


def go_up():
    if snk_head.direction!='Down':
        snk_head.direction='Up'
        snk_head.shape('upmouth.gif')


def go_down():
    if snk_head.direction != 'Up':
        snk_head.direction='Down'
        snk_head.shape('downmouth.gif')


def go_left():
    if snk_head.direction != 'Right':
        snk_head.direction='Left'
        snk_head.shape('leftmouth.gif')


def go_right():
    if snk_head.direction != 'Left':
        snk_head.direction='Right'
        snk_head.shape('rightmouth.gif')


gamewindow.listen()

gamewindow.onkeypress(go_up,'Up')
gamewindow.onkeypress(go_down,'Down')
gamewindow.onkeypress(go_left,'Left')
gamewindow.onkeypress(go_right,'Right')

snake_list =[]
while True:
    if abs(food_x-snk_head.xcor())<20 and abs(food_y-snk_head.ycor())<20:
        food_x = random.randint(-250, 250)
        food_y = random.randint(-250, 250)
        snk_food.goto(food_x, food_y)

        body=Turtle()
        body.penup()
        body.shape('body.gif')
        snake_list.append(body)

        score = score+10
        text.clear()
        text.write(f"Score:{score}",font=('courier',25,'bold'),align='center')

    if snk_head.xcor()>370 or snk_head.xcor()<-370 or snk_head.ycor()>370 or snk_head.ycor()<-370:
        lost.write('Game lost',align='center',font=('courier',40,'bold'))
        
        time.sleep(1)
        lost.clear()
        time.sleep(1)
        snk_head.goto(0,0)
        snk_head.direction='stop'
        score=0


        for body in snake_list:
            body.goto(1000,1000)

        snake_list.clear()
        text.clear()

    for i in range(len(snake_list)-1,0,-1):
        x=snake_list[i-1].xcor()
        y=snake_list[i-1].ycor()
        snake_list[i].goto(x,y)

    if len(snake_list)>0:
        x=snk_head.xcor()
        y=snk_head.ycor()
        snake_list[0].goto(x,y)

    move_snake()

    for body in snake_list:
        if body.distance(snk_head)<20:
            lost.write('Game lost', align='center', font=('courier', 40, 'bold'))
            time.sleep(1)
            lost.clear()
            time.sleep(1)
            snk_head.goto(0, 0)
            snk_head.direction = 'stop'
            score = 0

            for body in snake_list:
                body.goto(1000, 1000)

            snake_list.clear()

            text.clear()

    # Increasing the speed of our snake as score increases

    speed_increase = 0.011

    if score > 300:

        time.sleep(0.063 - speed_increase)
    else :
        time.sleep(0.063)

    gamewindow.update()



