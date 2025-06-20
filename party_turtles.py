import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle for the turtle body
party_turtle = turtle.Turtle()
party_turtle.shape("turtle")
party_turtle.color("green")
party_turtle.penup()
party_turtle.goto(0, -50)
party_turtle.stamp()  # Draw the turtle

# Draw a "chicken" on the turtle's head (just a yellow circle for now)
chicken = turtle.Turtle()
chicken.shape("circle")
chicken.color("yellow")
chicken.shapesize(2, 2)  # Make the chicken bigger
chicken.penup()
chicken.goto(0, 30)  # Position above the turtle's head
chicken.stamp()  # Draw the chicken

# Add a party hat (triangle)
hat = turtle.Turtle()
hat.penup()
hat.goto(-10, 60)  # Move hat higher
hat.pendown()
hat.color("red")
hat.begin_fill()
for _ in range(3):
    hat.forward(20)
    hat.left(120)
hat.end_fill()
hat.hideturtle()

# Keep the window open until you click
screen.exitonclick()