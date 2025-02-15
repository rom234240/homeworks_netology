from pprint import pprint

def parse_recipes(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            if line.strip():
                lines.append(line.strip())

    index = 0
    while index < len(lines):
        dish_name = lines[index]
        index += 1

        num_ingredients = int(lines[index])
        index += 1

        ingredients = []
        for _ in range(num_ingredients):
            parts = [part.strip() for part in lines[index].split('|')]
            ingredient = {
            'ingredient_name': parts[0],
            'quantity': int(parts[1]),
            'measure': parts[2]
            } 
            ingredients.append(ingredient)
            index += 1
        
        cook_book[dish_name] = ingredients

    return cook_book

pprint(parse_recipes('recipes.txt'), width = 120)