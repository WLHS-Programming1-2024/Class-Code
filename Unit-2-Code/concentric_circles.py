# Before Functions #

user_circle_radius1 = int(input("What is the first circle's radius?: "))
penup()
goto(0,-user_circle_radius1)
pendown()
circle(user_circle_radius1)

user_circle_radius2 = int(input("What is the second circle's raidus?: "))
penup()
goto(0,-user_circle_radius2)
pendown()
circle(user_circle_radius2)

user_circle_radius3 = int(input("what is the third circle's radius?: "))
penup()
goto(0,-user_circle_radius3)
pendown()
circle(user_circle_radius3)
##########################################################################
# After making function (modularization) #
def circle_drawer(radius):
    penup()
    goto(0,-radius)
    pendown()
    circle(radius)

user_circle_radius1 = int(input("What is the first circle's radius?: "))
circle_drawer(user_circle_radius1)

user_circle_radius2 = int(input("What is the second circle's raidus?: "))
circle_drawer(user_circle_radius2)

user_circle_radius3 = int(input("what is the third circle's radius?: "))
circle_drawer(user_circle_radius3)
##########################################################################
# Extra efficient version #
def circle_drawer(radius):
    penup()
    goto(0,-radius)
    pendown()
    circle(radius)

for circle_num in range(3):
    user_radius = int(input("Enter the radius for circle "+str(circle_num+1)+": "))
    circle_drawer(user_radius)
