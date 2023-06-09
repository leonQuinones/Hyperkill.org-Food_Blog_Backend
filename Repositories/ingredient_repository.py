from Model.ingredient.ingredient_entity import Ingredient
from Repositories.base_repository import BaseRepository
from Repositories.interfaces.interface_database_connection import IDataBaseClient


class IngredientRepository(BaseRepository):

    def __init__(self, database_connection: IDataBaseClient):
        super().__init__(database_connection, 'ingredients', Ingredient)
