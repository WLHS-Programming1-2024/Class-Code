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

def create_droid(droid_info):
    """Creates a droid

    Args:
        droid_info: a list of info [name,skill,battery_level]
    Returns: None
    """
    print(f"Congratulations!")
    print(f"You created a droid named {droid_info[0]} with a skill of {droid_info[1]} and a battery level of {droid_info[2]} ")

    return None
def droid_info():
    return None
    
def quick_charge():
    return None
    

def time_charge():
    return None
    


def main():
    print_menu()
    # droid list format is name,skill,battery_level
    droid_one_info = ["Bender","Bending",45]
    create_droid(droid_one_info)


if __name__ == '__main__':
    main()