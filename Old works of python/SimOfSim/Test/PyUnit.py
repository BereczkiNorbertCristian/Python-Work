
from Domain.ValidityWorld import *
from Domain.Product import *
from Repository.ProductRepo import *
from FileRepository.ProductFileRepo import *
from Controller.ProductCtrl import *
from UI.myUI import *



import unittest

class TestAll(unittest.TestCase) :


    def setUp(self):
        '''
        try:
            self.repo=ProductFileRepo(Validator())
        except ObjectException as e:
            print(e)
            exit()
        '''
        self.repo=ProductRepo(Validator())
        self.ctrl=ProductCtrl(self.repo)
        self.cons=Console(self.ctrl)




    def testAll(self):

        obj=Product("nivea","soap","23")
        self.repo.add(obj)
        obj=Product("milka","chocolate","2")
        self.repo.add(obj)
        obj=Product("heidi","chocolate","3")
        self.repo.add(obj)
        obj=Product("palmolive","showergel","9")
        self.repo.add(obj)
        obj=Product("lindl","chocolate","15")
        self.repo.add(obj)


        lst=self.repo.get_all()
        self.assertEqual( len (lst), 5)

        self.ctrl.update("lindl","chocolate","7")
        self.assertEqual( self.repo.find("lindl").get_q(),8)
