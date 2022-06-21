import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    cheese = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    cheese.shape('turtle')
    # Set your turtle's speed using .speed(2)
    cheese.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    cheese.color('green')
    cheese.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    for i in range (4):
        cheese.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
        cheese.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    cheese.goto(20,20)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    cheese.color('red')
    cheese.begin_fill()
    cheese.circle(50, steps=38)
    cheese.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    cheese.color('blue')
    cheese.begin_fill()
    cheese.circle(25, steps=38)
    cheese.end_fill()

    cheese.color('purple')
    cheese.begin_fill()
    cheese.circle(15, steps=38)
    cheese.end_fill()

    cheese.color('orange')
    cheese.begin_fill()
    cheese.circle(10, steps=38)
    cheese.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
