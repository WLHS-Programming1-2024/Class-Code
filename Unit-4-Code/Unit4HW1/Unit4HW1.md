# Unit 4 HW 1

Starter code can be found in Unit4HW1.py. Please use this code to start.

## Problem 1
Late October can be a rather frightening time of year, in fact you could say it is spooky. But how spooky?  Its spookiness level can, in fact, be measured and represented as a single integer *n*. 
However, a simple number doesn't truly do the spooky sensation justice. As such, it can also be described with the word spoo...ooky, with exactly *n* o's.

You are going to complete the function
```
def spooky_season(n):
```
### Input Specification
a single integer *n*

### Output Specification
Output a single line consisting of a single string – the spooky word corresponding to the given value of *n*

### Sample Input
```
5
```
### Sample Output
```
spoooooky
```

## Problem 2
February 18 is a special date this year.

Write a program that asks the user for a numerical month and numerical day of the month and then determines whether that date occurs before, after, or on February 18.

* If the date occurs before February 18, output the word Before.
* If the date occurs after February 18, output the word After.
* If the date is February 18, output the word Special.
**The output is case sensitive - before is not the same as Before**

You will be putting the code that does this in the function 

'''
def special_day(month,day):
'''

### Input Specification
The input consists of two integers each in a separate variable. These integers represent a date in 2015.

The first line will contain the month, which will be an integer in the range from 1 (indicating January) to 12 (indicating December). The second line will contain the day of the month, which will be an integer in the range from 1 to 31. You can assume that the day of the month will be valid for the given month.

### Output Specification
Exactly one of Before, After, or Special will be printed on one line.

### Sample Input 1
```
month = 1
day = 7
```
### Sample Output 1
```
Before
```

### Sample Input 2
```
month = 8
day = 31
```
### Sample Output 2
```
After
```

### Sample Input 2
```
month = 2
day = 18
```
### Sample Output 2
```
Special
```
