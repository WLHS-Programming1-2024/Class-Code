from turtle import *

# create a square function then call it to draw
# a square with your turtle

side_length = int(input("Side length: "))

def draw_square(side_length):
    for i in range(4):
        forward(side_length)
        left(90)
    

for i in range(4):
    draw_square(side_length)

done()
