"""
Georgia Institute of Technology - CS1301
HW07 - APIs and JSON
"""
__author__ = """ Jade Law """
__collab__ = """ I worked with Rashmi Athavale """

import requests

"""
Function name: currencyConverter
Parameters: country (string), money (int or float), conversionFactor (int or
float)
Returns: string indicating either that the function errored or the monetary
conversion
Description: An important aspect of traveling is money! Write a function that
takes in the name of the country you’re traveling to, the amount of money to
convert, and the conversion factor, and return a string of the format
"In [country name], $[money] USD is worth [foreign currency symbol][money times
currency factor, rounded to 2 decimal places] [three-letter foreign currency
code]." Your code should be able to handle an invalid country name and instead
of erroring, should return "[country name] is not a valid country."
"""

def currencyConverter(country, money, conversionFactor):
    baseURL = "https://restcountries.eu/rest/v2/name/"
    countryURL = baseURL + country.lower()
    r = requests.get(countryURL)
    data = r.json()
    newstring = ""
    converted = 0
    if data == {'status': 404, 'message': 'Not Found'}:
        newstring = country + " is not a valid country."
    else:
        converted = round(money*conversionFactor,2)
        newstring = "In {}, ${} USD is worth {}{} {}.".format(country, money, data[0]['currencies'][0]['symbol'], converted, data[0]['currencies'][0]['code'])
    return newstring

"""
Function name: translator
Parameters: codeList (list of strings)
Returns: dictionary where key and value are both strings
Description: Travelling around the world involves learning new languages! Write
a function that takes in a list of 3-letter codes representing a country and
return a dictionary where the key is the name of the country and the value is
the name of the country in its own language. Note that this function must be
able to ignore three letter codes that do not correspond to a country without
erroring. You can assume that we will not test strings that contain numbers.
Hint: The API will output something different if the country code is not valid.
Try using pprint with a request that uses an incorrect three-letter code and see
swhat it outputs!

"""

def translator(codeList):
    baseURL = "https://restcountries.eu/rest/v2/alpha/"
    newdict = {}
    for code in codeList:
        codeURL = baseURL + code.lower()
        r = requests.get(codeURL)
        data = r.json()
        if data == {'status': 404, 'message': 'Not Found'}:
            continue
        else:
            newdict[data['name']] = data['nativeName']
    return newdict

"""
Function name: nearbyLocations
Parameters: codeList (list of strings)
Returns: a list of tuples, each tuple containing floats
Description: You’ve finally eliminated the list of countries you’d like to visit
down to a few finalists and think that you’d get the most out of your money if
you could go somewhere with many other nearby places to visit. Write a function
that takes in a list of 3-letter codes representing a country, finds which
country has the most bordering countries, and returns a list of tuples
containing the latitude and longitude of its bordering countries. If there are
multiple countries with the same number of borders, use the one whose name
occurs last in the alphabet. If none of the countries have bordering countries,
return an empty list. Assume that all the country codes passed in will be valid.

Hint: You may need to request data more than once.
"""

def nearbyLocations(codeList):
    baseURL = "https://restcountries.eu/rest/v2/alpha/"
    newlist = []
    num = -1
    maxcountry = ""
    borders = []
    for i in range(len(codeList)):
        codeList[i] = codeList[i].lower()
    codeList = sorted(codeList, reverse = True)
    for code in codeList:
        codeURL = baseURL + code
        r = requests.get(codeURL)
        data = r.json()
        if len(data['borders']) > num:
            num = len(data['borders'])
            maxcountry = data['name']
            borders = data['borders']
        elif len(data['borders']) == num:
            continue
    for code in borders:
        codeURL = baseURL + code.lower()
        r = requests.get(codeURL)
        data = r.json()
        newlist.append(tuple(data['latlng']))
    return newlist

"""
Function name: humidityCheck
Parameters: locationsList (list of ints), maxHumidity (int)
Returns: list of strings or an error message as a string if an error occurs
Description: You have some suggestions for places to visit on your much-needed
vacation, but you don’t want to go somewhere that has too much humidity. Create
a function that takes in a list of location IDs (ints) and a max humidity (int)
and returns a list of cities (strings) that have humidities less than the max
humidity. If any of the IDs are invalid, return "[Location ID] is not a valid
ID".

Hint: Use the "Current weather data" to answer this question ("weather"
endpoint) and search by IDs

"""

def humidityCheck(locationsList, maxHumidity):
    baseURL = "https://api.openweathermap.org/data/2.5/weather?id="
    apikey = "&APPID=2b9fa1997782b89ed80da9e6b7953756"
    newlist = []
    for loc in locationsList:
        locURL = baseURL + str(loc) + apikey
        r = requests.get(locURL)
        data = r.json()
        if data == {'cod': '404', 'message': 'city not found'}:
            return str(loc) + " is not a valid ID"
        elif data['main']['humidity'] < maxHumidity:
            newlist.append(data['name'])
    return newlist

"""
Function name: locationTemps
Parameters: coordinatesList (list of tuples of floats)
Returns: list of tuples with the first item a string and the second item a float
Description: You are given some possible locations to visit, but you want to
know the temperatures of the locations so that you can plan accordingly. Create
a function that takes in a list of tuples that contain a latitude (float) and
longitude (float) and returns a list of tuples whose first item is the name of
the location (string) and the second item is the current temperature of that
location (float). The returned list should be sorted by temperatures from low to
high. Assume all coordinates are valid latitudes and longitudes.

Hint: Use the "Current weather data" to answer this question ("weather"
endpoint) and search by latitude and longitude. You can also use the
nearbyLocations() function to create your parameters to test!

"""

def locationTemps(coordinatesList):
    lat = 0
    long = 0
    baseURL = "https://api.openweathermap.org/data/2.5/weather?"
    apikey = "&APPID=2b9fa1997782b89ed80da9e6b7953756"
    urlList = []
    newlist = []
    temps = []
    tuplist = []
    for coordinates in coordinatesList:
        lat = str(coordinates[0])
        long = str(coordinates[1])
        latlong = "lat={}&lon={}".format(lat,long)
        urlList.append(baseURL + latlong + apikey)
    for url in urlList:
        r = requests.get(url)
        data = r.json()
        temps.append(data['main']['temp'])
        tuplist.append((data['name'],data['main']['temp']))
    temps = sorted(temps)
    for temp in temps:
        for tup in tuplist:
            if temp == tup[1]:
                newlist.append(tup)
    return newlist

"""
Function name: typesOfWeather
Parameters: locationsList (list of ints)
Returns: dictionary with strings as keys and lists of strings as values or an
error message as a string if error occurs
Description: You want to know the types of weather of different locations so
that you can plan an amazing trip! Create a function that takes in a list of
location IDs (ints) and returns a dictionary that’s keys are types of weather
(string) and values are lists of the names of the locations (string) that have
that weather. If any of the IDs are invalid, return "[Location ID] is not a
valid ID".

Hint: Use the "Current weather data" to answer this question ("weather"
endpoint) and search by IDs

"""

def typesOfWeather(locationsList):
    baseURL = "https://api.openweathermap.org/data/2.5/weather?id="
    apikey = "&APPID=2b9fa1997782b89ed80da9e6b7953756"
    newdict = {}
    weatherType = []
    templist = []
    for loc in locationsList:
        locURL = baseURL + str(loc) + apikey
        r = requests.get(locURL)
        data = r.json()
        if data == {'cod': '404', 'message': 'city not found'}:
            return str(loc) + " is not a valid ID"
        elif data['weather'][0]['main'] not in weatherType:
            weatherType.append(data['weather'][0]['main'])
    for weather in weatherType:
        for loc in locationsList:
            locURL = baseURL + str(loc) + apikey
            r = requests.get(locURL)
            data = r.json()
            if data['weather'][0]['main'] == weather:
                templist.append(data['name'])
        newdict[weather] = templist
        templist = []
    return newdict
