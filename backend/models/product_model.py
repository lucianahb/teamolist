class Product:
    def __init__(self, name:str, description:str, price:float, id:int = None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def price(self) -> float:
        return self.__price

    @id.setter
    def id(self, id: int):
        self.__id = id

    @name.setter
    def name(self, name: str):
        self.__name = name

    @description.setter
    def description(self, description: str):
        self.__description = description

    @price.setter
    def price(self, price: float):
        self.__price = price