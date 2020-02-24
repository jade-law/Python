#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW05 - Tuples and Modules
"""
__author__ = """ Jade Law """
__collab__ = """ I worked with Rashmi Athavale for some of the problems. """

"""
Function: yelp_rating
Parameters: original (float), num (float), operation (string)
Returns: A float

Description: After visiting restaurants, you want to change the rating of the place.
Provided is a Python file (rate.py) containing functions for simple calculations that
you will need to import and use for this function.This function will take in an operation
(as a string) that will either be '+', '-', '*', or '/', as well as two other parameters
that are floats. original stands for the original rating and num is the number you want
to perform the operation with. Depending on the operation that is passed in, call the appropriate
function from the provided Python file and pass in the original and num arguments as parameters
to the function. Return the result of your calculation. If the operation passed in is not one of
the four valid symbols, return None.  If you do not use the functions in rate.py to solve this function
then you will not receive credit for this function.

Note: Round to one decimal point. 

"""

def yelp_rating(num1, num2, operation):
    import rate
    newRating = 0.0
    if operation == "+":
        return round(rate.add(num1, num2),1)
    elif operation == "-":
        return round(rate.subtract(num1, num2),1)
    elif operation == "*":
        return round(rate.multiply(num1, num2),1)
    elif operation == "/":
        return round(rate.divide(num1, num2),1)
    else:
        return None

"""
Function name: register_passport
Parameters: information (string)
Returns: A tuple 

Description: Before you pick your flights and travel destinations, you need to
make sure that your passport has been fully registered since the process usually
takes a long time! Write a function that takes in a string that holds information
about a person registering for their passport. You can assume that the string will
always be in the format “NAME: AGE, COUNTRYCODE”. Return a tuple in the format (COUNTRYCODE (string), NAME (string), AGE (int)).

Note: There is a space before AGE and before COUNTRYCODE. The tuple returned must
not have any spaces around the strings. For example, it should be “Caitlin Yang”, not “ Caitlin Yang  ”.


"""

def register_passport(info):
    tup = (info[info.find(",")+2:], info[:info.find(":")], int(info[info.find(":")+2:info.find(",")]))
    return tup

"""
Function name: location_ideas 
Parameters: list of tuples
Returns: tuple 
Description: Now after you have registered your passport, you need to brainstorm what
locations you want to travel to. Write a function that takes in a list of tuples in the
form (LOCATION (string), MILES_AWAY (int)). Return a tuple of the locations in order from
closest (lowest miles away) to farthest (greatest miles away). If the list passed in is empty,
return an empty tuple. No two locations will have the same distance. 

NOTE: You cannot use the lambda function.

"""

def location_ideas(tuplist):
    tupDistance = ()
    newtup = ()
    for (place,distance) in tuplist:
        tupDistance += (distance,)
    tupDistance = sorted(tupDistance)
    for i in tupDistance:
        for (place,distance) in tuplist:
            if i == distance:
                newtup += (place,)
    return newtup

"""
Function: find_airbnb
Parameters:  airbnb list (list of tuples), number of people (int), max price (float) 
Returns: A tuple 

Description: As a broke college student, you want to be able to stay in the best airbnb as
possible but also stay in the airbnb that is affordable for you. You also want to be able to
find an airbnb that will fit you and all your friends. Write a function called find_airbnb that
takes in a list of airbnb tuples in the format (NAME, CAPACITY, RATING, PRICE_PER_NIGHT). The
airbnb must be able to fit everyone in your party and be within your price range. If multiple
apartments fit these requirements, return the one with the highest rating. No airbnbs with the
same capacity will ever have the same rating. Return a tuple with the name of the airbnb (string)
and the price that each person in your group will pay per night (float rounded to two decimal places). Also,
if no airbnbs satisfy the conditions, then return an empty tuple. 

Note: If two airbnbs are both below the price range, then you should return the one with the highest rating. 

"""

def find_airbnb(list, num, maxprice):
    newTuple = ()
    nope = ()
    bestRate = 0
    bestPrice = 1000
    personPrice = 0
    for (name, cap, rate, price) in list:
        if num > cap:
            nope += (name,)
        if price > maxprice:
            nope += (name,)
    for (name, cap, rate, price) in list:
        if rate > bestRate and name not in nope:
            bestRate = rate
    for (name, cap, rate, price) in list:
        if bestRate == rate:
            personPrice = round(price/num,2)
            if personPrice < bestPrice:
                bestPrice = personPrice
                newTuple = (name, personPrice)

    return newTuple


    

"""
Function: travel_buddy
Parameters: A string 
Returns: A tuple 

Description: When going on vacation, it’s always better going with your BFF, but
sometimes, it’s hard choosing your favorite. Write a function that takes in a string
containing information about multiple friends. You may assume the string may always
be formatted in this way: “Friend_Name, Friend_Level ; Friend_Name, Friend_Level ; etc.”. Using
the information given in the string, find the highest friend level, and return the friend’s name
and the friend’s level in a tuple formatted as (Friend_Name, Friend_Level).

Notes:

An empty string will never be passed in. If two friends have the same friend level, then return the friend that came last in the string


"""

def travel_buddy(friend):
    list = friend.strip().split("; ")
    list2 = []
    tuple = ()
    result = ()
    max = -100
    for f in list:
        list2.append(f.split(", "))
    for f in list2:
        f[1] = int(f[1])
        if f[1] >= max:
            result = (f[0], f[1])
            max = f[1]
    return result

"""

Function name: remove_ingredients
Parameters: recipeList (list of tuples of strings), allergyList (list of strings)
Returns: list of tuples of strings
Description: You prepared a list of dishes you wanted to try while on vacation, but at the last
minute you realize your BFF is allergic to a few ingredients. You are given a recipeList which is
a list of tuples. Each tuple represents a dish and contains strings representing the ingredients
of the dish. The second parameter, allergyList, is a list of things that your friend is allergic
to. For this function, go through the ingredients for each dish (tuple) and remove the ingredients
that she/he is allergic to. Return a new list of tuples representing the modified dishes without the ingredients.

Notes: Your code should not allow capitalization to change the searching of the ingredients. So for example,
if “Spinach” is in the dish, and “spinach” is on the allergy list, the ingredient “Spinach” would be eligible
to be removed. You will need to add the original casing of the ingredients to your final list.

"""

def remove_ingredients(recipeList, allergyList):
    recipeLower = []
    allergyLower = []
    allergic = []
    final = []
    for tup in recipeList:
        b = ()
        for item in tup:
            b += (item.lower(),)
        recipeLower.append(b)
    for item in allergyList:
        allergyLower.append(item.lower())
    for tup in recipeLower:
        for item in tup:
            if item in allergyLower:
                allergic.append(item)
    for tup in range(len(recipeLower)):
        b = ()
        for item in range(len(recipeLower[tup])):
            if recipeLower[tup][item] not in allergic:
                b += (recipeList[tup][item],)
        final.append(b)
    return final
