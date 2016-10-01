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
class student_repository:
    '''
    Class used for handling the list of students
    '''
    def __init__(self):
        
        self.__stud_list=[]
    
    def add(self,student):
        """
        appends student to the list
        input:student-Students
        """
        self.__stud_list.append(student)
    
    def __len__(self):
        '''
        returns the lenght of the stud_list
        '''
        return len(self.__stud_list)
    
    def get_list(self):
        '''
        returns the list in the repository
        '''
        return self.__stud_list
    
    def __str__(self):
        """
        adds to a string all the students
        """
        string_list=""
        for stud in self.__stud_list:
            string_list += str(stud) + "\n"
        return string_list
    
    
    def remove_by_id(self,studid):
        """
        searches for a student , if thath student has the same id with the one we are interested for it pops it from the list of studs
        input:
        studid-int
        """
        
        for i in range (0,len(self.__stud_list)) :
            if self.__stud_list[i].get_id() == studid :
                self.__stud_list.pop(i)
                return 
        '''
        for stud in self.__stud_list :
            if stud.get_id() == studid :
                del stud
        '''
    def remove_by_name(self,name):
        for stud in self.__stud_list :
            if stud.get_name() == name :
                del stud
        
    def update(self,studid,name,group):
        """
        Updates the student using setters
        Input:studid-int , name-string , group-int
        """
        stud=self.get_stud(studid)
        if not stud :
            print("There is no student with this ID")
        stud.set_name(name)
        stud.set_group(group)
    
    def get_stud(self,studid):
        '''
        searches for a student then returns in the stud_list of the repository 
        returns object student if it has found it by id
        returns false if it hasn't found and id that maches the given id
        '''
        for stud in self.__stud_list:
            if stud.get_id() == studid :
                return stud
        return False
    
    def showstuds(self):
        '''
        shows students
        '''
        if not self.__stud_list :
            print("The list of students is empty!")
            return 
        for stud in self.__stud_list :
            print(str(stud)+"\n")

def testRepositoryStud():
    myrepo=student_repository()
    
    s1=Students(5,"John",7)
    s2=Students(6,"Marry",8)
    
    assert len(myrepo) == 0
    
    myrepo.add(s1)
    myrepo.add(s2)
    
    assert len(myrepo) == 2
    
    myrepo.remove_by_id(5)
    
    assert len(myrepo) == 1
    
    myrepo.update(6,"Carlie",3)
    
    m=Students(6,"Carlie",3)
    assert len(myrepo) == 1
    
    
    

    
#testRepositoryStud()


