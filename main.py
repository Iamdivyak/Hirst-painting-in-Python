import turtle

# import colorgram
# from PIL.ImageQt import rgb

# colors = colorgram.extract('img.jpg', 100)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
#
# print(rgb_colors)

from turtle import Turtle
import random

turtle.colormode(255)

tim = Turtle()

rgb_colors = [(223, 73, 55), (233, 144, 82), (19, 14, 14), (44, 88, 149),
              (231, 245, 238), (150, 66, 86), (214, 231, 238), (228, 221, 102), (124, 170, 200), (121, 167, 130),
              (19, 138, 87), (243, 223, 7), (83, 173, 90), (39, 44, 68), (89, 33, 35), (230, 172, 180), (222, 61, 92),
              (195, 128, 158), (115, 65, 45), (78, 48, 84), (16, 164, 214), (174, 187, 45), (161, 209, 185),
              (146, 209, 234)]
tim.penup()
tim.ht()
tim.setheading(230)
tim.fd(250)
tim.setheading(0)
tim.speed(50)
for _ in range(10):
    for _ in range(10):
        tim.dot(15, random.choice(rgb_colors))
        tim.fd(40)
    tim.left(90)
    tim.fd(40)
    tim.left(90)
    tim.forward(400)
    tim.setheading(0)








screen = turtle.Screen()
screen.exitonclick()
