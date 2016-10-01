from Repository.ProductRepo import *
from Domain.ValidityWorld import *
from Domain.Product import *

class ProductFileRepo(ProductRepo):
    _fName="products.txt"

    def __init__(self,validator):
        '''
        constructor from filerepo
        and also calls the function that reads from file
        :return:
        '''
        ProductRepo.__init__(self,validator)
        self._loadFromFile()

    def _storeFile(self):
        """
        stores to file info in repository
        :return:
        """
        f=open(self._fName,"w")
        lst=ProductRepo.get_all(self)
        for obj in lst :
            stt=""
            stt+= obj.get_name()+"," +obj.get_pType()+","+str(obj.get_q())+"\n"
            f.write(stt)
        f.close()



    def _loadFromFile(self):
        '''
        reads from file informations then introduces it into the repository
        :return:
        '''
        try:
            f=open(self._fName,"r")
        except IOError:
            raise ObjectException("File could not be opened!!!")

        line=f.readline().strip()

        while not line == "" :
            t=line.split(",")
            if not len(t) == 3 :
                raise ObjectException("Not sufficient attributes given for an entity in the file!!!")
            # insert Validator
            prd=Product(t[0],t[1],t[2])
            ProductRepo.add(self,prd)
            line=f.readline().strip()

        f.close()

