class Category:

    def __init__(self,name: str, description: str, id: int = None):
        self.__id = id
        self.__name = name
        self.__description = description
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def description(self) -> str:
        return self.__description
    
    @id.setter
    def id(self, id: int) -> None:
        self.__id = id
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    
    @description.setter
    def description(self, description: str) -> None:
        self.__description = description