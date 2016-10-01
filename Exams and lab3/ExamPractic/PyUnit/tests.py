

from repos.purchased import *
from repos.shoppingcart import *
from repos.inventory import *
from domains.Product import *
from validation.validation import *
from controllers.controller import *


import unittest

class TestAll(unittest.TestCase):

    def setUp(self):

        self.repoI=Inventory()
        self.repoC=ShoppingCart()
        self.repoP=PurchasedP()
        self.ctrl=Controller(self.repoI,self.repoC,self.repoP)

    def testall(self):

        #testing file reading
        assert len(self.repoI.get_inventory()) == 11

        #testing add non-overlap
        self.ctrl.add_inventory("11","pastery","23","3")

        assert len(self.repoI.get_inventory()) == 11

        #testing add overlap->update
        self.ctrl.add_inventory("1","sugar","33","10")

        assert len(self.repoI.get_inventory()) == 11
        #testing adding to cart
        self.ctrl.add_cart("1","33")

        assert len(self.repoC.get_cart()) == 1
        #testing get_sum()
        lst=self.ctrl.get_cart()

        assert self.ctrl.get_sum(lst) == 330

        self.ctrl.purchase()

        assert len(self.repoP.get_purchased()) == 1

        assert len(self.repoC.get_cart()) == 0




