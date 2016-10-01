'''
Created on Oct 31, 2015

@author: Norbi
'''

from Domain import *


class student_repository:
    '''
    Class used for handling the list of students
    '''
    def __init__(self):
        
        self.__stud_list=[]
    
    def add(self,student):
        
        self.__stud_list.append(student)
    
    def __len__(self):
        
        return len(self.__stud_list)
    
    def __str__(self):
        string_list=""
        for stud in self.__stud_list:
            string_list += str(stud) + "\n"
        return string_list
    
    
    def remove_by_id(self,studid):
        
        for stud in self.__stud_list :
            if stud.get_id() == studid :
                del stud
        
    def remove_by_name(self,name):
        
        for stud in self.__stud_list :
            if stud.get_name() == name :
                del stud
        
    def update(self,studid,name,group):
        
        stud=self.get_stud(studid)
        if stud == None :
            print("There is no student with this ID")
        stud.set_name(name)
        stud.set_group(group)
    
    def get_stud(self,studid):
        
        for stud in self.__stud_list:
            if stud.get_id() == studid :
                return stud
        return False
    
    def showstuds(self):
        
        for stud in self.__stud_list :
            print(str(stud)+"\n")
    
class assignment_repository :
    
    def __init__(self):
        
        self.__asign_list=[]
        
    def add(self,assignment):
        
        self.__asign_list.append(assignment)
        
    def __len__(self):
        
        return len(self.__assign_list)
    
    def __str__(self):
        
        my_string = ""
        for assign in self.__asign_list :
            my_string+= str(assign) + "/n"
        return my_string
        
    def remove_by_id(self,studid):
        
        for assign in self.__asign_list :
            if studid == assign.get_id() :
                del assign
    
    def get_assign(self,studid):
        
        for assign in self.__asign_list :
            if assign.get_id() == studid :
                return assign
            
        return False
    
    def update(self,studid,description,deadline,grade):
        
        assign=self.get_assign(studid)
        assign.set_description(description)
        assign.set_deadline(deadline)
        assign.set_grade(grade)
        
    def showassigns(self):
        
        for assign in self.__asign_list :
            print(str (assign))
        
        
    