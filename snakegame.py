import turtle
turtle.shapesize(1,1)
turtle.penup()
turtle.speed(0.5)
turtle.shape("square")
tx=turtle.xcor()
ty=turtle.ycor()
def up():
    turtle.direction="Up"
    if turtle.direction=="Up":
        turtle.goto(tx,ty+20)
        print("you pressed the up key!")
turtle.onkeypress(up,"w")

def down():
    turtle.direction="Down"
    if turtle.direction=="Down":
    turtle.goto(tx,ty-20)
    print("you pressed the down key!")
turtle.onkeypress(up,"s")

def left():
    turtle.direction="Left"
    if turtle.direction=="Left":
    turtle.goto(tx-20,ty)
    print("you pressed the left key!")
turtle.onkeypress(up,"a")

def right():
    turtle.direction="Right"
    elif turtle.direction=="Right":
    turtle.goto(tx+20,ty)
    print("you pressed the right key!")
turtle.onkeypress(up,"d")
turtle.listen()



turtle.mainloop()
    
    


