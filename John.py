import turtle

# Create a turtle object for the car
car = turtle.Turtle()

# Function to turn the car left
def turn_left():
    car.left(30)

# Function to turn the car right
def turn_right():
    car.right(30)

# Function to move the car forward
def move_forward():
    car.forward(50)

# Function to move the car backward
def move_backward():
    car.backward(50)

# Function to exit the program
def exit_program():
    turtle.bye()

# Set up the screen
screen = turtle.Screen()
screen.title("Car Control")
screen.bgcolor("white")

# Set up keyboard bindings
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(exit_program, "q")

# Enable listening for keyboard events
screen.listen()

# Start the main event loop
turtle.mainloop()