

class Task:


    def __init__(self,taskId,text,status):

        self.__id=taskId
        self.__text=text
        self.__status=status

    def get_id(self):

        return self.__id

    def get_status(self):

        return self.__status

    def get_text(self):

        return self.__text

    def set_status(self,value):

        self.__status=value

    def set_text(self,value):

        self.__text=value

    def __str__(self):

        return "ID:{0}  TEXT:{1}    STATUS:{2}".format(self.get_id(),self.get_text(),self.get_status())

