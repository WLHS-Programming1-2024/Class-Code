def grade_book(grade):
    if grade >= 90:
        print("A")
    if grade >= 80:
        print("B")
    if grade >= 70:
        print("C")
    if grade >= 60:
        print("D")
    else:
        print("F")

def main():
    grade_book(75)

if __name__ == '__main__':
    main()