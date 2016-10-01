'''
Created on Nov 11, 2015

@author: Norbi
'''
from Domain.domassign import *
from Domain.domstud import *
from Domain.domdeadline import *

class StudAssign:
    
    def __init__(self,stud,assign,deadline,grade):
        '''
        constructor for studassign
        '''
        self.__stud=stud
        self.__assign=assign
        self.__deadline=deadline
        self.__grade=grade

    def __eq__(self, other):
        '''

        Args:
            other:object type StudAssign

        Returns:True if objects match
        False if they don't match

        '''
        return type(self)==type(other) and self.__stud == other.get_stud() and self.get_assign() == other.get_assign() and self.get_deadline() == other.get_deadline() and self.get_grade() == other.get_grade()

    def get_stud(self):
        '''
        getter for item stud
        '''
        return self.__stud

    def change_stud(self,Stud):
        """
        Changes the student in the association
        Args:
            Stud:Object type student
        Returns:
        """
        self.__stud=Stud

    def change_assign(self,Assign):
        '''
        changes the association's assign
        Args:
            Assign: object type Assign
        '''
        self.__assign=Assign

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
    def set_deadline(self,d):
        '''
        setter for deadline
        Returns:

        '''
        oldD=self.get_deadline()
        oldD.set_day(d.get_day())
        oldD.set_month(d.get_month())
        oldD.set_year(d.get_year())

    def update(self,newAssoc):
        '''
        updates by copying the new association's __dict__ into the old one's
        Args:
            newAssoc:object type StudAssign
        Returns:nothing
        '''
        if not type(newAssoc) == type(self) :
            raise TypeError("Association can only be updated with another association!")
        self.__dict__ = deepcopy(newAssoc.__dict__)

    def get_grade(self):
        '''
        getter for grade
        Returns:assignment's grade
        '''
        return self.__grade
    def set_grade(self,grade):
        '''
        setter for grade
        input:int-grade
        Returns:nothing
        '''
        self.__grade=grade
    def __str__(self):
        '''
        Transforms the object into a string
        '''
        stt="STUDENT:   {0}    ASSIGNMENT:   {1}   DEADLINE:   {2}   GRADE:{3}".format(self.__stud,self.__assign,self.__deadline,self.__grade)
        return stt
    '''
    def __eq__(self,other):
        
        verifies if 2 objects of class StudAssign are equal
        
        return type(self) == type (other) and self.__stud==other.__stud and self.__assign==other.__assign and self.__deadline == other.__deadline 
    '''

def test_StudAssign():
    
    stud=Student(3, "John", 3)
    d=Deadlines(1,1,1)
    assign=Assignment(3,"9 ex")
    d=Deadlines(4,4,4)
    print(d)
    sa=StudAssign(stud,assign,d,5)
    assert sa.get_stud() == stud
    assert sa.get_assign() == assign
    assert sa.get_deadline() == d
    assert sa.get_grade() == 5
    print(sa)
test_StudAssign()