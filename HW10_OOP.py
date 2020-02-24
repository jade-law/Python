"""
Georgia Institute of Technology - CS1301
HW10 - OOP
"""

__author__ = """ Jade Law """
__collab__ = """  """

class Food:
    """
    Function name: __init__
    Parameters: str, float, list, str, int
    """
    def __init__(self, name, price, ingredients, food_type, calories):
        self.name = name
        self.price = round(price,2)
        self.ingredients = ingredients
        self.food_type = food_type
        self.calories = calories


    """
    Function name: __eq__
    Parameters: Food object, Food object
    Returns: boolean
    """
    def __eq__(self, other):
        if self.name == other.name and self.price == other.price and self.food_type == other.food_type and self.calories == other.calories:
            for ing in self.ingredients:
                if ing in other.ingredients:
                    continue
                else:
                    return False
            return True
        else:
            return False

    """
    Function name: __str__
    Parameters: Food object
    Returns: str
    """
    def __str__(self):
        return "{} is a {} that costs ${}.".format(self.name, self.food_type, self.price)

    """
    Do not modify __repr__ function.
    Leave it in for testing purposes and when
    turning in your HW.
    """
    def __repr__(self):
        return f"{self.name}: {self.price}: {self.food_type}: {self.calories}"

class Menu:
    """
    Function name: __init__
    Parameters: list, list, list
    Remember to also initialize total_items
    """
    def __init__(self, appetizer_list, entree_list, dessert_list):
        self.appetizer_list = appetizer_list
        self.entree_list = entree_list
        self.dessert_list = dessert_list
        self.total_items = len(self.appetizer_list) + len(self.entree_list) + len(self.dessert_list)

    """
    Function name: delete_items
    Parameters: list of Food objects
    Returns: tuple in the following format: (int, boolean)
    """
    def delete_items(self, foods):
        num = 0
        for food in foods:
            if food.food_type == "appetizer" and food in self.appetizer_list:
                i = self.appetizer_list.index(food)
                del self.appetizer_list[i]
                num += 1
            elif food.food_type == "entree" and food in self.entree_list:
                i = self.entree_list.index(food)
                del self.entree_list[i]
                num += 1
            elif food.food_type == "dessert" and food in self.dessert_list:
                i = self.dessert_list.index(food)
                del self.dessert_list[i]
                num += 1
        self.total_items -= num
        if num == len(foods):
            return (num, True)
        else:
            return (num, False)

    """
    Function name: add_items
    Parameters: list of Food objects
    Returns: str
    """
    def add_items(self, foods):
        num = 0
        for food in foods:
            if food.food_type == "appetizer" and food not in self.appetizer_list:
                self.appetizer_list.append(food)
                num += 1
            elif food.food_type == "entree" and food not in self.entree_list:
                self.entree_list.append(food)
                num += 1
            elif food.food_type == "dessert" and food not in self.dessert_list:
                self.dessert_list.append(food)
                num += 1
        self.total_items += num
        return "You have added {} items to your menu. Your menu now contains {} total items.".format (num, self.total_items)

    """
    Function name: __str__
    Parameters: Menu object
    Returns: str
    """
    def __str__(self):
        return "There are {} items on the menu. Appetizers are {}. Entrees are {}. Desserts are {}.".format(self.total_items, self.appetizer_list, self.entree_list, self.dessert_list)

    """
    Do not modify __repr__ function.
    Leave it in for testing purposes.
    """
    def __repr__(self):
        return f"Menu: {self.total_items} items"

class Customer:
    """
    Function name: __init__
    Parameters: str, float/int, boolean, list, Server object
    """
    def __init__(self, name, wallet, is_vegetarian, allergies, server):
        self.name = name
        self.wallet = round(wallet,2)
        self.is_vegetarian = is_vegetarian
        self.allergies = allergies
        self.server = server

    """
    Function name: place_order
    Parameters: list of Food objects, Menu object
    Returns: boolean
    """
    def place_order(self, foods, menu):
        totalPrice = 0.0
        for food in foods:
            if food not in menu.appetizer_list or food not in menu.entree_list or food not in menu.dessert_list:
                return False
            for ing in food.ingredients:
                if ing in self.allergies:
                    return False
            totalPrice += food.price
        if self.wallet - totalPrice < 0:
            return False
        else:
            self.wallet -= totalPrice
            return True

    """
    Function name: change_servers
    Parameters: Server object
    """
    def change_servers(self, new_server):
        self.server.total_tips -= 5
        new_server.total_tips += 5
        i = self.server.customer_list.index(self)
        del self.server.customer_list[i]
        self.server = new_server
        self.server.customer_list.append(self)

    """
    Function name: give_tip
    Parameters: int
    """
    def give_tip(self, tip):
        if tip < self.wallet:
            self.server.total_tips += tip
            self.wallet -= tip
            i = self.server.customer_list.index(self)
            del self.server.customer_list[i]

    """
    Function name: __str__
    Parameters: Customer object
    Returns: str
    """
    def __str__(self):
        return "{} has ${} and has allergies to {}. Server is {}".format(self.name, self.wallet, self.allergies, self.server.name)

    """
    Do not modify __repr__ function.
    Leave it in for testing purposes.
    """
    def __repr__(self):
        return f"{self.name}: ${self.wallet}, {self.is_vegetarian}, {self.allergies}, {self.server.name}"

class Server:
    """
    Function name: __init__
    Parameters: str, list of Customer objects, int, str
    Remember to also initialize total_tips
    """
    def __init__(self, name, customer_list, restaurant):
        self.name = name
        self.customer_list = customer_list
        self.total_tips = 0
        self.restaurant = restaurant

    """
    Function name: done_serving
    Parameters: list of Customer objects
    Returns: str
    """
    def done_serving(self, customers):
        for customer in customers:
            if customer in self.customer_list:
                i = self.customer_list.index(customer)
                del self.customer_list[i]
            else:
                self.customer_list.append(customer)
        return "{} still has {} customers waiting to be served.".format(self.name, str(len(self.customer_list)))

    """
    Function name: __str__
    Parameters: Server object
    Returns: str
    """
    def __str__(self):
        return "{} is a server.".format(self.name)

    """
    Do not modify __repr__ function.
    Leave it in for testing purposes.
    """
    def __repr__(self):
        return f"server: {self.name}, tips: {self.total_tips}, restaurant: {self.restaurant}"

