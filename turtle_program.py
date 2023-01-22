import turtle

#Creating the turtle object
my_Turtle = turtle.Turtle()

#Changing the cursor shape
my_Turtle.shape('turtle')
#my_Turtle.shape('triangle')
#my_Turtle.shape('turtle')
#my_Turtle.shape('square')
#my_Turtle.shape('arrow')

#Changing the size of the turtle
my_Turtle.shapesize(8,4,1)

#Changing the size of the pen
my_Turtle.pensize(3)

#Changing the screen size of the turtle window
turtle.screensize(canvwidth=800, canvheight=800, bg="red")

#Creating the first shape
my_Turtle.color('blue') #Change the color of the pen
my_Turtle.speed(6) #Speed can be 0 / fast, 10/fast, 6/normal, 3/slow or 1/slowest
my_Turtle.pendown() #Putting the pen down to start drawing
my_Turtle.forward(200) #Going forward 200
my_Turtle.left(200) #Going left 200
my_Turtle.back(200) #Going backward 200
my_Turtle.right(200) #Going right 200
my_Turtle.penup() #Putting the pen up to stop drawing

#Changing the size of the turtle
my_Turtle.shapesize(8,4,1)

#Changing the size of the pen
my_Turtle.pensize(3)

#Changing the screen size of the turtle window
turtle.screensize(canvwidth=800, canvheight=800, bg="red")
