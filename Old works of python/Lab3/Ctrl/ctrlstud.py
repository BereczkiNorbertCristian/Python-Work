'''
Created on Nov 11, 2015

@author: Norbi
'''
from copy import deepcopy
from Domain.Validity import *
from Ctrl.UndoController import *
from Ctrl.ChangeHistory import *
from Domain.domstudassign import *
class StudController:
    '''
    class controler for students
    '''
    def __init__(self,repo,undoController,assocRepo):
        
        self.__repo=repo
        self.__assocRepo=assocRepo

        #the next attributes are needed for undo/redo
        self.__undoController=undoController
        self.__operations=[] #list of operations that have modified this controller
        self.__index=0 #keeps the current index in the list of operations-needed for undo/redo
        
    def get_all(self):
        '''
        Returns:a list of students
        '''
        return self.__repo    
    
    def add_stud(self,stud):
        """
        Adds a student to the repository
        Input:stud
        """

        self.__eraseOpAbove() #erases the operations after the one which will be newly added
        self.__undoController.eraseCtrlAbove() #erases the controllers afther the one which will be newly added

        self.__repo.add(stud)

        #if no exceptions were raised -> record the operation for undo/redo
        self.__operations.append(AddOperation(stud))
        self.__index+=1
        self.__undoController.recordUpdatedController(self)
        
    def remove_by_id(self,studid):
        """
        Removes by id a student
        Because we modify we insert a copy of our preceding list into the undo (stack)
        Input:stud's id which will be removed
        verifies if we have student's id if not we cannot remove anything and the remove_by_id methond stops
        """

        self.__eraseOpAbove() #erases the operations after the one which will be newly removed
        self.__undoController.eraseCtrlAbove() #erases the controllers afther the one which will be newly removed

        oldstud=deepcopy(self.fetch_stud(studid))



        self.__repo.remove_by_id(studid)
        if isinstance(oldstud,Student):
            self.__operations.append(RemoveOperation(oldstud))
            self.__index+=1
            self.__undoController.recordUpdatedController(self)
            appeared=self.__assocRepo.remove_stud(oldstud)
            while isinstance(appeared,StudAssign) :
                self.__operations[self.__index-1].insert_assoc(appeared)
                appeared=self.__assocRepo.remove_stud(oldstud)




    def update(self,newStud):
        """
        Updates a student
        Input:newStud: object type Student
        verifies if we have student's id if not we cannot update anything and the update methond stops
        """

        self.__eraseOpAbove() #erases the operations after the one which will be newly updated
        self.__undoController.eraseCtrlAbove() #erases the controllers afther the one which will be newly updated

        self.__undoController.printtt()
        oldStud=deepcopy(self.fetch_stud(newStud.get_id()))

        self.__repo.update(newStud)
        newStd=self.fetch_stud(newStud.get_id())
        self.__resolve_student(newStd)
        newStd=deepcopy(newStd)

        self.__operations.append(UpdateOperation(oldStud,newStd))
        self.__index+=1
        self.__undoController.recordUpdatedController(self)

    def __resolve_student(self,upStud):
        """
        replaces all the references in the association, which has the id equal to the updated student, with a reference to the updated student
        Args:
            upStud:object type Student (the updated student)
        Returns:
        """
        lst=self.__assocRepo.get_all()
        for assoc in lst:
            if assoc.get_stud().get_id() == upStud.get_id() :
                assoc.change_stud(upStud)




    def fetch_stud(self, studid):
        '''
        fetches a student by his id
        Args:
            studid:int -student's id to be fetched
        Returns:object type Student
        '''
        return self.__repo.fetch_stud(studid)
    
    def undo(self):
        """
        Undoes the last student operation that changed the set of students.
        Returns True if operation was undone, False otherwise.
        """
        if self.__index == 0:#no operation to undo
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
            self.__repo.update(deepcopy(operation.get_oldObject()))

    def redo(self):
        """
        Redoes the last undo operation
        Returns:True if operation was redone,False otherswise.
        """
        if self.__index == len(self.__operations) :
            return False

        operation=deepcopy(self.__operations[self.__index])

        if isinstance(operation,AddOperation):
            self.__repo.add(operation.get_object())
        elif isinstance(operation,RemoveOperation) :
            self.__repo.remove_by_id(operation.get_object().get_id())
            appeared=self.__assocRepo.remove_stud(operation.get_object())
            while isinstance(appeared,StudAssign) :
                appeared=self.__assocRepo.remove_stud(operation.get_object())
            self.__repo.remove_by_id(operation.get_object().get_id())
        else :
            self.__repo.update(deepcopy(operation.get_updatedObject()))

        self.__index+=1

    def __eraseOpAbove(self):
        """
        If a new operation is made we cannot redo anything , so we delete the operations ,we saved, after the index
        Returns:nothing
        """
        while self.__index < len(self.__operations) :
            self.__operations.pop()

    def showstuds(self):
        '''
        shows the list of students
        Returns:nothing
        '''
        self.__repo.showstuds()
#Tests to be added

def try_funct():

    r=0
    print(4|2)
    n=215
    n=n<<1
    print(n)

try_funct()