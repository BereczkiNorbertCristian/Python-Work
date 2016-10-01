
class Console:
    '''
    atributes:
    ---controller
    '''
    def __init__(self,ctrl):
        '''
        constructor for class console
        :param ctrl: controller
        :return:
        '''

        self.__ctrl=ctrl

    def __add(self):
        """
        adds an order
        :return:
        """
        drivId=int(input("Introduce driver's id:"))
        dist=int(input("Introduce order's distance:"))

        try :
            self.__ctrl.add(drivId,dist)
        except ValueError as e:
            print(e)

    def __compute(self):
        '''
        computes the sum of money a taxi driver earned by an id
        :return:
        '''
        drivId=int(input("Introduce driver's Id:"))

        sum=self.__ctrl.getSum(drivId)

        driver=self.__ctrl.findDriver(drivId)

        print("The Sum of:"+driver.get_name()+" is:"+str(sum*0.5))



    def menu(self):
        '''
        menu
        :return:
        '''
        stt="""
        1---Add an order
        2---Compute money by ID
        0---Exit

"""


        option="1"
        while not option == "0" :
            print(stt)
            option=input("Introduce your option:")

            if option == "1":
                self.__add()
            if option == "2":
                self.__compute()