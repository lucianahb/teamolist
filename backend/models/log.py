class Log:

    def __init__(self,datetime: str, action: str, id: int = None):
        self.__id = id
        self.__datetime = datetime
        self.__action = action
    
    @property
    def id(self) -> int:
        return self.__id

    @property
    def datetime(self) -> str:
        return self.__datetime
    
    @property 
    def action(self) -> str:
        return self.__action
    
    @id.setter
    def id(self, id: int) -> None:
        self.__id = id
    
    @datetime.setter
    def datetime(self, datetime: str) -> None:
        self.__datetime = datetime
    
    @action.setter
    def action(self, action: str) -> None:
        self.__action = action