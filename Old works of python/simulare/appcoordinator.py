from Domain.Order import *
from Domain.Driver import *
from FileRepository.DriverFileRepository import *
from FileRepository.OrderFileRepository import *
from Ctrl.GenCtrl import *
from UI.myUi import *

ordrRepo=OrderFileRepository()
drivRepo=DriverFileRepository()
ctrl=GenCtrl(drivRepo,ordrRepo)
cons=Console(ctrl)

cons.menu()