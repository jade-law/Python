#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW04 - Strings and Lists
"""
__author__ = """ Jade Law """
__collab__ = """ I worked on this assignment with Rashmi Athavale """

"""
Function name: reverse_sentence
Parameters: sentence (str)
Returns: reversed string (str)
Description: Write a function that takes in a sentence as a string and returns
the sentence with the words reversed. You may use the .split() function,
and a sentence will never start with a space.
"""

def reverse_sentence(sentence):
    sentenceList = sentence.split()
    newSentence = ""
    for index in range(len(sentenceList)-1,-1,-1):
        newSentence += sentenceList[index] + " "
    return newSentence.strip()

"""
Function name: insert_string
Parameters: sentence (str), word (str), index (int)
Returns: sentence with word inserted at the index (str)
Description: Given a sentence, a word and an integer index,
write a function that inserts the word into the sentence at the index.
"""

def insert_string(sentence, word, index):
    new = ""
    for ind in range(index):
        new += sentence[ind]
    new += word
    for ind in range(index,len(sentence)):
        new += sentence[ind]
    return new

"""
Function name: count_matches
Parameters: sentence (str), substring (str)
Returns: number of matches (int)
Description: Write a function that takes in two strings and returns
the number of times the substring occurs in the sentence
"""

def count_matches(sentence,substring):
    count = 0
    for i in range(len(sentence)):
        if sentence[i:i+len(substring)] == substring:
            count += 1
    return count

"""
Function name: list_symmetric
Parameters: list of integers (list)
Returns: boolean representing if list is symmetric or not (boolean)
Description:  Define a function that accepts one list of integers as a parameter
and returns a boolean representing whether the list is symmetric.
For the purpose of this problem, a list is considered symmetric if and only if,
there is an item of equal value on the opposite side of the list and equidistant
from the nearest end (similar in concept to a palindrome).
An empty list is also considered symmetric.
"""

def list_symmetric(intList):
    length = len(intList)
    if length == 1:
        return True
    elif length == 0:
        return True
    elif length%2 == 0:
        if intList[(length//2)-1::-1] == intList[length//2:]:
            return True
        else:
            return False
    elif length%2 == 1:
        if intList[(length//2)-1::-1] == intList[(length//2)+1:]:
            return True
        else:
            return False

"""
Function name: grade_counter
Parameters: list of grades (list of ints), amount of extra credit (int),  letter grade (string)
Returns: number of students that got that letter grade after extra credit (int)
Description: Write a function that takes a list of student grades in a class,
an integer amount of extra credit to be applied to each student's grade,
and a letter grade (“A”, “B”, “C”, “D”, or “F”).
The letter grade parameter will always be one capital letter from the list below.
Return the number of students that made the given letter grade after extra credit is applied to their grade. 
"""

def grade_counter(grades, ec, letter):
    count = 0
    for each in grades:
        each += ec
        if letter == "A":
            if each >= 90 and each <= 105:
                count += 1
        elif letter == "B":
            if each >= 80 and each < 90:
                count += 1
        elif letter == "C":
            if each >= 70 and each < 80:
                count += 1
        elif letter == "D":
            if each >= 60 and each < 70:
                count += 1
        elif letter == "F":
            if each < 60 and each >= 0:
                count += 1
    return count

"""
Function name: invite_only
Parameters: list of people in line (list of strings), list of people invited (list of strings)
Returns: list of people allowed in (list of strings)
Description: Write a function that takes in two lists of strings, where the first list
contains the names of people waiting in line to get into a party,
and the second list contains the names of the people invited to the party.
Someone waiting in line will be allowed in if they are on the invite list.
If two people in line have the same name, only allow the first person into
the party if their name is on the invite list. In other words, do not allow duplicate
entries into the party, even if the names have different capitalizations.
Return a list of the people who were allowed into the party, in the order
that they were present in the line (left to right).
In the event that nobody was allowed in, return an empty list.

Note: Your code should not allow capitalization to change the final input.
So for example, if “Cory Brooks” is in the line, he should be allowed in if “cory brooks”
is on the invite list. However, be sure to add the original “Cory Brooks” to your final list.
"""

def invite_only(line, invite):
    allowedList = []
    lowerLine = []
    lowerInvite = []
    for name in line:
        lowerLine += [name.lower()]
    for name2 in invite:
        lowerInvite += [name2.lower()]
    for i in range(len(lowerLine)):
        if lowerLine[i] in lowerInvite:
            dupCount = 0
            for name in allowedList:
                if name.lower() == lowerLine[i]:
                    dupCount += 1
            if dupCount == 0:
                allowedList.append(line[i])
    return allowedList

"""
Function name: study_group
Parameters: list of students and their major (list of strings), your major (string)
Returns: list of students with the same major (list of strings)
Description: Write a function that takes a list and a string, where the list
represents other students, and the string represents your major.
Return a list of the names of students that have same major as you so that
you can form a study group with them. Every string in the list of students
will be in the format “Full Name, Major”, and your major will be in the format “Major”.
If no other student has the same major as you, return an empty list.
Ignore capitalization of majors in the same manner as previous questions.
There will always be one comma in each string.

Hint: The .split() and .strip() functions might be helpful for this function
"""

def study_group(theirMajor,myMajor):
    theirMajorLower = []
    invited = []
    theirMajor2 = []
    myMajorLower = ""
    myMajorLower = myMajor.lower()
    for each in theirMajor:
        theirMajor2.append(each.split(", "))
        theirMajorLower.append(each.lower().split(", "))
    for ind in range(len(theirMajorLower)):
        if theirMajorLower[ind][1] == myMajorLower:
            invited.append(theirMajor2[ind][0])
    return invited
    

"""
Function name: calculate_gpa
Parameters: list of lists representing class grades and credits (nested list)
Returns: calculated GPA (float)
Description: Write a function that takes in a list of lists that each represent
your final grade in a class, and that class' associated number of credits.
Calculate your GPA based on the grades and weights using the following information (view the PDF).
Assume that the total number of credits taken will always be greater than zero.
Round your final answer to two decimal places.
"""

def calculate_gpa(list):
    totalCredits = 0
    PointsList = []
    numerator = 0
    for each in range(len(list)):
        if list[each][0] >= 90:
            PointsList.append(4)
        elif list[each][0] >= 80:
            PointsList.append(3)
        elif list[each][0] >= 70:
            PointsList.append(2)
        elif list[each][0] >= 60:
            PointsList.append(1)
        elif list[each][0] >= 50:
            PointsList.append(0)
    for ind in range(len(PointsList)):
        numerator += (PointsList[ind]) * (list[ind][1])
        totalCredits += list[ind][1]
    return round(numerator/totalCredits,2)
