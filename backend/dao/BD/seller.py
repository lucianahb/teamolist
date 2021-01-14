from backend.models.seller import Seller
from .base_dao import BaseDao


class SellerDao(BaseDao):
    def create(self, seller: Seller) -> None:
        query = f"""INSERT INTO seller (name, phone, mail) 
                    VALUES ('{seller.name}','{seller.phone}','{seller.email}');
                    """
        super().execute(query)

    def read_by_id(self, id:int)-> Seller:
        query = f"SELECT ID, NAME, PHONE, MAIL FROM seller WHERE ID = {id};"
        result = super().read(query)[0]
        seller = Seller(result[1],result[2] ,result[3], result[0])
        return seller

    def read_all(self)->list:
        query = f"SELECT ID, NAME, PHONE, MAIL FROM SELLER;"
        result_list = super().read(query)
        sellers = []
        for result in result_list:
            seller = Seller(result[1],result[2] ,result[3], result[0])
            sellers.append(seller)
        return sellers

    def delete(self, id:int)->None:
        query = f"DELETE FROM SELLER WHERE ID = {id};"
        super().execute(query)

    def update(self, seller:Seller)->None:
        query = f"""UPDATE seller 
                            SET 
                                NAME = '{seller.name}',
                                MAIL = '{seller.email}',
                                PHONE = '{seller.phone}'
                            WHERE ID = {seller.id};
                            """
        super().execute(query)