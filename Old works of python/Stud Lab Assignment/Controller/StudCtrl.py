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
class StudController:
    '''
    class controler for students
    '''
    def __init__(self,repo):
        
        self.__repo=repo
        self.__undo=[]
        
    def get_repo(self):
        return self.__repo    
    
    def add_stud(self,stud):
        """
        Adds a student to the repository
        Input:stud
        """
        if Validator.sverifyid(stud,self.get_repo()) == 0 :
            raise ObjectException("Id already exists!")
        self.__undo.append(deepcopy(self.__repo))
        self.__repo.add(stud)
        
    def remove_by_id(self,studid):
        """
        Removes by id a student
        Because we modify we insert a copy of our preceding list into the undo (stack)
        Input:stud's id which will be removed
        verifies if we have student's id if not we cannot remove anything and the remove_by_id methond stops
        """
        if Validator.sverifyid(Students(studid,"d",1), self.__repo) == 1 :
            print("Id student not found or list of students is empty!")
            return 
        self.__undo.append(deepcopy(self.__repo))
        self.__repo.remove_by_id(studid)    
        
    def remove_by_name(self,name):
        
        self.__undo.append(deepcopy(self.__repo))
        self.__repo.remove_by_name(name)
        
    def update(self,studid,name,group):
        """
        Updates a student
        Input:studid-int,name-string,group-int
        verifies if we have student's id if not we cannot update anything and the update methond stops
        """
        if Validator.sverifyid(Students(studid,"d",1), self.__repo) == 1 :
            print("Id student not found or list of students is empty!")
            return 
        self.__repo.update(studid,name,group)
        
    def get_by_id(self,studid):
        
            return self.__repo.get_stud(studid)
    
    def undo(self):
        
        if not self.__undo :
            print("You cannot undo anymore!")
            return
        del self.__repo
        self.__repo=self.__undo.pop()
        
    def showstuds(self):
        
        self.__repo.showstuds()

#Tests to be added