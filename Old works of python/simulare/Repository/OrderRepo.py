

class OrderRepo:

    def __init__(self):
        '''
        constructor
        :return:
        '''
        self.__list=[]

    def add(self,order):
        '''
        adds an order to the repository
        input:object type order
        :return:
        '''
        self.__list.append(order)

    def get_all(self):
        '''
        gets all elements in repository
        :return: list with elements
        '''
        return self.__list

    def __len__(self):
        '''
        computes the length of the repo
        :return:int- the length
        '''
        return len(self.__list)