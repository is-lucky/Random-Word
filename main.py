from flask import Flask
from flask_restful import Api, Resource
import random

app = Flask(__name__)
api = Api(app)

class Message(Resource):
    def get(self):
        list_of_words = ["apple", "banana", "grape", "orange", "lion", "tiger", "bear", "football", "soccer", "hockey", "basketball", "baseball", "ranger", "viking", "eagle", "spartan", "warrior", "cowboy", "panther", "thunder", "lightning", "mountain", "river", "valley", "iron", "steel", "forge", "ideal", "valor", "wisdom", "greatness", "magnanimity", "chivalry", "honor", "family", "wonder", "health", "spirit", "liberty", "freedom", "law", "rules", "chemistry", "biology", "philosophy", "politics", "democracy", "republic", "aristocracy", "kingdom", "tyranny", "oligarchy", "anarchy", "utility", "pragmatism", "leadership", "goal", "vision", "genius", "luck", "fortune", "people", "influence", "tribune", "consul", "praetor", "censor", "assembly", "popular", "reform", "land", "military", "civil", "contest", "victory", "triumph", "school", "public", "private", "city", "rural", "urban", "commerce", "dialogue", "generosity", "charity", "sweater", "vacuum", "bottle", "key", "frame", "audio", "visual", "computer", "paper", "plant", "dog", "best", "winner", "maverick", "big", "little", "book", "video", "federalism", "team", "element","market", "monkey", "modern", "gorilla", "harness", "sky", "earth", "space", "rocket", "knight", "night", "solar", "cosmos", "speed", "flight", "rapid", "total", "recall", "recursion", "random", "atom", "ultimate", "soldier", "infinite", "novice", "veteran"]
        return random.choice(list_of_words)

api.add_resource(Message, "/get word")

if __name__ == "__main__":
    app.run(debug=True)