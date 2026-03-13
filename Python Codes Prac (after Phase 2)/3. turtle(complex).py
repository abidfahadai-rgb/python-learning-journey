import turtle

# Draw pentagon
turtle.pendown()
for i in range(5):
    turtle.forward(100)
    turtle.left(72)

# Move to draw the inside line
turtle.penup()
turtle.goto(-60, -40)

# Draw inside line
turtle.pendown()
turtle.forward(120)

# Move to draw the bottom line
turtle.penup()
turtle.goto(-70, -120)

# Draw bottom line
turtle.pendown()
turtle.forward(140)

turtle.done()
