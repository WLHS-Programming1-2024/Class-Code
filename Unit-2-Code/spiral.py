from turtle import *

def spiral_one():
    n = 0
    while n<100:
        forward(n)
        right(90)
        n = n+3

def spiral_two():
    n = 0
    while n<75:
        forward(n)
        right(90-n)
        n = n+1

spiral_two()

done()