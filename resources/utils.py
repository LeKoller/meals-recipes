import json
from bson import json_util


def parse_json(data):
    return json.loads(json_util.dumps(data))


def insert_recipe_in_database(recipe, mongo):
    title = recipe["title"]

    homonymous_recipe = mongo.db.meals.find_one({'title': title})

    if homonymous_recipe:
        return 'error'

    categoryIds = recipe["categoryIds"]
    affordability = recipe["affordability"]
    complexity = recipe["complexity"]
    imageUrl = recipe["imageUrl"]
    duration = recipe["duration"]
    ingredients = recipe["ingredients"]
    steps = recipe["steps"]
    isGlutenFree = recipe["isGlutenFree"]
    isVegan = recipe["isVegan"]
    isVegetarian = recipe["isVegetarian"]
    isLactoseFree = recipe["isLactoseFree"]

    id = mongo.db.meals.insert({
        "title": title,
        "categoryIds": categoryIds,
        "affordability": affordability,
        "complexity": complexity,
        "imageUrl": imageUrl,
        "duration": duration,
        "ingredients": ingredients,
        "steps": steps,
        "isGlutenFree": isGlutenFree,
        "isVegan": isVegan,
        "isVegetarian": isVegetarian,
        "isLactoseFree": isLactoseFree
    })

    return str(id)
