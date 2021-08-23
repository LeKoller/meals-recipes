from flask import Blueprint, request

from extensions.database import mongo
from resources.utils import insert_recipe_in_database, parse_json


views_bp = Blueprint('views', __name__)


@views_bp.route('/recipes', methods=['POST'])
def create_meal():
    recipe = request.json

    recipe_id = insert_recipe_in_database(recipe, mongo)

    if recipe_id == 'error':
        return {'error': 'Recipe already invented!'}, 400

    response = {'id': recipe_id}

    return response, 201


@views_bp.route('/recipes/<string:title>', methods=['GET'])
def get_recipe(title):
    recipe = mongo.db.meals.find_one_or_404({'title': title})

    return parse_json(recipe), 200


@views_bp.route('/recipes/several', methods=['POST'])
def create_several_meals():
    recipes = request.json
    ids = []

    for recipe in recipes:
        recipe_id = insert_recipe_in_database(recipe, mongo)

        if recipe_id == 'error':
            return {'error': 'One or more recipes already invented!'}, 400

        ids.append(recipe_id)

    response = {'ids': ids}

    return response, 201


@views_bp.route('/recipes/several', methods=['GET'])
def list_all_recipes():
    recipes = {'all_recipes': parse_json(list(mongo.db.meals.find()))}

    if recipes:
        return recipes, 200

    return 404
