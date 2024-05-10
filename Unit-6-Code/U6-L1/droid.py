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

# create quick_charge that charges battery 5%
# should print message saying
# your battery was x% and is now y%



def main():
    droid_one_name = "Ann"
    droid_one_skill = "Welding"
    droid_one_batt_lev = 85
    create_droid(droid_one_name,droid_one_skill,droid_one_batt_lev)
    # droid_info(droid_one_name, droid_one_batt_level) - this is a warmup to start class


main()
