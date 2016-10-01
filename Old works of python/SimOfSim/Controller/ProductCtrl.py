
from Domain.Product import *

class ProductCtrl:


    def __init__(self,repo):
        '''
        contructor for controller
        :param repo: ProductRepo type
        :return: nothing
        '''

        self.__repo=repo

    def add(self,name,pType,quantity):
        '''
        creates the entity and then adds it to the repository
        :param name: string
        :param pType: string
        :param quantity: string(which will be converted into an int if ready)
        :return: nothing
        '''
        prod=Product(name,pType,quantity)

        self.__repo.add(prod)

    def update(self,name,pType,quantity):
        '''
        receives the atributes and cretes the entity Product type
        :param name: string
        :param pType: string
        :param quantity: string which will be converted into int if good
        :return:
        '''
        prod=Product(name,pType,quantity)

        self.__repo.update(prod)

    def get_all(self):
        '''
        gets all the elements in repository
        :return: list with elements
        '''
        return self.__repo.get_all()

    def getAllByType(self,iType):
        '''
        gets a list with elements with certain type
        :param iType: string , the type by which we filter
        :return: list with objects type Product
        '''
        return self.__repo.getAllByType(iType)

    def remv(self,iName,iType):

        self.__repo.remv(iName,iType)

