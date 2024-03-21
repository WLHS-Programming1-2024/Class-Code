PI = 3.1415
# square area
def square_area(number):
    area = number ** 2
    return area

# circle area - if number = 5, area is 78.5375
def circle_area(number):
    area = PI * number ** 2
    return area


def main():
    # float means it can be a decimal number
    fav_num = float(input("What is your favorite number? "))
    area = square_area(fav_num)
    area_two = circle_area(fav_num)
    print(f"A square with side {fav_num} has an area of {area}.")
    print(f"A circle with a radius of {fav_num} has an area of {area_two}")

if __name__ == '__main__':
    main()