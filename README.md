# DailyChallenge
## Daily Python Challenge 1
Create a function that removes all capital letters and punctuation in a string. Return the clean string.

```
def clean_string(s):
    return ""
```

## Daily Python Challenge 2
Create a function that estimates the weight loss of a person using a certain weight loss program with their gender, current weight and how many weeks they plan to do the program as input. If the person follows the weight loss program, men can lose 1.5% of their body weight per week while women can lose 1.2% of their body weight per week. 

The possible inputs are:

Gender: 'M' for Male, 'F' for Female

Current weight: integer above 0

Number of weeks: integer above 0

Return the estimated weight after the specified number of weeks.

```
def lose_weight(gender, weight, duration):
    return weight
```

## Daily Python Challenge 3
Create a function that calculates how many times an integer can be divided by another given integer. If the answer of resulting divisions does not result in an integer, that division is not counted towards the number of times. As an example: 

If n is 10 and divisor is 3, since in the first division 10/3 doesn't return an integer, this division doesn't count towards the number of times and therefore its number of times should be 0.

```
def divisions(n, divisor):
    return number_of_times
```

## Daily Python Challenge 4
Given the number of people in the room, calculate the probability that any two people in that room have the same birthday, assuming we have 365 days in a year. (no leap years) Return the probability rounded off to two decimal points.

```
def calculate_probability(n):

    return probability
```

Hint: In order to calculate the probability, you might find it useful to use the probability that NO ONE shares the same birthday in the room:
365! / ((365-n)! * 365^n)
The ! sign above denotes the mathematical notation factorial. eg. 10! = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
The math module in Python has a built-in function for factorials which you can easily call. As a challenge you can also attempt the question without using the built-in factorial function.

## Daily Python Challenge 5
Create a function that given an n positive integer, it sums all the cubed values from 1 to n. Return the sum.

```
def sum_cubes(n):
    return sum
```

## Daily Python Challenge 6
Create a function that given a string, it returns the middle character of the string. If the length of the string is even, return the two middle characters of the string.

```
def middle(string):
    return middle_string
```




