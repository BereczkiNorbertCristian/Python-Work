

class AddOperation:
    '''
    class that models an add operation
    '''
    def __init__(self,object):
        '''
        constructor
        Args:
            object
        '''
        self.__object=object

    def get_object(self):
        '''
        getter for object
        Returns:object in class

        '''
        return self.__object


class RemoveOperation:
    '''
    class that models a remove operation
    '''
    def __init__(self,object):
        '''
        constructor
        Args:
            object:the object on which a remove operations was applied
        '''
        self.__object=object
        self.__associations=[]

    def insert_assoc(self,assoc):
        '''
        inserts an association into the list of saved associations
        Args:
            assoc: object type StudAssign
        Returns:nothing
        '''
        self.__associations.append(assoc)

    def all_assocs(self):
        '''
        Gives back a list of all associations
        Returns:a list of all associations

        '''
        return self.__associations


    def get_object(self):
        '''
        getter for object
        Returns:object
        '''
        return self.__object

class UpdateOperation:
    '''
    class that models an update operation
    '''
    def __init__(self,oldObject,updatedObject):
        '''
        constructor
        Args:object
        '''
        self.__oldObject=oldObject
        self.__updatedObject=updatedObject

    def get_oldObject(self):
        '''
        getter for oldobject
        Returns:oldobject
        '''
        return self.__oldObject
    def get_updatedObject(self):
        '''
        getter for updatedobject
        Returns:updatedobject
        '''

        return self.__updatedObject


