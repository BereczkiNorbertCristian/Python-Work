


class PurchasedP:

    def __init__(self):

        self.__data=[]

    def add_purchase(self,product):
        '''
        adds a product to the container of the purchased items
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

    def get_purchased(self):
        '''
        returns the list of purchases
        :return:
        '''
        return self.__data