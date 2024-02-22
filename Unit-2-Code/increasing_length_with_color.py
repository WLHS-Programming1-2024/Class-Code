line_thickness = int(input("What is the thickness of the marks? (1-20): "))
color_one = input("What color should the first mark be?: ")
color_two = input("What color should the second mark be?: ")
color_three = input("What color should the third mark be?: ")
color_four = input("What color should the fourth mark be?: ")

# draws initial horizontal line
forward(200)
backward(400)

hash_mark_length = 100
# first hash mark
forward(25)
color(color_one)
pensize(line_thickness)
left(90)
forward(hash_mark_length/2)
right(180)
forward(hash_mark_length)

penup()
left(180)
forward(hash_mark_length/2)
right(90)

forward(25)
pendown()
color(color_two)
left(90)
forward(hash_mark_length/2)
