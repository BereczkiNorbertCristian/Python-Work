'''
Created on Nov 11, 2015

@author: Norbi
'''
from Domain.domassign import *
from Domain.Validity import *
class assignment_repository :
    
    def __init__(self):
        '''
        constructor for the repository of assignments
        '''
        self.__assign_list=[]
        
    def add(self,assignment):
        '''
        ads an assignment to the list
        '''
        if isinstance(self.fetch_assign(assignment.get_id()),Assignment) :
            raise ObjectException("Assignment id already exists!!!")
        self.__assign_list.append(assignment)
    
    def get_all(self):
        '''
        gets the list of assignments from the repository
        '''
        return self.__assign_list

    def __len__(self):
        '''
        returns the length of the repository
        '''
        return len(self.__assign_list)
    
    def __str__(self):
        '''
        returns a string with the meaning of all elements in the repository transformed to string
        '''
        my_string = ""
        for assign in self.__assign_list :
            my_string+= str(assign)
        return my_string
        
    def remove_by_id(self,assignid):
        """
        Searches for an assignment in the assignment list and if it found removes the assignment
        """
        lst=self.get_all()
        for i in range (0,len(lst)) :
            if lst[i].get_id() == assignid :
                lst.pop(i)
                return 
    
    def fetch_assign(self, studid):
        '''
        searches for an assignment in the list by an id
        returns object assign if id was found maching with studid
        returns false if id was not found
        '''
        lst=self.get_all()
        for assign in lst :
            if assign.get_id() == studid :
                return assign
            
        return False
    
    def update(self,newAssign):
        '''

        Args:
            newAssign:-updated the newAssign
        Returns:nothing,just modifies
        Exception:raises Object Exception if there isn't an assignment to be updated
        '''
        assign=self.fetch_assign(newAssign.get_id())
        if not isinstance(assign,Assignment) :
            raise ObjectException("AssignmentId not found!!!")

        assign.update(newAssign)
        
    def showassigns(self):
        '''
        shows all the assignments
        '''
        if not self.__assign_list :
            print("The list of assignments is empty!")
            return 
        for assign in self.__assign_list :
            print(str (assign))
    
def testrepass():
    repo=assignment_repository()
    #d=Deadlines(11,11,11)
    a=Assignment(5, "5 exercises", 6)
    
    assert len(repo) == 0
    
    repo.add(a)
    assert len (repo) == 1
    
    repo.remove_by_id(5)
    assert len(repo) == 0
    
    
    
    
    
    
    
    
#testrepass()
        
