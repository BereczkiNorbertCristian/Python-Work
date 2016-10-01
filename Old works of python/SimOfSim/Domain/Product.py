

from copy import deepcopy

class Product:
    """
    class product
    atributes:
    ---mark
    ---quantity
    """
    def __init__(self, name, pType, q):
        """
        constructor for object prduct
        """
        self.__name=name
        self.__pType=pType
        self.__q=q

    def __str__(self):
        """
        string transformator
        returns : string type
        """
        entity=""
        entity+= "Name:"+str(self.__name)+"\t" +"Type:"+str(self.__pType)+"\t" +"Quantity:" + str(self.__q)
        return entity
    def update(self,upObj):
        """
        updator for object
        :param upObj: object which we will do the update
        """
        self.__q=self.__q-upObj.get_q()

    def get_name(self):
        """
        getter for mark
        :return: the mark
        """
        return self.__name

    def get_pType(self):
        '''
        getter for type
        :return:
        '''
        return self.__pType

    def set_q(self):
        """
        converts quantity to int
        :return:
        """
        self.__q=int(self.__q)

    def get_q(self):
        """
        getter for q
        :return: quantity
        """
        return self.__q

    def __eq__(self,obj):
        '''
        :param obj: object type product
        :return:true if the objects are equal from this perspective
        false otherwise
        '''
        return type(self) == type(obj) and self.__name == obj.get_name() and self.__pType == obj.get_pType()
