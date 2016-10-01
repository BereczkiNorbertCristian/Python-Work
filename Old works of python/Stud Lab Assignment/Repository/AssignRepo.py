'''
Created on Nov 3, 2015

@author: Norbi
'''

from copy import deepcopy
from Controller.StudCtrl import *
from Controller.AssignCtrl import *
from Validity.MyValidFuntions import *
from Controller.StudAssignCtrl import *
from Repository.AssignRepo import *
from Repository.AssignRepo import *
from Repository.StudAssignRepo import *
from Domain.AssignmentD import *
from Domain.StudentD import *
from Domain.StudAssign import *
from Domain.DeadlinesD import *
class assignment_repository :
    
    def __init__(self):
        '''
        constructor for the repository of assignments
        '''
        self.__assign_list=[]
        
    def add(self,assignment):
        '''
        ads an assignment to the list
        '''
        self.__assign_list.append(assignment)
    
    def get_list(self):
        '''
        gets the list of assignments from the repository
        '''
        return self.__assign_list
    
    
    
    def __len__(self):
        '''
        returns the length of the repository
        '''
        return len(self.__assign_list)
    
    def __str__(self):
        '''
        returns a string with the meaning of all elements in the repository transformed to string
        '''
        my_string = ""
        for assign in self.__assign_list :
            my_string+= str(assign) + "/n"
        return my_string
        
    def remove_by_id(self,studid):
        """
        Searches for an assignment in the assignment list and if it found removes the assignment
        """
        
        for i in range (0,len(self.__assign_list)) :
            if self.__assign_list[i].get_id() == studid :
                self.__assign_list.pop(i)
                return 
    
    def get_assign(self,studid):
        '''
        searches for an assignment in the list by an id
        returns object assign if id was found maching with studid
        returns false if id was not found
        '''
        for assign in self.__assign_list :
            if assign.get_id() == studid :
                return assign
            
        return False
    
    def update(self,studid,description,grade):
        '''
        updates the assignment
        '''
        assign=self.get_assign(studid)
        assign.set_description(description)
        #assign.set_deadline(deadline)
        assign.set_grade(grade)
        
    def showassigns(self):
        '''
        shows all the assignments
        '''
        if not self.__assign_list :
            print("The list of assignments is empty!")
            return 
        for assign in self.__assign_list :
            print(str (assign))
    
def testrepass():
    repo=assignment_repository()
    #d=Deadlines(11,11,11)
    a=Assignments(5,"5 exercises",6)
    
    assert len(repo) == 0
    
    repo.add(a)
    assert len (repo) == 1
    
    repo.remove_by_id(5)
    assert len(repo) == 0
    
    
    
    
    
    
    
    
#testrepass()
        