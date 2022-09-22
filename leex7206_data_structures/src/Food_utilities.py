"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
Section: CP164 Winter 2022
__updated__ = '2022-01-15'
-------------------------------------------------------
"""
#Food_utilities
from Food import Food

def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    veg = False

    name = str(input('Name: '))
    origin = int(input(Food.origins()+"\n: "))
    is_vegetarian = str(input('Enter Y/N: '))

    if is_vegetarian == 'Y':
        veg = True

    calories = int(input('Calories: '))

    food = Food(name, origin, veg, calories)

    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    # 4
 
    strip = line.split('|')
    
    name = strip[0] 
    origin = int(strip[1])
    veg = strip[2] == "True" 
    cal = int(strip[3])
    
    Food1 = Food(name, origin, veg, cal)
    return(Food1)
    

def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    list = []
    
    for i in file_variable:
        list.append(read_food(i))
    
    return list
    

def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in foods:
        string = (f'''{i.name}|{i.origin}|{i.is_vegetarian}|{i.calories}\n''')
        file_variable.write(string)

    return 


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    list =[]
    for i in foods:
        if i.is_vegetarian:
            list.append(i)
            
    return list

def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    
    origins = []
    
    for i in foods:
        if i.origin == origin:
            origins.append(i)
    return origins
    

def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    list = []
    
    for i in foods:
        list.append(i.calories)
    
    return int(sum(list) / len(list))


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    
    return average_calories(by_origin(foods, origin))


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    string = f'''Food                                Origin       Vegetarian Calories
----------------------------------- ------------ ---------- --------\n'''
    
    foods.sort()
    
    for i in foods:
        if i.is_vegetarian:
            test = "True"
        else:
            test = "False"
        v = f"""{i.name:36}{Food.ORIGIN[i.origin]:<13}{test:>10} {i.calories:>8}\n"""
        string += v
    
    print(string)

    return None


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    list = []
    
    assert origin in range(-1, len(Food.ORIGIN))

    for i in foods:
        if origin != -1 and i.origin != origin:
            continue
        elif max_cals != 0 and i.calories > max_cals:
            continue
        elif is_veg != False and not i.is_vegetarian:
            continue
        list.append(i)
        
    return list