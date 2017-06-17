import turtle

def draw_square(move) :
    for i in range(1,5):
        move.forward(100)
        move.right(90)
    
def draw_pattern() :
    turtle.Screen().bgcolor("yellow")

    move = turtle.Turtle()

    move.shape("turtle")
    move.color("red")
    move.speed(0)

    for i in range(1,37):
        draw_square(move)
        move.right(10) 

    turtle.Screen().exitonclick

draw_pattern()
