

class DriverRepo:

    def __init__(self):
        '''
        constructor for driver repo
        :return:
        '''
        self.__list=[]

    def add(self,obj):
        """
        adds an entity
        :return:
        """
        self.__list.append(obj)

    def findDriver(self,drivId):
        '''
        :param drivId:int driver's id
        :return: object type driver
        '''
        lst=self.__list
        for obj in lst :
            if obj.get_drivId() == drivId :
                return obj

    def findById(self,drivId):
        """
        checks if the drivId is found in this repository
        :return:
        """

        for obj in self.__list :
            if obj.get_drivId() == drivId :
                return True

        return False

    def __len__(self):
        '''
        computes the length of the repo
        :return:int- the length
        '''
        return len(self.__list)