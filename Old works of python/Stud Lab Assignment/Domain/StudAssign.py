'''
Created on Nov 8, 2015

@author: Norbi
'''

from Domain.StudentD import *
from Domain.AssignmentD import *
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

class StudAssign:
    
    def __init__(self,stud,assign,deadline):
        '''
        constructor for studassign
        '''
        self.__stud=stud
        self.__assign=assign
        self.__deadline=deadline
        
    def get_stud(self):
        '''
        getter for item stud
        '''
        return self.__stud
    
    def get_assign(self):
        '''
        getter for item assign
        '''
        return self.__assign
    
    def get_deadline(self):
        '''
        getter for deadline
        '''
        return self.__deadline
    
    def __eq__(self,other):
        '''
        verifies if 2 objects of class StudAssign are equal
        '''
        return type(self) == type (other) and self.__stud==other.__stud and self.__assign==other.__assign and self.__deadline == other.__deadline 
    

def test_StudAssign():
    
    stud=Students(3,"John",3)
    d=Deadlines(1,1,1)
    assign=(3,"9 ex",d,8)
    d=Deadlines(4,4,4)
    sa=StudAssign(stud,assign,d)
    assert sa.get_stud() == stud
    assert sa.get_assign() == assign
    assert sa.get_deadline() == d
    
    
test_StudAssign()