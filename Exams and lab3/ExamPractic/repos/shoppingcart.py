

class ShoppingCart:

    def __init__(self):
        '''
        data:=container for object type products
        :return:
        '''
        self.__data=[]

    def add_shoppingCart(self,product):
        '''
        adds a product to the container of the shopping cart
        if list has no object the the we append directly a product
        then we check if the product is already in the container if yes the we update it
        :param product:object type product
        :return:
        '''

        if len(self.__data) == 0 :
            self.__data.append(product)
        else:

            if product in self.__data :
                for p in self.__data :
                    if p == product:
                        p=p+product

            else :
                self.__data.append(product)


    def clear_cart(self):
        '''
        clears the cart
        :return:
        '''
        self.__data=[]

    def get_cart(self):
        '''
        returns container cart
        :return:
        '''
        return self.__data