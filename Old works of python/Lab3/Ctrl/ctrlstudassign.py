'''
Created on Nov 11, 2015

@author: Norbi
'''
from copy import deepcopy
from Domain.domstud import *
from Domain.domassign import *
from Domain.domstudassign import *
from Domain.Validity import *
from Ctrl.ChangeHistory import *
from Ctrl.UndoController import *
from Domain.GradDTO import *
from Sorts.Heapsort import heapsort
class StudAssignCtrl :
    
    def __init__(self,repoSA,repoS,repoA,undoCtrl):
        '''
        constructor for controller
        repoSA-repository for associations StudAssign
        repoS-repository for students
        repoA-repository for assginments

        '''
        self.__repoSA=repoSA
        self.__repoS=repoS
        self.__repoA=repoA
        self.__undoCtrl=undoCtrl

        self.__operations=[]
        self.__index=0

        
    def associate(self,studId,assignId,d,grade):
        '''
        adds an association to the repository of associations
        Args:
            studId:int-the id of the student which will be associated
            assignId:int-the id of the assignment with which the student will be associated
            d:Deadline object-the deadline untill the assignment must be done
            grade:int between 1->10

        Returns:

        '''

        self.__eraseOpAbove() #erases the operations after the one which will be newly associated
        self.__undoCtrl.eraseCtrlAbove() #erases the controllers afther the one which will be newly associated

        std=self.__repoS.fetch_stud(studId)
        asg=self.__repoA.fetch_assign(assignId)
        if not isinstance(std,Student) or not isinstance(asg,Assignment) :
            raise ObjectException("Student's ID or Assignment's ID does not exist!!!")
        sa=StudAssign(std,asg,d,grade)
        self.__repoSA.add(sa)

        self.__operations.append(AddOperation(sa))
        self.__index+=1
        self.__undoCtrl.recordUpdatedController(self)
        
    def fetch_by_stud(self, stud):
        '''
        gets the object type studassign from the repository as field stud equals stud
        '''
        return self.__repoSA.fetch_by_stud(stud)
    
    def fetch_by_assign(self, assign):
        '''
        gets the object type studassign from the repository as field assign equals assign
        '''
        return self.__repoSA.fetch_by_assign(assign)
    
    def remove_by_assign(self,assign):
        '''
        removes by assign from repository by a controller
        '''

        self.__repoSA.remove_by_assign(assign)
        
    def remove_by_stud(self,stud):
        '''
        removes by stud from repository with a controller
        '''


        self.__repoSA.remove_by_stud(stud)

    def show_stud_assign(self):
        '''
        shows the list of associations
        Returns:nothing

        '''
        self.__repoSA.show_stud_assign()

    def fetch_association(self,studId,assignId):
        '''

        Args:
            studId:int student's id
            assignId:int assigment's id

        Returns:association
        Exception: returns Objectexception with message if association couldn't be fetched
        '''
        stud=self.__repoS.fetch_stud(studId)
        assign=self.__repoA.fetch_assign(assignId)
        if not isinstance(stud,Student) or not isinstance(assign,Assignment) :
            raise ObjectException("Student's Id or Assignment's id does not exist!!!")
        return self.__repoSA.fetch_association(stud,assign)

    def update(self,newAssoc):
        '''
        Updates the association between a student and an assignment
        Args:
            assoc:object type StudAssign
            d: object type Deadline
            g: int-the grade

        Returns:

        '''

        if not isinstance(newAssoc.get_stud(),Student) or not isinstance(newAssoc.get_assign(),Assignment) :
            raise ObjectException("Student or assignment not found, please introduce correct id's!!")


        self.__eraseOpAbove() #erases the operations after the one which will be newly updated
        self.__undoCtrl.eraseCtrlAbove() #erases the controllers afther the one which will be newly updated

        assoc=self.fetch_association(newAssoc.get_stud().get_id(),newAssoc.get_assign().get_id())
        oldAssoc=deepcopy(assoc)

        self.__repoSA.update(assoc,newAssoc)

        newAssoc=deepcopy(assoc)

        self.__operations.append(UpdateOperation(oldAssoc,newAssoc))
        self.__index+=1
        self.__undoCtrl.recordUpdatedController(self)


    def quick_remove(self,studId,assignId):
        '''
        removes the association with studid and assignid by poping it from the list of associations
        Args:
            studId: int representing student's id
            assignId: int representing assignment's id

        Returns:

        '''
        assoc=self.fetch_association(studId,assignId)
        i=self.__repoSA.search_by_index(assoc)
        lst=self.__repoSA.get_all()
        lst.pop(i)
    def remove_association(self):
        '''
        read's the student's id and assignment's id of the associations to be removed
        then removes is
        and introduces in the undo controller the operation we've done
        Returns:

        '''

        self.__eraseOpAbove() #erases the operations after the one which will be newly removed
        self.__undoCtrl.eraseCtrlAbove() #erases the controllers afther the one which will be newly removed

        studId=Validator.read_positive_integer("Introduce association's student id to be removed:")
        assignId=Validator.read_positive_integer("Introduce association's assignment id to be updated:")
        assoc=deepcopy(self.fetch_association(studId,assignId))

        std=self.__repoS.fetch_stud(studId)
        asg=self.__repoA.fetch_assign(assignId)
        self.__repoSA.RepoRemove(std,asg)

        if isinstance(assoc,StudAssign) :
            self.__operations.append(RemoveOperation(assoc))
            self.__index+=1
            self.__undoCtrl.recordUpdatedController(self)

    def undo(self):
        """
        Undoes the last studassign operation that changed the set of associations.
        Returns True if operation was undone, False otherwise.
        """
        if self.__index == 0 :
            return False

        self.__index-=1
        operation=deepcopy(self.__operations[self.__index])

        if isinstance(operation,AddOperation) :
            self.quick_remove(operation.get_object().get_stud().get_id(),operation.get_object().get_assign().get_id())
        elif isinstance(operation,RemoveOperation) :
            self.__repoSA.add(operation.get_object())
        elif isinstance(operation,UpdateOperation) :
            self.__repoSA.update(operation.get_updatedObject(),operation.get_oldObject())

    def redo(self):
        """
        Redoes the last undo operation
        Returns:True if operation was redone,False otherwise.
        """
        if self.__index ==len(self.__operations) :
            return False

        operation=deepcopy(self.__operations[self.__index])

        if isinstance(operation,AddOperation) :
            self.__repoSA.add(operation.get_object())
        elif isinstance(operation,RemoveOperation) :
            self.quick_remove(operation.get_object().get_stud().get_id(),operation.get_object().get_assign().get_id())
        elif isinstance(operation,UpdateOperation) :
            self.__repoSA.update(operation.get_oldObject(),operation.get_updatedObject())

        self.__index+=1

    def __eraseOpAbove(self):
        """
        If a new operation is made we cannot redo anything , so we delete the operations ,we saved, after the index
        Returns:
        """

        while self.__index < len(self.__operations) :
            self.__operations.pop()


    def avg_stud_grade(self,studid):
        '''
        Computes the average grade of a student by searching for associations(where we can find grades)
        Args:
            studid:int

        Returns:avgGrade of a student
        '''
        lst=self.__repoSA.get_all()
        grades=0
        gradeSum=0
        if len (lst) == 0 :
            return 100000
        for assoc in lst :
            if assoc.get_stud().get_id() == studid :
                grades+=1
                gradeSum+=assoc.get_grade()
        if grades == 0 :
            return -1
        return (gradeSum/grades)

    def AvgGradeBelow5(self):
        '''
        Takes the students with the average grade below 5
        Returns:a list of students with average grade below 5
        '''
        lst=[]
        lst_studs=self.__repoS.get_all()
        for stud in lst_studs :
            avgG=self.avg_stud_grade(stud.get_id())
            if avgG < 5 and avgG >-1:
                lst.append(gradeDTO(stud,avgG))
        return lst

    def __gather_by_assign(self, assign):
        '''
        gets the associations related to an assignment
        Args:
            assign: object type Assignment

        Returns:list of associations related to an assignment

        '''
        lst=[]
        lst_assoc=self.__repoSA.get_all()
        for assoc in lst_assoc :
            if assign == assoc.get_assign() :
                lst.append(assoc)
        return lst




    def SortAlphabetical(self,assign):
        '''
        takes the associations related to an assignment and then sorts them by student's name
        Args:
            assign:object type Assignment

        Returns:list sorted of associations

        '''
        lst=self.__gather_by_assign(assign)
        lst.sort(key=lambda x:x.get_stud().get_name())
        return lst

    def SortByGrade(self,assign):
        '''
        creates a list with associations related to an assignment and sorts it
        Args:
            assign:object type Assignment

        Returns:sorted list of associations by grade

        '''
        lst=self.__gather_by_assign(assign)
        newLst=heapsort(lst,is_greater_grade)
        lst.sort(key=lambda x:x.get_grade())
        assert lst == newLst

        return lst

def is_greater_grade(a,b):

    if a.get_grade() < b.get_grade() :
        return True
    return False
