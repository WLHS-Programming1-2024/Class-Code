# Unit 4 HW 2

Starter code can be found in [Unit4HW2.py](https://github.com/WLHS-Programming1-2024/Class-Code/blob/main/Unit-4-Code/Unit4HW2/Unit4HW2.py). Please use this code to start.

You must do 5 test for each function. Be sure to test a variety of numbers. Do not do user input for these tests. See the sample input.

## Problem 1
Write a function called number_classifier that takes two numbers as parameters. The program should print the relation between the two numbers, which will be one of the following:
* numbers are equal
* first number is less than the second number
* first number is greater than the second number.

### Sample Input
'''
number_classifer(5,3)
'''

### Sample Output
'''
first number is greater than the second number
'''

## Problem 2
If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are 1 inch long, you will not be able to get the short sticks to meet in the middle because 12 > 1 + 1. For any three lengths, there is a simple test to see if it is possible to form a triangle:

If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can. If the sum of two lengths equals the third, they form what is called a “degenerate” triangle which is not really a triangle.

You are going to complete the function 

'''
valid_triangle(side_one, side_two, side_three)
'''

that prints either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks with the given lengths. In the main method, prompt the user to input three stick lengths and tell the user if they can or cannot make a triangle with those lengths. Before getting user input, you should test the function directly since it will go more quickly. You can use [https://www.mathwarehouse.com/triangle-calculator/online.php](https://www.mathwarehouse.com/triangle-calculator/online.php) to verify your work. Extra credit: If any of the numbers is negative, find a way to handle that. I will scale the extra credit based on how you handle it.

### Sample Input
```
valid_triangle(5,5,5)
```
### Sample Output
```
Yes
```

### Sample Input
```
valid_triangle(5,9,8)
```
### Sample Output
```
Yes
```

### Sample Input
```
valid_triangle(5,19,8)
```
### Sample Output
```
No
```

### Sample Input
```
valid_triangle(5,3,2)
```
### Sample Output
```
No
```

### Sample Input
```
valid_triangle(5,1,2)
```
### Sample Output
```
No
```

