"""
Georgia Institute of Technology - CS1301
HW09 Recursion
"""
__author__ = """ Jade Law """
__collab__ = """ I worked on some of the problems with Rashmi Athavale. """

"""
Function name: count_evens
Parameters: list
Returns: int
"""
def count_evens(numbers):
    count = 0
    if len(numbers) == 0:
        return count
    elif numbers[0]%2 == 0.0:
        count += 1
        return count+count_evens(numbers[1:])
    else:
        return count+count_evens(numbers[1:])

"""
Function name:flatten_list
Parameters: list
Returns: list
"""
def flatten_list(aList):
    if len(aList) == 0:
        return []
    if type(aList[0]) == list:
        result = flatten_list(aList[0])
    else:
        result = [aList[0]]
    return result + flatten_list(aList[1:])


"""
Function name: num_substrings
Parameters: string (str), substring (str)
Returns: int
"""
def num_substrings(string, substring):
    count = 0
    if len(string) < len(substring):
        return count
    elif string[0:len(substring)] == substring:
        count += 1
        return count + num_substrings(string[1:], substring)
    else:
        return count + num_substrings(string[1:], substring)

"""
Function name: profit
Parameters: dictionary (dict), brand name (str)
Returns: int/float or str
"""
def profit(dictionary, brand):
    if len(dictionary) > 0:
        for key in dictionary.keys():
            print(key)
            if key == brand:
                return dictionary[key][0]
            elif dictionary[key][1]:
                return profit(dictionary[key][1], brand)
    else:
        return brand + " could not be found."


"""
Function name:pascal_dictionary
Parameters: int
Returns: dict
"""
def pascal_dictionary(num):
    result = {}
    if num == 0:
        return {}
    elif num == 1:
        result[1] = [1]
        return result
    else:
        new_row = [1]
        result = pascal_dictionary(num-1)
        last_row = result[num-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result[num] = new_row
    return result

"""
Function name: minmax
Parameters: nums (list)
Returns: tuple
"""
def minmax(nums):
    if nums == []:
        return ()
    elif len(nums) == 1:
        return (nums[0], nums[0])
    else:
        tup = minmax(nums[1:])
        if tup[1] < nums[0]:
            tup = (tup[0], nums[0])
        elif tup[0] > nums[0]:
            tup = (nums[0], tup[1])
    return tup

