import turtle
import random
turtle.tracer(1,0)
squaresize=20
startlength=6
timestep=100
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]
snake=turtle.clone()
snake.shape("square")
turtle.hideturtle()


snake.penup()
def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos)       
    stampid= snake.stamp()     
    stamp_list.append(stampid)
    
for i in range(6):
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]

    x_pos+=squaresize

    snake.goto(x_pos,y_pos) 
   
    new_stamp()
def remove_stamp():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position


def up():
    snake.direction="Up"
    move_snake()
    print("you pressed the up key!")
turtle.onkeypress(up,"w")

def down():
    snake.direction="Down"
    move_snake()
    print("you pressed the down key!")
turtle.onkeypress(down,"s")

def left():
    snake.direction="Left"
    move_snake()
    print("you pressed the left key!")
turtle.onkeypress(left,"a")

def right():
    snake.direction="Right"
    move_snake()
    print("you pressed the right key!")
turtle.onkeypress(right,"d")

turtle.listen()

def move_snake():
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]
    tx=snake.xcor()
    ty=snake.ycor()
    
    if snake.direction=="Up":
        snake.goto(x_pos,y_pos+20)
    if snake.direction=="Down":
        snake.goto(x_pos,y_pos-20)
    if snake.direction=="Left":
        snake.goto(x_pos-20,y_pos)
    if snake.direction=="Right":
        snake.goto(x_pos+20,y_pos)





turtle.mainloop()
    
    


