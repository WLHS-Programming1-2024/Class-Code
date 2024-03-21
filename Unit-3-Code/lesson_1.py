
# This covers lessons 1-3 in Unit 3 of CodeHS


def main():
    # Task: Ask a person for their first
    # name and their last name. Print out
    # a message that says 
    # "Good day, first_name last_name!"

    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    full_name = f"{first_name} {last_name}"
    age = int(input("Age: "))
    # print("Hello,",user_name)
    # print("Hello, "+user_name)
    print(f"Hello, {full_name.title()}!")
    print(f"Hello, {full_name.upper()}!")
    print(f"Hello, {full_name.lower()}!")
    print(f"You are {age} years old.")
    print(f"In 10 years you will be {age+10}.")
    # print('Mr. Smith said, "Hello".')

if __name__ == '__main__':
    main()