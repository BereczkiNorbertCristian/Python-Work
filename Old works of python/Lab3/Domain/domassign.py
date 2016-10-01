'''
Created on Nov 11, 2015

@author: Norbi
'''
from copy import deepcopy
from Domain.Validity import ObjectException
class Assignment:
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
    ---Equality between two objects of this type
    '''
    
    def __init__(self,assignmentid,description):
        '''

        Args:
            assignmentid:int assignment's id
            description: string -assignment's description

        Returns:nothing

        '''
        self.__id=assignmentid
        self.__description=description
    
    def __eq__(self,other):
        '''
        compares the two objects of the same type
        Args:
            other:object type assignment

        Returns:True if both objects are equal
        False if not

        '''
        return type(self) == type(other) and self.get_id() == other.get_id() and self.get_description() == other.get_description()
    
    def get_id(self):
        '''
        getter for id
        Returns:int-studid

        '''
        return self.__id
    
    def get_description(self):
        '''
        getter for description
        Returns:description-string

        '''
        return self.__description

    def update(self,newAssign):
        '''
        updates the atributes by copying the __dict__ from newAssign to the current assignment
        Args:
            newAssign:object type Assignment
        Returns:
        '''
        if not type(self) == type(newAssign) :
            raise TypeError("A student can only update with another student!!!")

        if self.get_description() == "" :
            raise ObjectException("It must have a name!!!")

        self.__dict__ = deepcopy(newAssign.__dict__)

    def set_description(self,description):
        '''
        setter for description
        Args:
            description: string

        Returns:nothing

        '''
        self.__description=description

    def __str__(self):
        '''
        transforms the object into a string
        Returns:string-my_string
        '''
        my_str=""
        my_str+="AssignmentId:"+str(self.get_id())+"\t"
        my_str+=" Description:" + self.get_description()+"\t"
        return my_str



       
       
def tests():
    
    m=Assignment(4, "5 ex")
    
    
    assert m.get_description() == "5 ex"
    #assert m.get_grade() == 5
    assert m.get_id() == 4
    assert (m == m) == True
    
     
tests()
