# Functions

## What are functions
* Functions allow us to break our program into smaller parts, and make the program
easier to understand.
* Functions allow us to break our program into parts that can be reused easily

Great part -  we don't even have to know how the work to use them

Example: print() in Python. We don't know how it is implemeted in Python. But we
use it all the time.

To use a function we have to call it by name

Make droid.py with the following functions
```
print_intro()
```

## What are parameters

Parameters are pieces of information that you can give functions when you call
them in order to customize their behavior.

Example: print() just prints a blank line
print("Hello") prints the string "Hello" and puts the cursor on a new line
print("Hello",end="") prints the string "Hello" and leaves the cursor on the
same line

Parameters can be a bit tricky so we have to trace them carefully

Consider the following

```
def print_num(x):
    print(x)
```

Where does x come from? We provide it
```
print_num(10)
print_num(30)
print_num(50)
```
You can have multiple parameters separated by commas
```
def print_sum(a,b):
    print(a+b)
```
print_sum(3,7)

To-do: Make a function called create_droid
that takes 3 parameters:
name - the droid's name
task - the droid's primary task
battery_level - the droid's initial battery level

It will print the following message:
Congratulations! You have created a droid named <droid's name> with a primary
task of <task> and an initial battery level of <battery level>%.