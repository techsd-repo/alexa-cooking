from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
from allrecipes import AllRecipes

app = Flask(__name__)
api = Api(app)


class search(Resource):
    def get(self, keyword, sort):
        #query
        query_options = {
        "wt": keyword
        "sort": sort #change this later
        }
        #Sort Info
        query_result = AllRecipes.search(query_options)
        main_recipe_url = query_result[0]['url']
        detailed_recipe = AllRecipes.get(main_recipe_url)
        #Send out json
        result = {'recipe_name': detailed_recipe['name'], 'ingredients': detailed_recipe['ingredients'], 'steps': detailed_recipe['steps']}
        return jsonify(result)

    api.add_resource(search, '/query')

    if __name__ == '__main__':
        app.run(port=5002)
