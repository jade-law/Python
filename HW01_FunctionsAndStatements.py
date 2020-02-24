#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Statements
"""
__author__ = """ Jade Law """
__collab__ = """ I only used my own knowledge of Python to complete the homework assignment """

"""
Function name: groceries()
Parameters: no parameters
Return value: None
Description: Write a function that asks a user how many apples they want to buy, how many bananas they
want to buy, and how many peaches they want to buy. Considering that apples cost $0.50 each, bananas
cost $0.20 each, and peaches cost $0.75 each, calculate how much the user’s desired fruit would cost.

"""

def groceries():
    apples = int(input("How many apples would you like?"))
    bananas = int(input("How many bananas would you like?"))
    peaches = int(input("How many peaches would you like?"))
    cost = (apples*0.5) + (bananas*0.2) + (peaches*0.75)
    cost = str(cost)
    apples = str(apples)
    bananas = str(bananas)
    peaches = str(peaches)
    print("{} apples, {} bananas and {} peaches cost ${}.".format(apples, bananas, peaches, cost))

#groceries()

"""
Function name: volume_of_donut()
Parameters: no parameters
Return value: None
Description: Write a function that asks the user for the outer radius R and inner radius r (assume both
will be positive numbers) of a donut (also known as a torus), then calculates its volume based on the
following formula:
volume of a donut=(2πR)*(πr^2)
"""

import math
pi = math.pi

def volume_of_donut():
    outerRadius = float(input("What is the outer radius of the donut?"))
    innerRadius = float(input("What is the inner radius of the donut?"))
    volume = (2*pi*outerRadius)*(pi*(innerRadius**2))
    outerRadius = str(outerRadius)
    innerRadius = str(innerRadius)
    volume = str(round(volume, 3))
    print("A donut with the outer radius of {} and an inner radius of {} has the volume of {}.".format(outerRadius, innerRadius, volume))

#volume_of_donut()

"""
Function name: split_uber()
Parameters: no parameters
Return value: None
Description: Write a function that asks the user for the length in miles of the Uber ride (this can be a
non-negative int or float), a surge pricing multiplier (assume this will be a number greater than or
equal to 1), and the number of people who rode (assume this will be a positive int). Then, calculate
how much each person should pay for the ride, based on each mile of the ride costing $0.45.
Print this calculated value in the format:
“Your ride cost $(total cost of ride including surge pricing multiplier and tip), so the (number of
riders) riders should each pay $(cost per rider).”

"""

def split_uber():
    length = float(input("How many miles was the ride?"))
    surge = float(input("What is the surge pricing multiplier?"))
    people = int(input("How many people rode?"))
    tip = float(input("How much would you like to tip your driver?"))
    totalPrice = (length*0.45*surge)+tip
    singlePrice = totalPrice/people
    totalPrice = str(round(totalPrice,2))
    singlePrice = str(round(singlePrice,2))
    people = str(people)
    print("Your ride cost ${} so the {} riders should each pay ${}.".format(totalPrice, people, singlePrice))

#split_uber()


"""
Function name: cupcake_fan()
Parameters: no parameters
Return value: None
Description: You love cupcakes, but you also want to maintain your current weight! Write a function
that asks the user for the number of vanilla cupcakes they want to eat today, and the number of
chocolate cupcakes they want to eat today (assume the user wants to eat a whole integer number
of cupcakes). Then, calculate the number of miles the user would need to run to burn off the
calories, and the number of laps the user would need to swim to burn off the calories, and
print it in the following format:
“To burn off (number of vanilla cupcakes) vanilla cupcakes and (number of chocolate cupcakes)
chocolate cupcakes, you would need to run (number of miles) miles or swim (number of laps) laps!”
"""

import math
ceil = math.ceil

def cupcake_fan():
    numVanilla = int(input("How many vanilla cupcakes would you like to eat today?"))
    numChocolate = int(input("How many chocolate cupcakes would you like to eat today?"))
    calTotal = (numVanilla*300) + (numChocolate*410)
    runMiles = str(ceil(calTotal/95))
    swimLaps = str(ceil(calTotal/10))
    numVanilla = str(numVanilla)
    numChocolate = str(numChocolate)
    print("To burn off {} vanilla cupcakes and {} chocolate cupcakes, you would need to run {} miles or swim {} laps!".format(numVanilla, numChocolate, runMiles, swimLaps))

#cupcake_fan()

"""
Function name: package_eggs()
Parameters: no parameters
Return value: None
Description: Write a function that asks the user for the number of eggs that must be packaged
(assume this is a non-negative int), and calculates the number of grosses, boxes, cartons,
and mini-cartons to hold all the eggs. Print out the result in the following format:
“For (number of eggs) eggs, you will need (number of grosses) grosses, (number of boxes)
boxes, (number of cartons) cartons, and (number of mini-cartons) cartons, with (number of
leftover eggs) left over.”

Keep in mind the following:
144 eggs fit in a gross
36 eggs fit in a box
12 eggs fit in a carton
4 eggs fit in a mini-carton

Note: The answer should contain as many crates as possible followed by as many grosses as possible, then as many boxes as possible followed by cartons.

"""

def package_eggs():
    numEggs = int(input("How many eggs do you need to package?"))
    gross = numEggs//144
    box = (numEggs%144)//36
    carton = ((numEggs%144)%36)//12
    miniCarton = (((numEggs%144)%36)%12)//4
    leftOver = (((numEggs%144)%36)%12)%4
    numEggs = str(numEggs)
    gross = str(gross)
    box = str(box)
    carton = str(carton)
    miniCarton = str(miniCarton)
    leftOver = str(leftOver)
    print("For {} eggs, you will need {} grosses, {} boxes, {} cartons, and {} mini-cartons, with {} left over.".format(numEggs, gross, box, carton, miniCarton, leftOver))

#package_eggs()
