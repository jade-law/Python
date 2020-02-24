#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW02 - Return and Conditionals
"""
__author__ = """ Jade Law """
__collab__ = """ I worked on this assignment with Rashmi Athavale. """

"""
Function name: can_buy
Parameters: str, float, int
Returns: boolean 
Description: Write a function that takes in a stock’s ticker as a string, a wallet amount as a float,
and number of shares as an int. Given this information, calculate whether or not you can afford to buy that
number of shares of the particular stock given the amount in your wallet. If you can afford to buy that
number of shares that stock, return True; if you cannot, return False. If a ticker that is not present in
the table is passed through, return None. Assume the number of shares is a nonnegative integer. Case sensitivity
should not matter: “A” should be treated as “a”.

"""

amd_share = 23.98
xom_share = 79.62
tsla_share = 322.82
snap_share = 11.63

def can_buy(ticker, wallet, shares):
    ticker = str.upper(ticker)
    money = 0
    if ticker == "AMD":
        money = wallet - (shares * amd_share)
        return enough(money)
    elif ticker == "XOM":
        money = wallet - (shares * xom_share)
        return enough(money)
    elif ticker == "TSLA":
        money = wallet - (shares * tsla_share)
        return enough(money)
    elif ticker == "SNAP":
        money = wallet - (shares *  snap_share)
        return enough(money)
def enough(spent):
    if spent < 0:
        return False
    else:
        return True

"""
Function name: amount_spent
Parameters: str, float, int
Returns: float
Description: Write a function that takes in a stock’s ticker as a string, a wallet amount as a float, and
number of shares as an int. Given this information, use your can_buy function to determine whether or not
you can afford to buy the given number of shares of the given stock. If you can afford it, return the amount
you would spend if you bought that number of shares of that particular stock (rounded to two decimals).
If you cannot afford it or a ticker that is not present in the table is passed through, assume that you will
not buy any shares.  Case sensitivity should not matter. “A” should be treated as “a”.

"""

def amount_spent(ticker, wallet, shares):
    if can_buy(ticker, wallet, shares):
        if ticker.upper() == "AMD":
            return round(shares*amd_share,2)
        elif ticker.upper() == "XOM":
            return round(shares*xom_share,2)
        elif ticker.upper() == "TSLA":
            return round(shares*tsla_share,2)
        elif ticker.upper() == "SNAP":
            return round(shares*snap_share,2)
    else:
        return 0.0

"""
Function name: good_buy
Parameters: str
Returns: bool 
Description: Write a function that takes in a stock’s ticker as a string, a wallet amount as a float, and number
of shares as an int. Given this information, you should return whether or not a stock is a good buy. The definition
of a good buy is: given the current trend and reversal, the stock’s price will be increasing in the near future.
If the ticker passed in is not in the table then you should return False. Case sensitivity does not matter.
“A” should be treated as “a”.

"""

amdTrend = "Up"
xomTrend = "Down"
tslaTrend = "Up"
snapTrend = "Down"
amdReversal = True
xomReversal = False
tslaReversal = False
snapReversal = True

def good_buy(ticker):
    ticker = str.upper(ticker)
    if ticker == "AMD":
        return trendReversal(amdTrend, amdReversal)
    elif ticker == "XOM":
        return trendReversal(xomTrend, xomReversal)
    elif ticker == "TSLA":
        return trendReversal(tslaTrend, tslaReversal)
    elif ticker == "SNAP":
        return trendReversal(snapTrend, snapReversal)
    else:
        return False
def trendReversal(nameTrend, nameReversal):
    if (nameTrend == "Up" and nameReversal == False) or (nameTrend == "Down" and nameReversal == True):
        return True
    else:
        return False

"""
Function name: warren_buffet_buy
Parameters: str, int
Returns: None
Description: Warren Buffett is one of the the world’s most successful investors, because of this, he has a
different definition of what a “good buy” is. His definition is that the stock meets all the criteria from
the good_buy function, as well as that the stock’s industry is on his list of promising industries. His list
of promising industries includes the Semiconductor and Technology sectors. Write a function that takes in a
stock’s ticker as a string and a number of shares as an int. Given this information and the assumption that
Warren Buffett has $1,000,000 in his wallet, use the good_buy function to check if the stock meets the basic
criteria of a good buy, then determine whether or not the stock meets the remaining criteria of a Warren
Buffett buy. If a stock does not meet basic ‘good buy’ standards, print: "{ticker} does not meet basic 'good buy'
standards.". If the stock does meet basic ‘good buy’ standards, but it does not meet Warren Buffett’s definition
of a good buy (based on the industry), then print: "{ticker} does not meet Warren Buffett's industry standards.".
Since Warren Buffett is such a wealthy man, if you try to buy less than 500 shares of a stock then print:
"Warren Buffett wouldn't waste his time with {number_of_shares} shares.". If the stock is a Warren Buffett good
buy use the amount_spent  function to calculate the amount he spends and then print: "Warren Buffett would have
${1000000 - amount} remaining after buying {number_of_shares} shares of {ticker}.". 
"""

amdIndus = "Semiconductor"
xomIndus = "Emergy"
tslaIndus = "Automotive"
snapIndus = "Technology"
wallet = 1000000

def warren_buffet_buy(ticker, shares):
    if good_buy(ticker) == False:
        print("{} does not meet basic 'good buy' standards.".format(ticker))
    if ticker == "AMD":
        print(warrenGoodBuy(amdIndus, shares, ticker))
    elif ticker == "XOM":
        print(warrenGoodBuy(xomIndus, shares, ticker))
    elif ticker == "TSLA":
        print(warrenGoodBuy(tslaIndus, shares, ticker))
    elif ticker == "SNAP":
        print(warrenGoodBuy(snapIndus, shares, ticker))
    elif shares < 500:
        print("Warren Buffett wouldn't waste his time with {} shares.".format(shares))
        

def warrenGoodBuy(industry, shares, ticker):
    if industry == "Semiconductor" or industry == "Technology":
        amount = amount_spent(ticker, wallet, shares)
        remaining = wallet - amount
        return "Warren Buffett would have ${} remaining after buying {} shares of {}.".format(remaining, shares, ticker)
    else:
        return "{} does not meet Warren Buffett's industry standards.".format(ticker)

"""
Function name: temperature
Parameters: int
Returns: string
Description: Write a function that takes in the temperature, an int. If the temperature is 90 or above return
“It’s over 9,000!!!”. If the temperature is less than 90 but 75 or above return: “Can it stay like this?”.
If the temperature is less than 75 but 40 or above return: “Okay not too low now.”. If the temperature is less
than 40 but 32 or above return: “Can it be 90 again?”. If the temperature is less than 32 return: “We’re in Georgia
not Antarctica.”

"""

def temperature(temp):
    if temp >= 90:
        return "It's over 9,000!!!"
    elif temp >= 75:
        return "Can it stay like this?"
    elif temp >= 40:
        return "Okay not too low now."
    elif temp >= 32:
        return "Can it be 90 again?"
    else:
        return "We're in Georgia not Antarctica."

"""
Function name: attack
Parameters: str, str
Returns: string
Description: Write a function that takes in two parameters - the first string is the name of the attacking pokemon
and the second string isthe name of the defending pokemon. The attacking pokemon will lower the defending pokemon’s
hp by the amount of their attack. However, if the attacking pokemon’s type is the weakness of the defending pokemon
then lower the defending pokemon’s hp by 1.1 times the attack of the attacking pokemon. Return a string of the
format: "{attacker} lowered {defender}'s hp to {hp after attack}." If one of the parameters is not in the table
return a string of the format: “No information on this.” Case sensitivity does not matter:
“A” should be treated as “a”. You can assume the defending pokemon is at max hp.

"""

charHp = 188
squirtHp = 198
bulbHp = 200
charAtk = 98
squirtAtk = 90
bulbAtk = 92
atkMultiplier = 1.1

def attack(atkPokemon, defPokemon):
    attacking = str.lower(atkPokemon)
    deffending = str.lower(defPokemon)
    if attacking == "charmander":
        if deffending == "squirtle":
            return atkMath(atkPokemon, defPokemon, squirtHp, charAtk)
        elif deffending == "bulbasaur":
            return atkWeakness(atkPokemon, defPokemon, bulbHp, charAtk)
    if attacking == "squirtle":
        if deffending == "charmander":
            return atkWeakness(atkPokemon, defPokemon, charHp, squirtAtk)
        elif deffending == "bulbasaur":
            return atkMath(atkPokemon, defPokemon, bulbHp, squirtAtk)
    if attacking == "bulbasaur":
        if deffending == "charmander":
            return atkMath(atkPokemon, defPokemon, charHp, bulbAtk)
        elif deffending == "squirtle":
            return atkWeakness(atkPokemon, defPokemon, squirtHp, bulbAtk)
    else:
        return "No information on this."
def atkMath(atkPokemon, defPokemon, defHp, Atk):
    newHp = round(defHp - Atk,1)
    return "{} lowered {}'s hp to {}.".format(atkPokemon, defPokemon, newHp)
def atkWeakness(atkPokemon, defPokemon, defHp, Atk):
    newHp = round(defHp - (Atk * atkMultiplier),1)
    return "{} lowered {}'s hp to {}.".format(atkPokemon, defPokemon, newHp)

"""
Function name: adopt
Parameters: str, str
Returns: str
Description: Write a function that takes in two strings, one being the name of one pokemon and the other being
the name of another pokemon, and compares the corresponding pokemon to see which one you adopt! You would want
to adopt the pokemon with higher combined stats: hp + attack + level. If there is a tie, you will adopt the first
pokemon. Return a string of the format: “You adopted [the pokemon you adopted]!”. If one of the parameters is not
a pokemon on the list then return the string: “No information on one of these pokemon.” Case sensitivity does not
matter.
"""

charLevel = 100
squirtLevel = 95
bulbLevel = 90
charTotal = charAtk + charHp + charLevel
squirtTotal = squirtAtk + squirtHp + squirtLevel
bulbTotal = bulbAtk + bulbHp + bulbLevel

def adopt(one, two):
    pokeOne = str.lower(one)
    pokeTwo = str.lower(two)
    if pokeOne == "charmander" and pokeTwo == "squirtle":
        return compute(one, two, charTotal, squirtTotal)
    elif pokeOne == "charmander" and pokeTwo == "bulbasaur":
        return compute(one, two, charTotal, bulbTotal)
    elif pokeOne == "squirtle" and pokeTwo == "bulbasaur":
        return compute(one, two, squirtTotal, bulbTotal)
    elif pokeOne == "squirtle" and pokeTwo == "charmander":
        return compute(one, two, squirtTotal, charTotal)
    elif pokeOne == "bulbasaur" and pokeTwo == "charmander":
        return compute(one, two, bulbTotal, charTotal)
    elif pokeOne == "bulbasaur" and pokeTwo == "squirtle":
        return compute(one, two, bulbTotal, squirtTotal)
    else:
        return "No information on one of these pokemon."
def compute(one, two, total1, total2):
    if total1 >= total2:
        return "You adopted {}!".format(one)
    elif total1 < total2:
        return "You adopted {}!".format(two)
