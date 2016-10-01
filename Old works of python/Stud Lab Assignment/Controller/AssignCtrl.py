'''
Created on Nov 3, 2015

@author: Norbi
'''

from copy import deepcopy
from Repository.AssignRepo import *
from Domain.AssignmentD import *
from Validity.MyValidFuntions import *
from Controller.StudCtrl import *
from copy import deepcopy
from Controller.StudCtrl import *
from Controller.AssignCtrl import *
from Validity.MyValidFuntions import *
from Controller.StudAssign import *
from Repository.AssignRepo import *
from Repository.AssignRepo import *
from Repository.StudAssignRepo import *
from Domain.AssignmentD import *
from Domain.StudentD import *
from Domain.StudAssign import *
from Domain.DeadlinesD import *

class AssignController:
    '''
    class controller for assignments
    '''
    def __init__(self,repo):
        self.__repo=repo
        self.__undo=[]

    def add_assign(self,assign):
        """
        Adds an assginment to the list of assginments
        Input:assginment ot be added of class Assginments
        """
        
        self.__undo.append(deepcopy(self.__repo))
        self.__repo.add(assign)
        
    def remove_by_id(self,studid):
        """
        Removes by id a student
        input:studid -int
        verifies if we have assignment's id if not we cannot remove anything and the remove_by_id methond stops
        """
        #d=Deadlines(1,1,1)
        if Validator.averifyid(Assignments(studid,"d",1), self.__repo) == True :
            print("Id student not found or list of assignments is empty!")
            return 
        self.__undo.append(deepcopy(self.__repo))
        self.__repo.remove_by_id(studid)

    def update(self,studid,description,grade):
        """
        uptades a student
        input :
        studid-int
        descprition-string
        deadline-Deadlines
        grade-int
        verifies if we have assignment's id if not we cannot update anything and the update methond stops
        """
        #d=Deadlines(1,1,1)
        if Validator.averifyid(Assignments(studid,"d",1), self.__repo) == 1 :
            print("Id student not found or list of assignments is empty!")
            return 
        self.__repo.update(studid,description,grade)
        
    def get_assign(self,studid):
        
        return self.__repo.get_assign(studid)
    
    def undo(self):
        del self.__repo
        self.__repo=self._undo.pop()
    
    def showassigns(self):
        
        self.__repo.showassigns()

#Tests to be added
