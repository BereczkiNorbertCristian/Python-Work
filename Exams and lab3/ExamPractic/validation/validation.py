


class StoreException(Exception):


    def __init__(self,msg):
        '''

        :param msg:string
        :return:
        '''
        self.__msg=msg

    def __str__(self):
        '''
        string formater
        :return:
        '''
        return self.__msg



class Validator:

    @staticmethod
    def validate(pId,name,quantity,price):
        '''
        Validates
        :param pId:string
        :param name: string
        :param quantity: string
        :param price: string
        :return:
        raises StorException if there are some errors
        '''

        errors=""

        #checks the name
        if name == "":

            errors+="Name must be non-empty!!!"
        #checks the id
        try:
            ppId=int(pId)
        except ValueError:
            errors+="Id not int format!!!"

        #checks the quantity and the price
        try:
            q=int(quantity)
            p=int(price)
            if q<1 or p<1 :
                errors+="Quantity and price must be positive integers!!!"
        except ValueError:
            errors+="Quantity and price must be positive integers!!!"


        if len(errors) > 0 :

            raise StoreException(errors)

    @staticmethod
    def validateIdQ(pId,quantity):
        '''

        :param pId: string product's id
        :param quantity: string
        :return:
        '''
        errors=""
        #checks the product's id and the quantity
        try:
            p1=int(pId)
            p2=int(quantity)
            if p2 <1 :
                errors+="Quantity is a negative number!!!"

        except ValueError :
            errors+="Id and quantity not integers!!!"

        if len(errors) > 0:
            raise StoreException(errors)
