'''
Created on Nov 11, 2015

@author: Norbi
'''
from copy import deepcopy
class Student:
    '''
    Student object contains 3 fields
    +__name
    +__id
    +__group
    Methods:
    ---Getters
    ---Setters
    ---equal
    ---make into string
    '''
    def __init__(self,id_student,name,group):
        '''
        contructor of class
        Args:
            -id_student : int
            -name :string
            -groud : int
        '''
        self.__id=id_student
        self.__name=name
        self.__group=group

    def update(self,newStud):
        '''
        updates the existing student by the atributes of a 'new student' by copying newStud's __dict__
        Args:
            newStud: object type Student (the student having the atributes which which we will do the updated)
        Returns:nothing

        '''
        if type(self) != type(newStud):
            raise TypeError("A student can only update with another student!!!")

        self.__dict__ = deepcopy(newStud.__dict__)

    def __eq__(self,other):
        '''
        verifies if another object is the same as self by the following criteria
        Args:others:object type Student
        '''
        
        return self.get_id() == other.get_id() and self.get_name() == other.get_name() and self.get_group() == other.get_group()
    
    def get_id(self):
        '''
        getter for id
        '''
        return self.__id
    
    def get_name(self):
        '''
        getter for name
        '''
        return self.__name
    
    def get_group(self):
        '''
        getter for group
        '''
        return self.__group
        
    def set_name(self,name):
        """
        setter for name
        Args:name-string
        """
        self.__name=name
        
    def set_group(self,group):
        '''
        setter for group
        Args:group-int between 1->10
        '''
        self.__group=group
    
    def __str__(self):
        '''
        returns the content of the object as a string
        '''
        return "Name:{0}    ID:{1}    Group:{2}".format(self.get_name(),self.get_id(),self.get_group())
        
        
        
def tests():
    m=Student(3, "peter", 4)
    assert m.get_id() == 3
    assert m.get_group() == 4
    assert m.get_name() == "peter"

    assert m.get_id() == 3
    m.set_name("Clara")
    assert m.get_name() == "Clara"
    print(m)
    
tests()

