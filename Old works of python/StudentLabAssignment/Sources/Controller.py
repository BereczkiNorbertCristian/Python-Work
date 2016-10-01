'''
Created on Oct 31, 2015

@author: Norbi
'''

from copy import deepcopy
from Repository import *
from Domain import *
from validityFuntions import *

class StudController:
    '''
    class controler for students
    '''
    def __init__(self,repo):
        
        self.__repo=repo
        self.__undo=[]
        
    def add_stud(self,stud):
        
        self.__undo.append(deepcopy(self.__repo))
        self.__repo.add(stud)
        
    def remove_by_id(self,studid):
        
        self.__undo.append(deepcopy(self.__repo))
        self.__repo.remove_by_id(studid)    
        
    def remove_by_name(self,name):
        
        self.__undo.append(deepcopy(self.__repo))
        self.__repo.remove_by_name(name)
        
    def update(self,studid,name,group):
        
        self.__repo.update(studid,name,group)
        
    def get_by_id(self,studid):
        
        return self.__repo.get_stud(studid)
    
    def undo(self):
        del self.__repo
        self.__repo=self._undo.pop()
        
    def showstuds(self):
        
        self.__repo.showstuds()
