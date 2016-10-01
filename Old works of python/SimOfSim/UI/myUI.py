
from Domain.ValidityWorld import *

class Console:


    def __init__(self,ctrl):
        '''
        contructor for console
        :param ctrl: controller
        :return:
        '''
        self.__ctrl=ctrl


    def __add(self):
        '''
        adds a product
        :return:
        '''
        name=input("Introduce name:")
        pType=input("Introduce a type:")

        quantity=input("Introduce quantity:")

        try:
            self.__ctrl.add(name,pType,quantity)
        except ObjectException as e:
            print(e)


    def __update(self):
        '''
        updated a product
        :return:
        '''
        name=input("Introduce name:")
        pType=input("Introduce a type:")

        quantity=input("Introduce quantity:")
        try :
            self.__ctrl.update(name,pType,quantity)
        except ObjectException as e:
            print(e)


    def __show_all(self):
        '''
        shows all elements
        :return:
        '''
        lst=self.__ctrl.get_all()
        for obj in lst :
            print(obj)

    def __showByType(self):
        '''
        shows all elements by type in alphabetical order by name
        :return:
        '''
        iType=input("Introduce type by which we will sort:")
        lst=self.__ctrl.getAllByType(iType)
        if len(lst) > 0 :
            lst.sort(key=lambda x:x.get_name())
            for obj in lst :
                print(obj)
        else : print("There is no element with the wanted type")

    def __remv(self):
        """
        deletes an object from the repository
        :return:
        """
        iName=input("Introduce name :")
        iType=input("Introduce type :")
        try:
            self.__ctrl.remv(iName,iType)
        except ObjectException as e:
            print(e)


    @staticmethod
    def menu():
        myMenu="""
        1---add
        2---update
        3---Show all
        4---Show by type
        5---Delete
        0---exit
"""
        print(myMenu)

    def main(self):
        Console.menu()
        option = "1"
        while not option == "0" :
            option=input("Introduce your option:")

            if option == "1" :

                self.__add()

            if option == "2":

                self.__update()

            if option == "3":

                self.__show_all()

            if option == "4":

                self.__showByType()

            if option == "5" :

                self.__remv()