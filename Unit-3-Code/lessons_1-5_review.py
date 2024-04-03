'''
Date: 4/1/2024
Lesson: Units 1-5 Review
'''

def main():
    # get pet breed
    breed = input("What is your pet's breed? ")
    
    # get pet weight in kg
    weight = float(input("What is your pet's weight in kilograms? "))
   
    # convert pet weight
    lb_weight = weight * 2.2
    rounded_weight = round(lb_weight,2)
    
    # create message to user
    message = f"Your {breed} weighs {weight}kg or {rounded_weight}lbs."
   
    # print message to user
    print(message)

if __name__ == '__main__':
    main()