
from Repository.OrderRepo import *
from Domain.Order import *

class OrderFileRepository(OrderRepo) :
    '''
    _fName-file's name from which we will read
    '''
    _fName="orders.txt"

    def __init__(self):
        '''
        constructor for file repository
        :return:
        '''
        OrderRepo.__init__(self)
        self._loadFromFile()

    def add(self,obj):
        '''
        adds an entity to the file and to the repo
        :param obj: object type order
        :return:
        '''
        OrderRepo.add(self,obj)
        self._storToFile()


    def _loadFromFile(self):
        '''
        reads from file the needed information and puts it in the repository
        :return:
        '''
        try:
            f= open (self._fName,"r")
        except IOError :
            return

        line=f.readline().strip()
        while not line == "" :
            t=line.split(",")
            ordr=Order(int(t[0]),int(t[1]))
            OrderRepo.add(self,ordr)
            line=f.readline().strip()

        f.close()

    def _storToFile(self):
        '''
        writes in the file the information from the repository
        :return:
        '''
        f=open(self._fName,"w")
        lst=OrderRepo.get_all(self)
        for obj in lst:
            stt=""
            stt+=str(obj.get_drivId()) + "," + str(obj.get_dist()) + "\n"
            f.write(stt)
        f.close()

