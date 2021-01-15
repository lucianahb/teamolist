from backend.models.marketplace_model import Marketplace
from backend.dao.BD.base_dao import BaseDao


class MarketplaceDao(BaseDao):
    def create(self, model: Marketplace) -> None:
        query = f"INSERT INTO marketplace (name, description) VALUES ('{model.name}', '{model.description}');"
        super().execute(query)

    def read_all(self)->list:
        query = 'SELECT name, description, id FROM marketplace;'
        result_list = super().read(query)
        marketplaces = []
        for result in result_list:
            marketplaces.append(Marketplace(result[0], result[1], result[2]))
        return marketplaces

    def read_by_id(self, id: int) -> Marketplace:
        query = f'SELECT name, description, id FROM marketplace WHERE id = {id}'
        result = super().read(query)[0]
        marketplace = Marketplace(result[0],result[1],result[2])
        return marketplace

    def update(self, model: Marketplace) -> None:
        query = f"UPDATE marketplace SET name = '{model.name}', description = '{model.description}' WHERE id = '{model.id}'"
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"DELETE FROM marketplace WHERE id = '{id}'"
        super().execute(query)