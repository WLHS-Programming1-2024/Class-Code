# test if a number is positive and
# is greater than  12

number = int(input("Enter number: "))

# old way
# if number > 0:
#     if number > 12:
#         print("Great choice!")
#     else:
#         print("Not greater than 12")
# else:
#     print("Not positive")

if number > 0 and number > 12: # both are true
    print("Great choice!")

# one or the other is true or both are true
if number > 0 or number > 12: 
    print("Great choice!")

# Truth tables
# T and T = T
# T and F = F
# F and T = F
# F and F = F

# T or T = T
# T or F = T
# F or T = T
# F or F = F
