
from Domain.ValidityWorld import *
from Domain.Product import *
from Repository.ProductRepo import *
from FileRepository.ProductFileRepo import *
from Controller.ProductCtrl import *
from UI.myUI import *

try:
    repo=ProductFileRepo(Validator())
except ObjectException as e:
    print(e)
    exit()

ctrl=ProductCtrl(repo)
cons=Console(ctrl)
cons.main()