"""
Georgia Institute of Technology - CS1301
HW08 - File I/O
"""
__author__ = """ Jade Law """
__collab__ = """ I worked on some of the problems with Rashmi Athavale. """

"""
Function name: get_roster
Parameters: filename (string)
Returns: Read in a file of any name, but assume it is in the format stated
above. Go through every line and make a list of tuples of all the students
in the class. The tuples will be formatted (FirstName, LastName). Return this
list. If the file is not found, catch a FileNotFoundError and return
“File is not found.” 
"""
def get_roster(filename):
    tuplist = []
    num = 0
    try:
        file = open(filename,"r")
        lines = file.readlines()
        for line in lines:
            if "," in line:
                line = line.strip()
                num = line.find(",")
                tuplist.append((line[:num], line[num+2:]))
            else:
                continue
        file.close()
        return tuplist
    except FileNotFoundError:
        return "File is not found."

"""
Function name: get_average
Parameters: filename (string), student (string)
Returns: A tuple with the name of the student (without the comma)
and their average for their exams
Description: Read in a file of any name but in the format as what is stated
above. For the student passed into the function, find the student and take
the average of their test scores. The average will be a float rounded to two
decimals. Return this data as a tuple in the format
(FirstName LastName, Average). If the student is not found in the file,
return “Student not found in file.”. If the file is not found, catch a
FileNotFoundError and return “File is not found.” 
"""
def get_average(filename, student):
    studentname = student.split()
    studentname = studentname[0] + ", " + studentname [1] + "\n"
    avgscore = 0
    try:
        file = open(filename,"r")
        lines = file.readlines()
        lines.append("\n")
        num = lines.index(studentname)
        lines = lines[num+1:]
        num = lines.index("\n")
        lines = lines[:num]
        for score in lines:
            num = score.find(":")
            score = float(score[num+2:])
            avgscore += score
        avgscore = round(avgscore/len(lines),2)
        file.close()
        return (student, avgscore)
    except FileNotFoundError:
        return "File is not found."
    except ValueError:
        file.close()
        return "Student not found in file."

"""
Function name: get_all_averages
Parameters: filename (string)
Returns: A dictionary representing a student as the key,
and their average on exams as the value
Description: Read in a file of any name but in the format as what is stated
above. For every student, make an entry in a dictionary where their first
name is the key and their average for their exams as the value. The file will
not have duplicate first names. The average will be a float rounded to two
decimals. If the file is not found, catch a FileNotFoundError and return
“File is not found.” 
"""

def get_all_averages(filename):
    newdict = {}
    name = ""
    score = 0
    testcount = 0
    try:
        file = open(filename,"r")
        lines = file.readlines()
        for line in lines:
            if "," in line:
                name = line[:line.find(",")]
            elif ":" in line:
                line = line.strip()
                score += float(line[line.find(":")+2:])
                testcount += 1
            else:
                newdict[name] = round(score/testcount,2)
                name = ""
                score = 0
                testcount = 0
        newdict[name] = round(score/testcount,2)
        file.close()
        return newdict
    except FileNotFoundError:
        return "File is not found."

"""
Function name: form_groups
Parameters: filename (string), current_student (string), num_per_team (int)
Returns: None
Description: Read in a file of any name but in the format as what is stated
above. If the file is not found, catch a FileNotFoundError and return
“File is not found.”. In a new file to write named group.txt, write
“Team StudentName” on one line, replacing StudentName with the name of the
current student passed in. Go through the file to find the top X-1 number
of students to add to your team, top being those with the highest averages.
X is the number passed in representing the maximum number of people per team,
and X-1 is the number of students selected on the team minus the current
student. The current student can not be one of the students added to the team.
If there are less than X number of students, then everyone in the file is
included on the team. However, the number of students in a team can not exceed
X. If X == 1, then just write the header on the file “Team StudentName”
and if X == 0, then do not write anything to the file. There will not be more
than one student with the same average. Each of these students will be a
separate line in the new file in the format of “Y) Student Name”, Y being a
number in a list in increasing order, going from 1 - the maximum number of
people per team. The top student will be 1, and then it will go down in
decreasing top scores. The last line of the file should not have a “\n”.
This function will return None unless there is an error.
"""
def form_groups(filename, current_student, num_per_team):
    studentname = current_student.split()
    studentname = studentname[0] + ", " + studentname [1] + "\n"
    score = 0
    testcount = 0
    studict = {}
    try:
        stufile = open(filename,"r")
        lines = stufile.readlines()
        lines.append("\n")
        for line in lines:
            if "," in line:
                name = line
            if name != studentname:
                if "," in line:
                    student = line.strip()
                    student = student[:line.find(",")]
                    student += line[line.find(",")+1:line.find("\n")]
                elif ":" in line:
                    line = line.strip()
                    score += float(line[line.find(":")+2:])
                    testcount += 1
                else:
                    studict[student] = round(score/testcount,2)
                    student = ""
                    score = 0
                    testcount = 0
        stufile.close()
        groupfile = open("group.txt","w")
        groupfile.write("Team " + current_student + "\n")
        if num_per_team-1 < len(studict.keys()):
            for i in range(num_per_team-1):
                highest = -1
                for name,avg in studict.items():
                    if avg > highest:
                        highest = avg
                        highestName = name
                groupfile.write("{}) {}\n".format(i+1, highestName))
                del studict[highestName]
        elif num_per_team-1 > len(studict.keys()):
            for i in range(len(studict.keys())):
                highest = -1
                for name,avg in studict.items():
                    if avg > highest:
                        highest = avg
                        highestName = name
                groupfile.write("{}) {}\n".format(i+1, highestName))
                del studict[highestName]
        groupfile.close()
    except FileNotFoundError:
        return "File is not found."
    
form_groups('files/CS1332.txt', 'Steve Jobs', 0)
"""
Function name: zero_calorie_diet
Parameters: filename (string)
Returns: A string representing the name of a dish
Description: Read in a file of any name but in the format as what is stated
above. If the file is not found, catch a FileNotFoundError and return
“File is not found.”. You are trying to go on a low calorie diet, so parse
through the file and return the name of the dish with the least amount of
calories. If two dishes have the same amount of calories, return the one that
occurred first. 
"""
def zero_calorie_diet(filename):
    try:
        file = open(filename,"r")
        heading = file.readline()
        lines = file.readlines()
        lowcal = 10000000000000
        for line in lines:
            line = line.split(",")
            line[2] = int(line[2])
            line = tuple(line)
            (name, price, cal, cuisine) = (line[0], line[1], line[2], line[3])
            if cal < lowcal:
                lowcal = cal
                lowfood = name
        file.close()
        return lowfood
    except FileNotFoundError:
        return "File is not found."

"""
Function name: erica_menu
Parameters: filename (string), num_of_dishes (int)
Returns: None
Description:  Read in a file of any name but in the format as what is stated
above. If the file is not found, catch a FileNotFoundError and return
“File is not found.”. Erica wants to put together an ideal menu for her,
consisting of the same or less number of items than the number passed in,
but never more. There are conditions, however, since she is broke and very
picky. Parse through the file and create a menu for Erica by choosing the
cheapest dishes. However, never put a Vegetarian dish on her menu, because
she will not eat it. What this means is that if there are 4 dishes on the
list, one being Vegetarian, and she wants 4 items on her menu, then her menu
will consist of 3 dishes. You will be writing this menu out onto a new file
named EricaMenu.txt. The first line of the file will be “Erica’s Menu” and
every corresponding line after that will be the Dish Name, Price, and Cuisine
Type all on the same line, with each dish being on a separate line.
Price will have a $ preceding the number and each element for a line, except
the last element, will be followed by a “, “ (comma and space). The last
line will not have a “\n”. This function will return None, unless there is an
error. 
"""
def erica_menu(filename, num_of_dishes):
    try:
        file = open(filename,"r")
        heading = file.readline()
        lines = file.readlines()
        menu = open("EricaMenu.txt.","w")
        menu.write("Erica's Menu\n")
        used = []
        foods = {}
        num = 0
        for line in lines:
            line = line.split(",")
            line[1] = float(line[1][1:])
            line[3] = line[3].strip()
            line = tuple(line)
            (name, price, cal, cuisine) = (line[0], line[1], line[2], line[3])
            if cuisine != "Vegetarian":
                foods[name] = (price, cuisine)
        for i in range(num_of_dishes):
            if len(foods) != 1:
                cheapest = 100000000
                for food in foods:
                    (price, cuisine) = (foods[food][0], foods[food][1])
                    if price < cheapest:
                        cheapest = price
                        cheapfood = food
                        cheapcuisine = cuisine
                menu.write("{}, ${}, {}\n".format(cheapfood, str(cheapest), cheapcuisine))
                del foods[cheapfood]
            else:
                for food in foods:
                    menu.write("{}, ${}, {}".format(food, foods[food][0], foods[food][1]))
                break
        file.close()
        menu.close()
    except FileNotFoundError:
        return "File is not found."

erica_menu('files/chikfila.csv', 0)
erica_menu('files/westvillage.csv', 10)
erica_menu('files/chikfila.csv', 4)
erica_menu('files/chikfila.csv', 10)
