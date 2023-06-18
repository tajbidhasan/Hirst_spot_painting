import turtle as turtle_module
import random
import color_generator

turtle_module.colormode(255)

pen = turtle_module.Turtle()
pen.color("")
pen.speed("fastest")

color_list = color_generator.rgb_colors

pen.setheading(225)
pen.forward(300)
pen.setheading(0)
number_of_dots = 100


for dot_count in range(1,number_of_dots + 1):
    pen.dot(20, random.choice(color_list))
    pen.forward(50)

    if dot_count % 10 == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()