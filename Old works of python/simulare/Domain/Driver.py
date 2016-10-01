

class Driver:
    '''
    attributes:
    ---drivId
    ---name
    methods:
    get_name
    get_drivId
    '''
    def __init__(self,drivId,name):
        '''
        constructor for driver type
        :return:
        '''
        self.__drivId=drivId
        self.__name=name

    def get_name(self):
        '''
        getter for name
        :return: string name
        '''
        return self.__name

    def get_drivId(self):
        '''
        getter for driver's id
        :return: int driver's id
        '''
        return self.__drivId