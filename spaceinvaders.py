import turtle
import os
import math
import random

main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.title("Space Invaders Game")
main_screen.screen.bgpic("background3.gif")
main_screen.done()


#Border 
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup() 
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle() 

#Scoring system
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False , align="left", font=("Arial", 14, "normal"))


#Create player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)


#Choosing number of invaders
number_of_invaders = 5
#Create an empty list
invaders = []

#Add invaders to the list
for i in range(number_of_invaders):
    invaders.append(turtle.Turtle())



#Creating the Invaders
for invader in invaders:
    invader.color("red")
    invader.shape("circle")
    invader.penup()
    invader.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    invader.setposition(x, y)

invaderspeed = 2


#Create the players weapon
weapon = turtle.Turtle()
weapon.color("yellow")
weapon.shape("triangle")
weapon.penup()
weapon.speed(0)
weapon.setheading(90)
weapon.shapesize(0.5, 0.5)
weapon.hideturtle()

weaponspeed = 20

#Defining the weapon
weaponstate = "ready"


#Making the player move
playerspeed = 15
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare weapon as a global variable
    global weaponstate
    if weaponstate == "ready":
        weaponstate = "fire"
        #Moving the weapon above the player
        x = player.xcor()
        y = player.ycor() + 10
        weapon.setposition(x ,y)
        weapon.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2)+math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 15: 
        return True;
    else:
        return False



#Creating keyboard binds
turtle.listen()
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(fire_bullet, "space")


#Main Loop
while True:
    for invader in invaders:

        #Moving the Invaders
        x = invader.xcor()
        x += invaderspeed
        invader.setx(x)

         #Stopping the invaders from going off screen
        if invader.xcor() > 280:
            for e in invaders:
                y = e.ycor()
                y -= 40        
                e.sety(y)
            invaderspeed *= -1

        if invader.xcor() < -280:
            for e in invaders:
                y = e.ycor()
                y -= 40
                e.sety(y)
            invaderspeed *= -1
        #Che ck for collision between the weapon and invader
        if isCollision(weapon, invader):
            #reset the weapon
            weapon.hideturtle()
            weaponstate = "ready"
            weapon.setposition(0, -400)

            #reset the invader
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            invader.setposition(x, y)

            #Update the score
            score += 1
            scorestring = "Score: %s"  %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, invader):
            player.hideturtle()
            invader.hideturtle() 
            print ("Game Over")
            break

    #Move the weapon
    if weaponstate == "fire":
        y = weapon.ycor()
        y += weaponspeed
        weapon.sety(y)

    #Border checking the weapon
    if weapon.ycor() > 275:
        weapon.hideturtle()
        weaponstate = "ready"
    
    







 






delay =  input("press enter to finish.")    #creates a delay and user input is required to exit the program