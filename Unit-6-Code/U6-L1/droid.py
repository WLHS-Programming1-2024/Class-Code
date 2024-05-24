# function example for many units
# functions let us break programs into 
# small, easy to understand, easy to 
# diagnose parts

# no parameter function
def print_menu():
    print(f"Welcome to the droid interface. Right now, you can\
 just create a droid, but there is more coming.")
    print(r"""
     ,     ,
    (\____/)
     (_oo_)
       (O)
     __||__    \)
  []/______\[] /
  / \______/ \/
 /    /__\
(\   /____\
    
    """)

def create_droid(name,skill,battery_level):
    print(f"Congratulations! You have created the following droid:")
    print(f"Name: {name}")
    print(f"Skill: {skill}")
    print(f"Battery Level: {battery_level}")

# create droid_info that prints
# Name: 
# Current battery level: 

def droid_info(name,battery_level):
    print(f"Name: {name}")
    print(f"Current battery level: {battery_level}")

# create quick_charge that charges battery 5%
# should print message saying
# your battery was x% and is now y%

def quick_charge(current_level):
    print(f"Your battery level was {current_level}")
    print(f"Your batter level is now {current_level+5}")
    return 5

def deplete_battery(amount):
    return amount
    

def perform_task(task,current_level):
    if task == "Welding":
        current_level -= deplete_battery(-10)

def main():
    droid_one_name = "Ann"
    droid_one_skill = "Welding"
    droid_one_batt_lev = 85
    create_droid(droid_one_name,droid_one_skill,droid_one_batt_lev)
    droid_info(droid_one_name, droid_one_batt_lev)
    droid_one_batt_lev = droid_one_batt_lev + quick_charge(droid_one_batt_lev)
    droid_info(droid_one_name, droid_one_batt_lev)
    droid_one_batt_lev = deplete_battery(droid_one_batt_lev,droid_one_skill)
    droid_info(droid_one_name, droid_one_batt_lev)


main()
