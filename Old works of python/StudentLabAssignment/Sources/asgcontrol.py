'''
Created on Oct 31, 2015

@author: Norbi
'''

from copy import deepcopy
from Repository import *
from Domain import *
from validityFuntions import *

class AssignController:
    '''
    class controller for assignments
    '''
    def __init__(self,repo):
        self.__repo=repo
        self.__undo=[]

    def add_assign(self,assign):
        
        self.__undo.append(deepcopy(self.__repo))
        self.__repo.add(assign)
        
    def remove_by_id(self,studid):
        
        self.__undo.appen(deepcopy(self.__repo))
        self.__repo.remove_by_id(studid)

    def update(self,studid,description,deadline,grade):
        
        self.__repo.update(studid,description,deadline,grade)
        
    def get_assign(self,studid):
        
        return self.__repo.get_assign(studid)
    
    def undo(self):
        del self.__repo
        self.__repo=self._undo.pop()
    
    def showassigns(self):
        
        self.__repo.showassigns()
