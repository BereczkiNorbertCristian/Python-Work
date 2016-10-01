

class Order :
    '''
    atributes:
    ---drivId
    ---dist
    methods:
    ---get_divId
    ---get_dist
    '''
    def __init__(self,drivId,dist):
        """
        constructor for order
        :return:
        """
        self.__drivId=drivId
        self.__dist=dist

    def get_drivId(self):
        '''
        getter for driver's id
        :return: int driver's id
        '''
        return self.__drivId

    def get_dist(self):
        '''
        getter for order's distance
        :return: int distance
        '''
        return self.__dist

    