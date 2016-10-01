'''
Created on Nov 10, 2015

@author: Norbi
'''
from Repository.StudAssignRepo import *
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

class StudAssignCtrl :
    
    def __init__(self,repo):
        '''
        constructor for controller
        '''
        self.__repo=repo
        
    def add(self,sa):
        '''
        adds an object to the repository
        '''
        self.__repo.add(sa)
        
    def get_by_stud(self,stud):
        '''
        gets the object type studassign from the repository as field stud equals stud
        '''
        return self.__repo.get_by_stud(stud)
    
    def get_by_assign(self,assign):
        '''
        gets the object type studassign from the repository as field assign equals assign
        '''
        return self.__repo.get_by_assign(assign)
    
    def remove_by_assign(self,assign):
        '''
        removes by assign from repository by a controller
        '''
        self.__repo.remove_by_assign(assign)
        
    def remove_by_stud(self,stud):
        '''
        removes by stud from repository with a controller
        '''
        self.__repo.remove_by_stud(stud)
        
    def show_stud_assign(self):
        
        self.__repo.show_stud_assign()    
    
        
        
        
        
        