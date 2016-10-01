'''
Created on Nov 3, 2015

@author: Norbi
'''

from Domain.DeadlinesD import *


class Assignments:
    '''
    Object assignmet has 4 entities
    +__studentid
    +__description
    +__dedline
    +__grade
    Methods:
    ---Getters
    ---Setters
    ---Makes into string
    '''
    
    def __init__(self,studentid,description,grade):
        self.__studid=studentid
        self.__description=description
        self.__grade=grade
    
    def __eq__(self,other):
        return type(self) == type(other) and self.get_id() == other.get_id() and self.get_description() == other.get_description() and self.get_grade() == other.get_grade()
    
    def get_id(self):
        return self.__studid
    
    def get_description(self):
        return self.__description
    
    def get_grade(self):
        return self.__grade
    
    def set_id(self,studid):
        self.__studid=studid
        
    def set_description(self,description):
        self.__description=description
        
    def set_grade(self,grade):
        self.__grade=grade
    
    def __str__(self):
        
        my_string = "Student ID:" + str(self.__studid)
        my_string += " " + "Description:" + self.__description
        my_string += " " + "Grade" + str(self.__grade)
        return my_string
       
       
       
def tests():
    #d=Deadlines(3,3,3)
    m=Assignments(4,"5 ex",5)
    
    #assert m.get_deadline() == Deadlines(3,3,3)
    assert m.get_description() == "5 ex"
    assert m.get_grade() == 5
    assert m.get_id() == 4
    
     
tests()
