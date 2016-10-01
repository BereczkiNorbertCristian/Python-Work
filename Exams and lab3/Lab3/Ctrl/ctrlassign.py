'''
Created on Nov 11, 2015

@author: Norbi
'''
from copy import deepcopy
from Domain.Validity import ObjectException
from Ctrl.UndoController import *
from Ctrl.ChangeHistory import *
from Domain.domassign import *
from Domain.domstudassign import *
class AssignController:
    '''
    class controller for assignments
    Atributes:
    ---repo
    ---undoController
    ---operations-list of operations which were done in this controller
    ---index - the index in the operations list regarding the last operations which was done
    '''
    def __init__(self,repo,undoController,assocRepo):
        self.__repo=repo
        self.__assocRepo=assocRepo
        self.__undoController=undoController
        self.__operations=[]
        self.__index=0

    def add_assign(self,assign):
        """
        Adds an assginment to the list of assginments
        Input:assginment ot be added of class Assginments
        """

        self.__eraseOpAbove() #erases the operations after the one which will be newly added
        self.__undoController.eraseCtrlAbove() #erases the controllers afther the one which will be newly added

        self.__repo.add(assign)

        self.__operations.append(AddOperation(assign))
        self.__index+=1
        self.__undoController.recordUpdatedController(self)
        
    def remove_by_id(self,assignid):
        """
        Removes by id a student
        input:studid -int
        verifies if we have assignment's id if not we cannot remove anything and the remove_by_id methond stops
        """

        self.__eraseOpAbove() #erases the operations after the one which will be newly removed
        self.__undoController.eraseCtrlAbove() #erases the controllers afther the one which will be newly removed

        oldassign=deepcopy(self.fetch_assign(assignid))

        self.__repo.remove_by_id(assignid)
        if isinstance(oldassign,Assignment) :
            self.__operations.append(RemoveOperation(oldassign))
            self.__index+=1
            self.__undoController.recordUpdatedController(self)
            appeared=self.__assocRepo.remove_assign(oldassign)
            while isinstance(appeared,StudAssign) :
                self.__operations[self.__index-1].insert_assoc(appeared)
                appeared=self.__assocRepo.remove_assign(oldassign)

    def update(self,newAssign):
        """
        uptades an assignment
        input :
            newAssign -Object type Assignment
        verifies if we have assignment's id if not we cannot update anything and the update methond stops
        """

        self.__eraseOpAbove() #erases the operations after the one which will be newly updated
        self.__undoController.eraseCtrlAbove() #erases the controllers afther the one which will be newly updated

        oldAssign=deepcopy(self.fetch_assign(newAssign.get_id()))
        self.__repo.update(newAssign)
        newAssign=self.fetch_assign(newAssign.get_id())
        self.__resolve_assignment(newAssign)
        newAssign=deepcopy(newAssign)

        self.__operations.append(UpdateOperation(oldAssign,newAssign))
        self.__index+=1
        self.__undoController.recordUpdatedController(self)

    def __resolve_assignment(self,upAssign):
        """
        replaces all the references in the association, which has the id equal to the updated student, with a reference to the updated student
        Args:
            upStud:object type Student (the updated student)
        Returns:
        """
        lst=self.__assocRepo.get_all()
        for assoc in lst:
            if assoc.get_assign().get_id() == upAssign.get_id() :
                assoc.change_assign(upAssign)


    def fetch_assign(self, studid):
        '''
        returns an assignment which has in it a studid
        '''
        return self.__repo.fetch_assign(studid)
    
    def undo(self):
        """
        Undoes the last assignment operation that changed the set of assignments.
        Returns True if operation was undone, False otherwise.
        """
        if self.__index == 0 :
            return False

        self.__index-=1
        operation=deepcopy(self.__operations[self.__index])

        if isinstance(operation,AddOperation) :
            self.__repo.remove_by_id(operation.get_object().get_id())
        elif isinstance(operation,RemoveOperation) :
            self.__repo.add(operation.get_object())
            lst=operation.all_assocs()
            for iassoc in lst :
                self.__assocRepo.add(iassoc)
        else :
            self.__repo.update(operation.get_oldObject())

    def redo(self):
        """
        Redoes the last undo operation
        Returns:True if operation was redoed,False otherswise.
        """
        if self.__index == len(self.__operations) :
            return False

        operation=deepcopy(self.__operations[self.__index])

        if isinstance(operation,AddOperation):
            self.__repo.add(operation.get_object())
        elif isinstance(operation,RemoveOperation) :
            self.__repo.remove_by_id(operation.get_object().get_id())
            appeared=self.__assocRepo.remove_assign(deepcopy(operation.get_object()))
            while isinstance(appeared,StudAssign) :
                appeared=self.__assocRepo.remove_assign(operation.get_object())
        else :
            self.__repo.update(deepcopy(operation.get_updatedObject()))

        self.__index+=1

    def __eraseOpAbove(self):
        """
        If a new operation is made we cannot redo anything , so we delete the operations ,we saved, after the index
        Returns:
        """

        while self.__index < len(self.__operations) :
            self.__operations.pop()


    def showassigns(self):
        '''
        shows the list of assignments
        Returns:nothing

        '''
        self.__repo.showassigns()

#Tests to be added

