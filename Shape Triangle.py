import turtle

def draw_triangle() :
    turtle.Screen().bgcolor("yellow")

    move = turtle.Turtle()

    move.shape("turtle")
    move.color("red")
    move.speed(1)

    i=0
    while i < 3:    
        move.forward(100)
        move.right(120)
        i+=1
   
    turtle.Screen().exitonclick

draw_triangle()
