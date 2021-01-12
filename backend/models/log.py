class Log:

    def __init__(self,datetime: str, action: str, id: int = None):
        self.id = id
        self.datetime = datetime
        self.action = action