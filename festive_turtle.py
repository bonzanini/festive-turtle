import turtle

if __name__ == '__main__':
    wn = turtle.Screen()

    my_turtle = turtle.Turtle()

    # start drawing the tree
    my_turtle.color("darkgreen")
    my_turtle.pensize(5)
    my_turtle.begin_fill()
    # right half of the tree
    my_turtle.forward(100)
    my_turtle.left(150)
    my_turtle.forward(90)
    my_turtle.right(150)
    my_turtle.forward(60)
    my_turtle.left(150)
    my_turtle.forward(60)
    my_turtle.right(150)
    my_turtle.forward(40)
    my_turtle.left(150)
    my_turtle.forward(100)
    # left half of the tree
    my_turtle.left(60)
    my_turtle.forward(100)
    my_turtle.left(150)
    my_turtle.forward(40)
    my_turtle.right(150)
    my_turtle.forward(60)
    my_turtle.left(150)
    my_turtle.forward(60)
    my_turtle.right(150)
    my_turtle.forward(90)
    my_turtle.left(150)
    my_turtle.forward(133)

    my_turtle.end_fill()
    # trunk
    my_turtle.color("brown")
    my_turtle.pensize(1)
    my_turtle.begin_fill()

    my_turtle.right(90)
    my_turtle.forward(70)
    my_turtle.right(90)
    my_turtle.forward(33)
    my_turtle.right(90)
    my_turtle.forward(70)

    my_turtle.end_fill()

    # star, see similar example on python.org
    my_turtle.penup()
    my_turtle.setpos(-17, 110)
    my_turtle.color("gold")
    my_turtle.begin_fill()
    my_turtle.pendown()
    for _ in range(36):
        my_turtle.forward(40)
        my_turtle.left(170)
    my_turtle.end_fill()


    # some colourful balls
    def ball(trt, x, y, size=10, colour="red"):
        trt.penup()
        trt.setpos(x, y)
        trt.color(colour)
        trt.begin_fill()
        trt.pendown()
        trt.circle(size)
        trt.end_fill()

    ball(my_turtle, 95, -5)
    ball(my_turtle, -110, -5)
    ball(my_turtle, 80, 40, size=7, colour="gold")
    ball(my_turtle, -98, 40, size=7, colour="gold")
    ball(my_turtle, 70, 70, size=5)
    ball(my_turtle, -93, 70, size=5)


    my_turtle.hideturtle()
    wn.mainloop()
