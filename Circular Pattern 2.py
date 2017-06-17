import turtle

def draw_diamond(move) :
    for i in range(1,5):
        move.forward(100)
        move.right(45)
        move.forward(100)
        move.right(135)
        
def draw_pattern() :
    turtle.Screen().bgcolor("yellow")

    move = turtle.Turtle()

    move.shape("turtle")
    move.color("red")
    move.speed(0)

    for i in range(1,37):
        draw_diamond(move)
        move.right(10) 

    turtle.Screen().exitonclick

draw_pattern()
