# Unit 4 HW 2

## Exercise 1
Complete the function called valid_triangle(side_one, side_two, side_three). If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are 1 inch long, you will not be able to get the short sticks to meet in the middle because 12 > 1 + 1. For any three lengths, there is a simple test to see if it is possible to form a triangle:

If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can. If the sum of two lengths equals the third, they form what is called a “degenerate” triangle which is not really a triangle.

Write a code that prompts the user to input three stick lengths, and that prints either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks with the given lengths.
