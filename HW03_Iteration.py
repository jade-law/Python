#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW03 - Iteration
"""
__author__ = """ Jade Law """
__collab__ = """ I worked with Rashmi Athavale on some of the problems """

"""
Function name: countMeasures()
Parameters: a number (an int)
Return value: None
Description: In music, when there is a time signature 4/4, it means that
there are four beats a measure. You are able to count a measure by counting
to four, “1, 2, 3, 4”. However, when you want to keep track of what measure
you are on in a song, you can change the first number to the number
corresponding to what measure you are on. So if there are four measures
in a song, a person might count
“1, 2, 3, 4, 2, 2, 3, 4, 3, 2, 3, 4, 4, 2,3 , 4”.
Write a function that will take in a number that corresponds to the
number of measures needed to be counted. The function will then create a
string PER MEASURE of how it would be counted, with commas separating each
number, and then print on a new line. Follow the format shown below in the
test cases. Nothing is to be returned. 

"""

def countMeasures(measures):
    for i in range(1,measures+1):
        print(i,end=", ")
        for j in range(2, 5):
            if j == 4:
                print(j,end="\n")
            else:
                print(j,end=", ")

"""
Function name: expandWord()
Parameters: a word (a String) and a number (an int)
Return value: the string with the letters repeated as many times as specified by the number
Description: Write a function that makes a new string of the letters in the
word repeated the number of times specified by the number. Return the newly
created string.

Notes: 
You may not use the multiplication operator in this problem!
Spaces are also considered to be characters.

"""

def expandWord(word, num):
    newString = ""
    for letter in word:
        for i in range(num):
            newString += letter 
    return newString

"""
Function name: findMiniWord()
Parameters: a word that contains two brackets “[]” (a String)
Return value: the word with the brackets and everything in between them removed (a String)
Description: Write a function that removes the brackets and everything in between them
from the word. Return the new word with the brackets and everything in between them removed.
"""

def findMiniWord(sentence):
    miniWord = ""
    notMiniWord = ""
    loc1 = 0
    loc2 = 0
    for letter in range(len(sentence)):
        if sentence[letter] == "[":
            loc1 = letter
        if sentence[letter] == "]":
            loc2 = letter+1
    miniWord += sentence[loc1:loc2]
    notMiniWord += sentence[0:loc1]
    notMiniWord += sentence[loc2:len(sentence)]
    return notMiniWord

"""
Function name: makeRectangle()
Parameters: a length (an int) and a width (an int)
Return value: None
Description: Print out a rectangle based on the length and width that were given as parameters.
The output should be formatted exactly as shown in the pdf. There should be no extra newline at
the end of the output.
"""

def makeRectangle(l, w):
    for i in range(w):
        for j in range(l, 0, -1):
            if j==1:
                print(j,end="\n")
            else:
                print(j,end="")

"""
Function name: howManyEggs()
Parameters: number of eggs (an int) and number of guesses allowed (an int)
Return value: True if the user guessed the answer within the number of guesses allowed limit; False otherwise
Description: Write a function that takes in an integer value of the number of eggs and asks
the user to try to guess this number. If the user has not guessed the correct answer after trying
the allowed number of times, then print “You lost!” and return False. If the user guesses the
correct number within the limit, then print “You did it in [number of tries] tries!” and return True.

Notes: 
You must use a while loop.
All bolded values in the test cases (on the pdf) are user input values

"""

def howManyEggs(numEggs, numTries):
    guess = int(input("How many eggs do you think there are?"))
    tries = 0
    while guess != numEggs:
        tries += 1
        if tries == numTries:
            print("You lost!")
            return False
        else:
            guess = int(input("Wrong answer! Try again: "))
    if guess == numEggs:
        print("You did it in {} tries!".format(tries+1))
        return True

"""
Function name: secret_message()
Parameters: a phrase that contains a hidden message (a String)
Return value: the hidden message (a String)
Description: You have a new job as a detective and they assign you to decode secret messages.
Write a function that takes in a message, which is separated by spaces. You must find the first
letter of each word and put them together into a new word. Each space indicates the start of
a new word.

Note: The first and last character of the hidden message (parameter) will never be a space.

"""

def secret_message(message):
    secretMessage = ""
    secretMessage += message[0]
    for letter in range(len(message)):
        if message[letter] == " ":
            secretMessage += message[letter+1]
    return secretMessage
"""
Function name: multiplication_table()
Parameters: number of multiples (rows) your table should have - positive integer (an int),
base multiplier of you table - positive integer (an int).
Return value: None
Description: Write a function that takes two positive integers as parameters and prints a table.
The first parameter should be the number of rows of your table. The second parameter should be the
base multiplier of your table. The table consists of a certain number of rows and each row should
be multiplied by a specific multiple. Additionally, each row should have the same number of elements of the
result of the multiplication. For example, if the result of the multiplication in a row is 3, it
should print three “3”. See the test cases for more information.

"""

def multiplication_table(rows, multiplier):
    for i in range(1,rows+1):
        for j in range(i*multiplier-1):
            print(i*multiplier,end="")
        print(i*multiplier,end="\n")

"""
Function name: sum_check()
Parameters: a string of positive integers (a String), and an int
Return value: Boolean, whether the sum of the numbers in the string equals the int passed as a parameter.
Description: This function should iterate through the string and
sum all the numbers in it. Return True if the sum of the values in the string is equal to the int passed in as
a parameter. Otherwise, return False. 

"""

def sum_check(numbers, trueSum):
    total = 0
    for i in numbers:
        total = int(i)+total
    if total == trueSum:
        return True
    elif total != trueSum:
        return False

"""
Function name: string_cleaner()
Parameters: a string that consists of digits and characters (a String), and a boolean.
Return value: a new string - depending on whether it was changed or not (a String)
Description: This function should “clean” the string that is passed in, depending whether the
boolean is True or False. If the boolean is True, the function should return a new string that
does not include the digits; additionally, the function should print the digits that you removed.
If the boolean is False, the function should return the string as it was before.

"""
def string_cleaner(string, boolean):
    cleanString = ""
    if boolean:
        for i in string:
            if i not in "1234567890":
                cleanString += i
            else:
                print(i)
        return cleanString
    else:
        return string

