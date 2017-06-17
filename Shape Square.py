import turtle

def draw_square() :
    turtle.Screen().bgcolor("yellow")

    move = turtle.Turtle()

    move.shape("turtle")
    move.color("red")
    move.speed(1)

    i=0
    
    while i < 4:    
        move.forward(100)
        move.right(90)
        i+=1
    turtle.Screen().exitonclick

draw_square()
