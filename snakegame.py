moves = []
full = []
#snake look
import turtle
import random
turtle.tracer(1,0)
squaresize=20
startlength=6
timestep=100
pos_list=[]
stamp_list=[]
food_pos = []
food_stamps=[]
gfuel_pos=[]
gfuel_stamps=[]
snake=turtle.clone()
snake.shape("square")
turtle.hideturtle()
snake.color("blue")
#pop up window

#title
title=turtle.clone()
title.penup()
title.goto(10,300)
title.color('red')
style = ('Courier', 30, 'italic')
title.write('!SNAKE GAME!', font=style, align='center')
turtle.hideturtle()

snake.direction = "Up"
UP_EDGE = 260
DOWN_EDGE = -260
RIGHT_EDGE = 400
LEFT_EDGE = -400
SIZE_X=400
SIZE_Y=250

#border
border=turtle.clone()
turtle.penup()
turtle.color("Dark Green")
turtle.pensize(20)
turtle.goto(LEFT_EDGE,UP_EDGE)
turtle.pendown()
turtle.goto(RIGHT_EDGE,UP_EDGE)
turtle.goto(RIGHT_EDGE,DOWN_EDGE)
turtle.goto(LEFT_EDGE,DOWN_EDGE)
turtle.goto(LEFT_EDGE,UP_EDGE)
#food
turtle.register_shape("snakefood-1.gif")
food = turtle.clone()
food.shape("snakefood-1.gif")
#gfuel
turtle.register_shape("pewdswithgfuel.gif")
gfuel=turtle.clone()
gfuel.shape("pewdswithgfuel.gif")



#stamp
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
def noth():
    turtle.forward(0)
    

def up():
    if snake.direction != "Down":
        snake.direction="Up"
        print("you pressed the up key!")
    else:
        print("Snake is unable to go down")
turtle.onkeypress(up,"w")

def down():
    if snake.direction != "Up":
        snake.direction="Down"
        print("you pressed the down key!")
    else:
        print("Snake is unable to go up")
turtle.onkeypress(down,"s")

def left():
    if snake.direction != "Right":
        snake.direction="Left"
        print("you pressed the left key!")
    else:
        print("Snake is unable to go right")
turtle.onkeypress(left,"a")

def right():
    if snake.direction != "Left":
        snake.direction="Right"
        print("you pressed the right key!")
    else:
        print("Snake is unable to go left")
turtle.onkeypress(right,"d")


turtle.listen()

def makefood():
    min_x=-int(SIZE_X/2/squaresize)+1
    max_x=int(SIZE_X/2/squaresize)-1
    min_y=-int(SIZE_Y/2/squaresize)+1
    max_y=int(SIZE_Y/2/squaresize)-1
    food.penup()
    food_x = random.randint(min_x,max_x)*squaresize
    food_y = random.randint(min_y,max_y)*squaresize
    food.goto(food_x, food_y)
    food_stamps.append(food.stamp())
    food_pos.append(food.pos())

def makegfuel():
    min_x=-int(SIZE_X/2/squaresize)+1
    max_x=int(SIZE_X/2/squaresize)-1
    min_y=-int(SIZE_Y/2/squaresize)+1
    max_y=int(SIZE_Y/2/squaresize)-1
    gfuel.penup()
    gfuel_x = random.randint(min_x,max_x)*squaresize
    gfuel_y = random.randint(min_y,max_y)*squaresize
    gfuel.goto(gfuel_x, gfuel_y)
    gfuel_stamps.append(gfuel.stamp())
    gfuel_pos.append(gfuel.pos())

    
    
    






def move_snake():
    moves.append("yo")
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]
    tx=snake.xcor()
    ty=snake.ycor()
    def eatfood():
        if snake.pos() in food_pos:
            food_index=food_pos.index(snake.pos())
            food.clearstamp(food_stamps[food_index])
            food_pos.pop(food_index)
            food_stamps.pop(food_index)
            print("You have eaten the food!")
            if len(moves) % 5 == 0:
                makegfuel()
            else:
                makefood()
            new_stamp()
    def eatgfuel():
        if snake.pos() in gfuel_pos:
            gfuel_index=gfuel_pos.index(snake.pos())
            gfuel.clearstamp(gfuel_stamps[gfuel_index])
            gfuel_pos.pop(gfuel_index)
            gfuel_stamps.pop(gfuel_index)
            print("You have eaten the food!")
            if len(moves) % 5 == 0:
                makegfuel()
            else:
                makefood()
            new_stamp()
            new_stamp()
            new_stamp()
        full.append(1)
        full.append(1)
        full.append(1)
            
    eatfood()
    eatgfuel()
    
    if snake.direction=="Up":
        snake.goto(x_pos,y_pos+20)
    if snake.direction=="Down":
        snake.goto(x_pos,y_pos-20)
    if snake.direction=="Left":
        snake.goto(x_pos-20,y_pos)
    if snake.direction=="Right":
        snake.goto(x_pos+20,y_pos)
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
#snake kills itself
    if new_pos in pos_list:
        quit()
#snake out of border
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    new_stamp()
    remove_stamp()
##    if len(full) > 1:
##        full.pop(0)
##        turtle.ontimer(move_snake,timestep)
##    else:
    turtle.ontimer(move_snake,timestep)

        
makefood()
move_snake()


turtle.mainloop()
    
    


