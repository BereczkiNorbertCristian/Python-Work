

class UndoController:
    """
    This class controls the undo/redo operations over all application
    controllers.
    It is required so that we have a record of what controller must perform
    each undo
    """
    def __init__(self):
        '''
        constructor
        '''
        # constains list of controllers that have been modified (in the order of modification)
        self.__controllers=[]
        #index for the last controller that suffered modification
        self.__index=-1

    def recordUpdatedController(self,modifController):
        """
        Every time an application controller record an operation with support
        for undo/redo it must call this method.
        Input: modifController - A list of controllers that can undo/redo the
        operation.

        !!! In case an operation involves multiple distinct
        controllers, then a list of modified controllers will have to be provided
        (NOT just one controller!)

        Output: the current list of controllers is modified and the index is
        set to the last list of modified controllers.
        """
        self.__controllers.append(modifController)
        self.__index=len(self.__controllers)-1

    def undo(self):
        '''
        undo last performed operation
        Returns:

        '''
        print(self.__index)
        print(len(self.__controllers))
        if self.__index < 0 :
            return False

        #all the undo functions for the last controller that has been modified
        self.__controllers[self.__index].undo()
        #self.__controllers.pop(self.__index)
        self.__index-=1
        return True

    def printtt(self):
        print(len(self.__controllers))

    def redo(self):
        '''
        redoes last performed undo
        Returns:
        '''

        if self.__index + 1 == len(self.__controllers) or len(self.__controllers) == 0 :
            return False

        self.__index+=1
        self.__controllers[self.__index].redo()
        print(self.__index)
        print(len(self.__controllers))
        return True



    def eraseCtrlAbove(self):
        """
        pops the controllers saved in the controllers list between the index and the length of the list
        we do this because every time we do a new opperation we cannot redo anything
        Returns:
        """

        while len(self.__controllers) > self.__index + 1 and self.__index > -1 :
            self.__controllers.pop()





