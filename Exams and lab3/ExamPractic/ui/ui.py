
from validation.validation import StoreException

class Console:

    def __init__(self,ctrl):

        self.__ctrl=ctrl

    def show_inventory(self):

        products=self.__ctrl.get_inventory()

        for product in products:
            print(product)

    def show_cart(self):

        cart=self.__ctrl.get_cart()

        for product in cart:

            print(product)

    def add_inventory(self):
        try:
            pId=input("Introduce product Id:")
            name=input("Introduce name:")
            quantity=input("Introduce quantity for product:")
            price=input("Introduce price per product:")
            self.__ctrl.add_inventory(pId,name,quantity,price)
        except StoreException as e:
            print("")
            print(e)

    def add_cart(self):

        try :
            pId=input("Id of the product:")
            quantity=input("Quantity of the product:")
            self.__ctrl.add_cart(pId,quantity)
        except StoreException as e:
            print(e)

    def show_purchase(self):

        purchase=self.__ctrl.get_purchased()

        for product in purchase :
            print(product)

    def finalize(self):

        cost=self.__ctrl.get_cartCost()
        print("The grand total cost of the shopping cart is:{0}".format(cost))
        decision=input("Do you want to purchase these product ?(yes/no):")
        if decision.strip() == "yes" :
            self.__ctrl.purchase()
        else:
            self.__ctrl.notpurchase()

    def income(self):

        totalIncome=self.__ctrl.income()

        print("The Store's Income is :{0}".format(totalIncome))

    def report(self):

        purchaseOrdered=self.__ctrl.report()

        for product in purchaseOrdered :

            print(product)

    def run(self):

        menu="""
        1---Add/Update a product from keyboard
        2---Add product to shopping cart
        3---Finalize sale
        4---Show income
        5---Report
        6---Show inventory
        7---Show cart
        0---Exit

        """


        option=-1
        while option != 0:

            print(menu)

            option=input("Introduce option:")

            if option.strip() == "1":

                self.add_inventory()
            elif option.strip() == "6" :

                self.show_inventory()

            elif option.strip() == "2" :

                self.add_cart()

            elif option.strip() == "3" :

                self.finalize()

            elif option.strip() == "4" :

                self.income()

            elif option.strip() == "5" :

                self.report()

            elif option.strip() == "0":

                exit()

            elif option.strip() == "7":

                self.show_cart()





