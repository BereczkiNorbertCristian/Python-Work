
from validation.validation import *
from domains.Product import Product

class Inventory:

    _fName="products.txt"
    def __init__(self):

        self.__data=[]
        self._loadFromFile()

    def add_inventory(self,product):

        if len(self.__data) == 0 :
            self.__data.append(product)
        else:

            if product in self.__data :
                for p in self.__data :
                    if p == product:
                        p=p+product

            else :
                self.__data.append(product)
        self.save()


    def get_inventory(self):

        return self.__data


    def _loadFromFile(self):


        f=open(self._fName,"r")

        line=f.readline().strip()

        while line !="" :

            pId,name,quantity,price=line.split(";")
            try:
                Validator.validate(pId,name,quantity,price)
                product=Product(int(pId),name,int(quantity),int(price))
                self.add_inventory(product)
            except StoreException as e:
                print(e)
                print("We will not add this produc to our inventory!!!")

            line=f.readline().strip()


        f.close()


    def save(self):

        f=open(self._fName,"w")

        for product in self.__data :

            writeString="{0};{1};{2};{3}\n".format(product.get_id(),product.get_name(),product.get_quantity(),product.get_price())
            f.write(writeString)


        f.close()