
from validation.validation import *
from domains.Product import Product
from copy import deepcopy

class Controller:

    def __init__(self,inventory,shoppingCart,purchasedP):
        '''

        :param inventory:repo
        :param shoppingCart: repo
        :param purchasedP: repo
        :return:
        '''
        self.__inventory=inventory
        self.__shoppingCart=shoppingCart
        self.__purchasedP=purchasedP

    def add_inventory(self,pId,name,quantity,price):

        Validator.validate(pId,name,quantity,price)
        product=Product(int(pId),name,int(quantity),int(price))
        self.__inventory.add_inventory(product)

    def get_inventory(self):
        '''
        returns the list of products in the inventory
        :return:
        '''
        return self.__inventory.get_inventory()

    def add_cart(self,pId,quantity):
        '''
        adds to the cart and validates if the product can be added to the card
        :param pId:string
        :param quantity:string
        :return:
        exceptions:
        raises StoreException if we have not found the product with the given id or if the quantity is not available
        '''
        inventory=self.__inventory.get_inventory()


        Validator.validateIdQ(pId,quantity)
        prodId=int(pId)
        quantity=int(quantity)
        found=False
        for product in inventory:
            if product.get_id() == prodId :
                if product.get_quantity() < quantity :
                    raise StoreException("Quantity not available!!!")
                else:
                    found=True

                    productInShopping=deepcopy(product)
                    product.set_quantity(product.get_quantity()-quantity)
                    productInShopping.set_quantity(quantity)
                    self.__shoppingCart.add_shoppingCart(productInShopping)
        self.__inventory.save()

        if found == False:
            raise StoreException("Product not in inventory!!!")

    def get_cart(self):
        '''
        gets the container of the cart
        :return:
        '''
        return self.__shoppingCart.get_cart()


    def get_purchased(self):
        '''
        gets the container of the purchased items
        :return:
        '''
        return self.__purchasedP.get_purchased()

    def get_cartCost(self):
        '''
        gets the sum for the cart items using the get_sum() function
        :return:
        '''
        cart=self.__shoppingCart.get_cart()

        return self.get_sum(cart)

    def get_sum(self,lst):
        '''
        computes the sum of the list (cart or purchased list of items)
        :param lst: list of products to be parsed and to be added to the sum their cost(each product's cost)
        :return:
        '''
        sum = 0
        for product in lst :
            sum+=product.get_quantity()*product.get_price()

        return sum

    def purchase(self):
        '''
        a purchase has been done so the elements in the cart are put in the purchased container
        then we clear the cart
        then we save to the file the modifications
        :return:
        '''

        cart=self.__shoppingCart.get_cart()

        for product in cart :

            self.__purchasedP.add_purchase(product)

        self.__shoppingCart.clear_cart()
        self.__inventory.save()


    def notpurchase(self):
        '''
        we clear the cart
        we put the product back in the inventory
        :return:
        '''
        cart=self.__shoppingCart.get_cart()

        for product in cart :

            self.__inventory.add_inventory(product)

        self.__shoppingCart.clear_cart()

    def income(self):
        '''
        calculates the total income using the function get_sum()
        :return:
        '''
        purchase=self.__purchasedP.get_purchased()

        return self.get_sum(purchase)

    def report(self):
        '''
        takes the purchased items the it orders them
        :return:list of purchased products ordered descedingly
        '''
        purchase=self.get_purchased()

        purchase.sort(key=lambda x:x.get_quantity(),reverse=True)

        return purchase



