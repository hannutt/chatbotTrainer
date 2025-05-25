from chatterbot import ChatBot


class Variables():
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.adaptions=False
        self.cbTime=ChatBot('Norman',storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3',logic_adapters=["chatterbot.logic.TimeLogicAdapter"])
        self.cbMath=ChatBot('Norman',storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3',logic_adapters=["chatterbot.logic.MathematicalEvaluation"])
        self.CbotNoAdaptions=ChatBot('Norman',storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')
        self.selection=""