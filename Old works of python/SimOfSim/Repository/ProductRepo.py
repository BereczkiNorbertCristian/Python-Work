

from Domain.Product import *
from Domain.ValidityWorld import *

class ProductRepo:

    def __init__(self,validator):
        """
        constructor for repository
        """
        self.__list=[]
        self.__validator=validator

    def add(self,obj):
        """
        adds an object to the existing list if it is not already there
        :param obj: object to be appended
        """

        if obj in self.__list :
            raise ObjectException("Object already in the list!!!")
        self.__validator.validate(obj)
        obj.set_q()
        self.__list.append(obj)

    def get_all(self):
        """
        :return:  a list with all the objects in repository
        """
        return self.__list

    def update(self,upObj):
        """
        updates an existing object
        :param upObj: object type Product with which we will update the existing object
        """
        self.__validator.validate(upObj)
        upObj.set_q()
        if not upObj in self.__list :
            raise ObjectException("Object to be updated not found!!!")

        lst=self.get_all()
        for obj in lst :
            if obj == upObj :

                if obj.get_q() < upObj.get_q():
                    raise ObjectException("Error: Too small of a quantity!!!")

                obj.update(upObj)

    def getAllByType(self,iType):
        '''
        gets all elements by a type
        :param iType: string , the type wanted
        :return: list with elements only with a specific type
        '''
        lst=[]
        for obj in self.__list :
            if obj.get_pType() == iType :
                lst.append(obj)

        return lst

    def find(self,name):

        for obj in self.__list :

            if obj.get_name() == name :
                return obj

        return False

    def remv(self,iName,iType):

        lst=self.get_all()
        for obj in lst :
            if obj.get_name() == iName and obj.get_pType() == iType :
                lst.remove(obj)
                return
