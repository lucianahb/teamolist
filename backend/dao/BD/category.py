from backend.models.category import Category
from .base_dao import BaseDao


class CategoryDao(BaseDao):
    def create(self, category: Category) -> None:
        query = f"INSERT INTO category (name, description) VALUES ('{category.name}','{category.description}');"
        super().execute(query)

    def read_by_id(self, id:int)-> Category:
        query = f"SELECT ID, NAME, DESCRIPTION FROM CATEGORY WHERE ID = {id};"
        result = super().read(query)[0]
        category = Category(result[1],result[2] ,result[0])
        return category
        
    def read_all(self)->list:
        query = f"SELECT ID, NAME, DESCRIPTION FROM CATEGORY;"
        result_list = super().read(query)
        categories = []
        for result in result_list:
            category = Category(result[1],result[2] ,result[0])
            categories.append(category)
        return categories

    def delete(self, id:int)->None:
        query = f"DELETE FROM CATEGORY WHERE ID = {id};"
        super().execute(query)

    def update(self, category:Category)->None:
        query = f"""UPDATE CATEGORY 
                            SET 
                                NAME = '{category.name}',
                                DESCRIPTION = '{category.description}' 
                            WHERE ID = {category.id};
                            """
        super().execute(query)