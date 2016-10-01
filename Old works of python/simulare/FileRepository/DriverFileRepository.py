


from Repository.DriverRepo import *
from Domain.Driver import *

class DriverFileRepository(DriverRepo) :
    '''
    _fName-file's name from which we will read
    '''
    _fName="drivers.txt"

    def __init__(self):
        '''
        constructor for file repository
        :return:
        '''
        DriverRepo.__init__(self)
        self._loadFromFile()


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
            drv=Driver(int(t[0]),t[1])
            DriverRepo.add(self,drv)
            line=f.readline().strip()

        f.close()
