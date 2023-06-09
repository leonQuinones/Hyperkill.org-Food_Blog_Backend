from collections import namedtuple

from Model.abstract_model import Model


class Ingredient(Model):
    @staticmethod
    def _get_model_fields() -> tuple:
        class_fields = ('ingredient_id', 'ingredient_name')
        return class_fields

    def __init__(self, args: namedtuple):
        self.ingredient_id = args.ingredient_id
        self.ingredient_name = args.ingredient_name
