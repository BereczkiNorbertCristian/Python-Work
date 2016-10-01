
from Domain.Order import *
from Domain.Driver import *
from FileRepository.DriverFileRepository import *
from FileRepository.OrderFileRepository import *
from Ctrl.GenCtrl import *
from UI.myUi import *
from Repository.DriverRepo import *
from Repository.OrderRepo import *

import unittest

class TestAll(unittest.TestCase):

    def setUp(self):
        self.ordrRepo=OrderRepo()
        self.drivRepo=DriverRepo()
        self.ctrl=GenCtrl(self.drivRepo,self.ordrRepo)


    def testAll(self):

        drv=Driver(1,"Alex")
        self.drivRepo.add(drv)

        self.assertEqual(len(self.drivRepo),1)

        drv=Driver(2,"Peter")
        self.drivRepo.add(drv)
        drv=Driver(1000,"John")
        self.drivRepo.add(drv)
        drv=Driver(4,"Anton")
        self.drivRepo.add(drv)
        drv=Driver(20,"Carlos")
        self.drivRepo.add(drv)

        self.assertEqual(len(self.drivRepo),5)

        ordr=Order(1,6)
        self.ordrRepo.add(ordr)
        ordr=Order(2,10)
        self.ordrRepo.add(ordr)
        ordr=Order(1000,30)
        self.ordrRepo.add(ordr)
        ordr=Order(1,33)
        self.ordrRepo.add(ordr)
        ordr=Order(4,67)
        self.ordrRepo.add(ordr)
        ordr=Order(20,20)
        self.ordrRepo.add(ordr)
        ordr=Order(20,1)
        self.ordrRepo.add(ordr)

        self.assertEqual(len(self.ordrRepo),7)

        self.assertEqual(self.ctrl.getSum(1),39)
        self.assertEqual(self.ctrl.getSum(2),10)
        self.assertEqual(self.ctrl.getSum(20),21)







