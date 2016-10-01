
from Domain.Order import *

class GenCtrl :

    def __init__(self,drivRepo,ordrRepo):
        '''
        contructor for gen controller
        :param drivRepo: drivers's repository
        :param ordrRepo: order repository
        :return:
        '''
        self.__drivRepo=drivRepo
        self.__ordrRepo=ordrRepo

    def add(self,drivId,dist):
        '''
        creates an object and adds it to the repo if good to go
        :param drivId:int driver's id
        :param dist: int distance
        :return:
        exceptions:raises valueexception if driver's id not found in driver's repo
        '''

        if self.__drivRepo.findById(drivId) == False :
            raise ValueError("Driver's Id not found in driver's file!!!")
        if dist <1 :
            raise ValueError("Order's distance smaller than 1!!!")

        ordr=Order(drivId,dist)

        self.__ordrRepo.add(ordr)


    def getSum(self,drivId):
        '''
        compoutes the sum of a driver's orders by his id
        :param drivId: int driver's id
        :return: sum-int the driver's sum of money
        '''
        lst=self.__ordrRepo.get_all()
        sum=0
        for obj in lst :
            if obj.get_drivId() == drivId :
                sum+=obj.get_dist()
        return sum

    def findDriver(self,drivId):
        """
        fetches the driver
        :param drivId: int driver's id
        :return: object type Driver
        """
        return self.__drivRepo.findDriver(drivId)

