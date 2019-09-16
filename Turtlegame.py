#Kyle Seto
#03/04/2017
#ICS201-01
#Cope, D
#Turtlegame.py

import turtle, random, pyaudio, wave, time
screen = turtle.Screen()
screen.screensize(580,580,'lightblue')

P1 = turtle.Turtle()
P1.ht()
P1.color("turquoise2")
P1.pu()
P1.goto(75,-220)
P1.shapesize(2,2,2)
P1.left(90)
P1.st()


P2 = turtle.Turtle()
P2.ht()
P2.color("turquoise2")
P2.pu()
P2.goto(-75,-220)
P2.shapesize(2,2,2)
P2.left(90)
P2.st()


P3 = turtle.Turtle()
P3.ht()
P3.left(90)
P3.color("red")
P3.st()
P3.pu()
while(True):
        def forward():
                P3.fd(20)
        def left():
                P3.left(22.5)
        def right():
                P3.right(22.5)
        def backward():
                P3.back(20)
                
        screen.onkey(forward,"Up")
        screen.onkey(left,"Left")
        screen.onkey(right,"Right")
        screen.onkey(backward,"Down")

        screen.listen()

        if P2.distance(P3)>400:
                P2.left(P2.towards(P3)-P2.heading())
                P2.fd(400)
        elif P2.distance(P3)>300:
                P2.left(P2.towards(P3)-P2.heading())
                P2.fd(300)
        elif P2.distance(P3)>200:
                P2.left(P2.towards(P3)-P2.heading())
                P2.fd(200)
        elif P2.distance(P3)>100:
                P2.left(P2.towards(P3)-P2.heading())
                P2.fd(100)
        elif P2.distance(P3)>50:
                P2.left(P2.towards(P3)-P2.heading())
                P2.fd(50)
