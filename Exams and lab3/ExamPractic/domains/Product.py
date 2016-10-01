


class Product:


    def __init__(self,pId,name,quantity,price):
        '''

        :param pId:int
        :param name: string
        :param quantity: int
        :param price: int
        :return:
        '''
        self.__id=pId
        self.__name=name
        self.__quantity=quantity
        self.__price=price

    def get_id(self):
        '''
        getter for id
        :return: int id
        '''
        return self.__id

    def get_name(self):
        '''
        getter for name
        :return: string name
        '''
        return self.__name

    def get_quantity(self):
        '''
        getter for quantity
        :return: int quantity of the product
        '''
        return self.__quantity

    def get_price(self):
        '''
        getter for price
        :return: int price
        '''
        return self.__price

    def set_quantity(self,value):
        '''
        setter for quantity
        :param value: int
        :return:nothing
        '''
        self.__quantity=value

    def set_price(self,value):
        '''
        setter for price
        :param value: int the value with which price will be replaced
        :return:
        '''
        self.__price=value

    def __add__(self, other):
        '''
        defines addition of two object type products
        :param other: object type product
        :return: object type product self
        '''
        self.__quantity+=other.get_quantity()
        self.__price=other.get_price()
        return self

    def __repr__(self):
        '''
        defines string formating
        :return:string
        '''
        return "PRODUCT: ID:{0} NAME:{1}    QUANTITY:{2}    PRICE:{3}".format(self.__id,self.__name,self.__quantity,self.__price)

    def __eq__(self, other):
        '''
        defines equality of object type product
        :param other: object type product
        :return: True if equality defined holds
        False if equality defined doesn't hold
        '''
        return self.__id == other.get_id()




