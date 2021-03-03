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

## Daily Python Challenge 7
Given a list of integers, create a function that finds the odd one out in the list.

Example:

Input: [1,1,1,1,1,1,1,2]

Output: 2

## Daily Python Challenge 8
Given two integer inputs n and d, create a function that squares all numbers from 1 to n, then returns the count of all instances of d from the square results.  

Example: 
n: 5
d: 1

square of numbers from 1 to 5: 1, 4, 9, 16, 25
returns: 2 (since there's 2 instances of the digit 1, in 1 and 16)

## Daily Python Challenge 9
Given a string, add or subtract numbers and return the answer.

Example:
Input: 1plus2plus3minus4
Output: 2

Input: 2minus6plus4plus7
Output: 7


## Daily Python Challenge 10
Given an integer, create a function that finds and returns the length of the longest binary gap of the binary representation of that integer. A binary gap is the sequence of consecutive zeros in between ones in a binary representation. Reference for binary representation can be found here: https://www.rapidtables.com/convert/number/decimal-to-binary.html

Example:
Input: 9, which has binary representation 1001
Returns: 2

Input: 529, which has binary representation 1000010001
Returns: 4

Input: 20, which has binary representation 10100
Returns: 1

Input: 15, which has binary representation 1111
Returns: 0


## Daily Python Challenge 11
Given a string, return the character with the most value. The value of a character is the difference between the index of its first occurrence and the index of its last occurrence. If there is a tie, return the character that goes first alphabetically.

Example:
Input: 'abcdbcd'
Output: 'b', since difference between first index and last index = 4 - 1 = 3, which ties with the values of c and d but since b goes first alphabetically, that's the most valuable character.


## Daily Python Challenge 12
Given a list of 5 floats, return a tuple of the average of the middle 3 floats and the lowest float of that list.

Example:
Input:
[6.4, 11.4, 7.6, 10.5, 8.1]
Returns:
(9.83, 6.4), 9.83 (rounded off to nearest two decimal places) is the average of 11.4, 7.6 and 10.5 and 6.4 is the lowest float of the list.


## Daily Python Challenge 13
Given a string, create a function that splits the string into pairs of two characters. Put the pairs inside a list then return the list. If a character is missing in a pair, use the character '?' to replace the missing character.

Example:
Input: "abcdefg"
Output = ["ab", "cd", "ef", "g?"]

Input: "abcdef"
Output = ["ab", "cd", "ef"]


## Daily Python Challenge 14
Given a list of integers, split the list into two, put the arrays on top of each other, then add them together. Return the finished list.


Example:

Input:

[1, 2, 3, 4, 5, 6, 7]

Putting on top:

[1, 2, 3]

[4, 5, 6, 7]

Adding up process:

[1, 2, 3]

+

[4, 5, 6, 7]

Returns:

[5, 7, 9, 7]



## Daily Python Challenge 15
Given two lists of any data type, return a list that combines the two lists by alternating the elements passed. The input lists can be of different lengths.

Example 1:
Input lists: 
[1, 2, 3, 4, 5]
['a', 'b', 'c', 'd', 'e']
Returns:
[1, 'a', 2, b', 3, 'c', 4, 'd', 5, 'e']

Example 2:
Input lists:
[1, 2, 3]
['a', 'b', 'c', 'd', 'e']
Returns:
[1, 'a', 2, 'b', 3, 'c', 'd', 'e']

Example 3:
Input lists:
[1, 2, 3, 4, 5]
['a', 'b']
Returns:
[1, 'a', 2, 'b', 3, 4, 5]


## Daily Python Challenge 16
Given an integer n, find all the integers that is the multiple of 3 from 0 to n. Return the sum of all these integers.

Example:
Input: 
10
Multiples of 3 from 0 to 10:
3, 6, 9
Return sum of these integers:
18

## Daily Python Challenge 17
Given a list of 11 integers, return a string in the form of a Hong Kong phone number in this format: +852 xxxx xxxx

Only the numbers 2, 3, 5, 6, 7, and 9 can be added after the extension 852.

Example 1:

Input:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]

Returns:

"+852 9134 6701"


## Daily Python Challenge 18
Given an integer greater than 0, return a list of all possible palindromes of the integer.

Example:

Input: 

34322122

Output:

[22, 212, 343, 22122]

## Daily Python Challenge 19
Given a string of names with a certain pattern, return a formatted string with a certain pattern. 

Example:

Input:

"Alfred:Black;Carey:Drake;Elena:Ferguson;Georgina:Harrison"

Output:

"(BLACK, ALFRED)(DRAKE, CAREY)(FERGUSON, ELENA)(HARRISON, GEORGINA)"

## Daily Python Challenge 20
Given a string, count all the lowercase letters. Return a dictionary with the keys as the lowercase letters and the values as the letters' counts respectively. The keys should be sorted in alphabetical order.

Example:

Input:

"apple"

Output:

{'a': 1, 'e': 1, 'l': 1, 'p': 2}

## Daily Python Challenge 21
Given a list of mixed integers of different representations, add up the non-string integers and subtract this from the total of string integers.



Example:

Input:

[1, '2', 3, '4', 5]

Output:

-3, because:

total of non-string integers = 1+3+5 = 9

total of string integers = 2+4 = 6

total of string integers - total of non-string integers = -3 

## Daily Python Challenge 22
Given a string of decimal digits, output an integer of its binary representation like below:

Example:

Input: "2973"

"2" => 10

"9" => 1001

"7" => 111

"3" => 11

Therefore output is 10100111111, because of 10+1001+111+11.








