

class Student:

    def __init__(self,studId,name):
        '''
        fields:
        :param studId:int
        :param name: string
        :return:
        '''
        self.__id=studId
        self.__name=name

    def get_id(self):
        '''
        getter for id
        :return: id
        '''
        return self.__id

    def get_name(self):
        '''
        getter for name
        :return: name string
        '''
        return self.__name

    def __repr__(self):
        '''
        formater for string
        :return:
        '''
        return "STUDENT ID:{0}  NAME:{1}".format(self.get_id(),self.get_name())

    def __eq__(self, other):
        '''
        verifies equality of identity
        :param other:object type student
        :return:
        '''
        return self.__id == other.get_id()

