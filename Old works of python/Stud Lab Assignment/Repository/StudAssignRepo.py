'''
Created on Nov 10, 2015

@author: Norbi
'''
from Domain.StudAssign import *
from Domain.DeadlinesD import *
from Domain.StudentD import *
from Domain.AssignmentD import *

class StudAssignRepo :
    
    def __init__(self):
        '''
        constructor for list in repository
        '''
        self.__sa_list=[]
    
    def __len__(self):
        '''
        returns the length of the list
        '''
        return len(self.__sa_list)
    
    def get_list(self):
        '''
        returns the list in repository
        '''
        return self.__sa_list
    
    def add(self,sa):
        '''
        adds in the list an object StudAssign
        '''
        self.__sa_list.append(sa)
    
    def get_by_stud(self,stud):
        '''
        gets an object studassign by student
        '''
        
        lst=self.get_list()
        for st in lst :
            if st.get_stud() == stud :
                return st
        return False
    
    def remove_by_stud(self,stud):
        '''
        removes objects from listby assign
        '''
        sa=True
        bef_len=len(self)
        while not sa == False :
            sa=self.get_by_stud(stud)
        return not (bef_len == len(self))
        
    def get_by_assign(self,assign):
        '''
        searches an object studassign by assign
        '''
        lst=self.get_list()
        for st in lst :
            if st.get_assign() == assign :
                return st
        return False
    def remove_by_assign(self,assign):
        '''
        removes objects from list by assgin
        '''
        sa=True
        bef_len=len(self)
        while not sa == False :
            sa=self.get_by_assign(assign)
        return not (bef_len == len(self))
        
    def show_stud_assign(self):
        
        print(self.get_list())
        
def RepoTest():
    slst=StudAssignRepo()
    s=Students(5,"John",8)
    d=Deadlines(4,4,4)
    a=Assignments(5,"5 exercises",9)
    sa=StudAssign(s,a,d)
    
    slst.add(sa)
    assert slst.get_by_stud(s) == StudAssign(Students(5,"John",8),Assignments(5,"5 exercises",9),Deadlines(4,4,4))
    assert len(slst) == 1
    s=Students(5,"John",8)
    d=Deadlines(4,4,4)
    a=Assignments(5,"6 essays",6)
    sa=StudAssign(s,a,d)
    slst.add(sa)

    assert len(slst) == 2
    m=Students(5,"John",8)
    assert slst.remove_by_stud(m) == True
    assert len(slst) == 0
    s=Students(5,"John",8)
    d=Deadlines(4,4,4)
    a=Assignments(5,"5 exercises",9)
    sa=StudAssign(s,a,d)
    
    slst.add(sa)
    assert slst.get_by_stud(s) == StudAssign(Students(5,"John",8),Assignments(5,"5 exercises",9),Deadlines(4,4,4))
    assert len(slst) == 1
    s=Students(5,"John",8)
    d=Deadlines(4,4,4)
    a=Assignments(5,"6 essays",6)
    sa=StudAssign(s,a,d)
    slst.add(sa)
    assert slst.remove_by_assign(a) == True
    
    
    
RepoTest()
        
        