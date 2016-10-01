

from repos.inventory import Inventory
from repos.shoppingcart import ShoppingCart
from repos.purchased import PurchasedP
from controllers.controller import Controller
from ui.ui import Console


repoI=Inventory()
repoC=ShoppingCart()
repoP=PurchasedP()
ctrl=Controller(repoI,repoC,repoP)
consl=Console(ctrl)

consl.run()
