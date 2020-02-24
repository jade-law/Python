#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW06 - TRY/EXCEPT & DICTIONARIES
"""
__author__ = """ Jade Law """
__collab__ = """ I worked with Rashmi Athavale on some of the problems. """

"""
Function name: make_gamertag
Parameters: list, str
Returns: str 
Description: Write a function that takes in a string and a list of integers
and adds indices (specified in the list) from the string into your
soon-to-be tag. Anytime the desired index does not exist, add in a “0” zero
to the gamertag, but if the index is valid, add the corresponding character
as well as another “x” just for spice. When you have gone through all entries
of the list, surround the tag with square “[“  “]” brackets and return the string.

"""

def make_gamertag(string, list):
    gamertag = "["
    for num in list:
        try:
            gamertag += string[num]
            gamertag += "x"
        except:
            gamertag += "0"
    gamertag += "]"
    return gamertag

"""
Function name: split_the_loot
Parameters: dict, list, int/float, int
Returns: float
Description: Write a function split_the_loot that takes in these four things
and also the number of thieves to split between. If the letter case of the
items in the list differ from the dictionary entries at all,
do not count it to the total. (i.e. “hello” != “hEllo”)

If any of the parameter types are invalid, the code should catch it and
return a string saying “TypeError”. If any of the catalog prices are negative
and it is in the items list, return “Negative”. If the number of burglars is 0
or less, return “BurglarError”
"""

def split_the_loot(items, stolen, money, people):
    try:
        total = float(money)
        if people <= 0:
            raise ZeroDivisionError
    except TypeError:
        return TypeError
    except ZeroDivisionError:
        return "BurglarError"
    for item in stolen:
        try:
            if type(item) is not type(""):
                raise TypeError
            total += items[item]
        except TypeError:
            return "TypeError"
        except KeyError:
            for each in items:
                if item.lower() == each.lower():
                    break
                else:
                    return "Negative"
        except items[item] < 0 and item not in items:
            return "Negative"
    return round(total/people,2)

"""
Function name: football_stars
Parameters: dict, dict
Returns: dict 
Description: Write a function that takes in two different dictionaries, one with
a state name as the key and a list of teams in that state as the value. The other
dictionary has an NFL team name as the key and the name of a top player on that
team as the value. If a player in the latter dictionary is on a team that appears
in the first list, add the player’s name as a key in a new dictionary and match it
to a tuple of the state and the team name that the player is on.

"""

def football_stars(loc,teams):
    newdict = {}
    player = ""
    team = ""
    place = ""
    for pl in loc:
        for i in loc[pl]:
            if i in teams:
                team = i
                player = teams[i]
                place = pl
                newdict[player] = (place,team)
    return newdict

"""
Function name: pair_rivals
Parameters: dict, dict
Returns: dict
Description: In this function you will take in two dictionary arguments, and return
a new dictionary. Both parameters will have one string keys paired to one string
values. Each key will represent a certain character and the value will be the rival
of that character. If one character’s rival in the first dictionary is that rival’s
rival in any of the dictionaries, add a tuple of both names as a key (first, second)
in a new dictionary, paired to True as its value. In other words, only add it into
the new dictionary if “character”:”rival” in one is found as “rival”:”character” somewhere.
"""

def pair_rivals(dict1, dict2):
    newdict = {}
    tup = ()
    for char in dict1.keys():
        if dict1[char] in dict2.keys():
            if dict2[dict1[char]] == char:
                tup = (char, dict1[char])
                newdict[tup] = True
    return newdict

"""
Function name: zoo_keeper
Parameters: list
Returns: dict
Description: Write a function called zoo_keeper that takes in a list of tuples
with the animal’s type, the animal’s species and the number of each animal.
You should return a dictionary with the animal’s type as a key and a dictionary
with the species and the number of each animal as its value. If an animal’s type
or species appears more than once, you should add the population to the existing
animal. All tuples will be completely lower cased.

"""
def zoo_keeper(list):
    dictionary = {}
    tempdict = {}
    types = []
    for tup in list:
        if tup[0] not in types:
            types.append(tup[0])
    for i in types:
        for tup in list:
            if i == tup[0] and  tup[1] not in tempdict:
                tempdict[tup[1]] = tup[2]
            elif i == tup[0] and tup[1] in tempdict:
                tempdict[tup[1]] += tup[2]
            dictionary[i] = tempdict
        tempdict = {}
    return dictionary

"""
Function name: animal_locator
Parameters: dict
Returns: dict
Description: Write a function called animal_locator that takes in a dictionary
containing zoo locations as keys and their values being a list of tuples with the
specific animal and the population of that specific animal at that zoo. You should
return a dictionary containing the animals as keys and their values being a tuple
with their first element being an ordered list of all the zoo locations based on
how many animals are at each location (greatest to least) and the second element
being an integer of the total population of that specific animal.
You do not have to take in account case sensitivity. 

"""

#return {'animal': (['place'].sorted(pop), totalPop)} 
def animal_locator(dict):
    aniCounts = list(dict.values())
    places = list(dict.keys())
    newdict = {}
    finaldict = {}
    plist = []
    total = 0
    for i in range(len(aniCounts)):
        for (animal, count) in aniCounts[i]:
            if animal in newdict.keys():
                newdict[animal].append((places[i], count))
            else:
                newdict[animal] = [(places[i], count)]
    for each in newdict.keys():
        newdict[each] = sorted(newdict[each], key=lambda x: x[1], reverse = True)
        plist = [p for (p, n) in newdict[each]]
        for (p, n) in newdict[each]:
            total += n
        finaldict[each] = (plist, total)
        total = 0
    return finaldict
        

print(animal_locator({'San Diego': [('lion', 4), ('snake', 4), ('tiger', 4)],
                'Phoenix': [('lion', 4), ('snake', 4), ('bee', 4)],
                'Seattle': [('bee', 4), ('tiger', 4)]}))
# return {'lion': (['San Diego', 'Phoenix'], 8),
#         'snake': (['San Diego', 'Phoenix'], 8),
#         'tiger': (['San Diego', 'Seattle'], 8,
#         'bee': (['Phoenix', 'Seattle'], 8)}
print(animal_locator({'Winter Garden': [('chicken', 4), ('pig', 2), ('cow',8)],
                'Ocoee': [('chicken', 20), ('snake', 5), ('pig', 1)],
                'Windermere':[('chicken', 3), ('snake', 2), ('bee', 4500)],
                'Gainesville': [('bee', 234),('pig', 123)]}))
# return {'chicken': (['Ocoee', 'Winter Garden', 'Windermere'], 27),
#         'pig': (['Gainesville', 'Winter Garden', 'Ocoee'], 126),
#         'cow': (['Winter Garden'], 8,
#         'snake': (['Ocoee', 'Windermere'], 7),
#         'bee': (['Windermere', Gainesville], 4734)}
