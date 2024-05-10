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



def main():
    print_menu()

main()
