'''
Created on Nov 11, 2015

@author: Norbi
'''
from Domain.Validity import ObjectException

class StudAssignRepo :
    
    def __init__(self):
        '''
        constructor for list in repository
        '''
        self.__sa_list=[]
    
    def __len__(self):
        '''
        returns: the length of the list
        '''
        return len(self.__sa_list)
    
    def get_all(self):
        '''
        returns: the list in repository
        '''
        return self.__sa_list
    
    def add(self,sa):
        '''
        adds in the list an object StudAssign
        Args:sa - object type StudAssign
        Exception:raises ObjectException if association like sa already exists
        '''
        if self.identical_search(sa) == True :
            raise ObjectException("Association between this student and this assignment already exists!!!")
        else :
            self.__sa_list.append(sa)

    def identical_search(self,sa):
        '''
        searches for an association equal to sa's student and assignment
        Args:
            sa:object type StudAssign
        Returns:True-if an association's student and assignment equals to sa student and assignment
        False-if not even an association's student and assignemnt equal to sa's hasn't been found
        '''
        lst=self.get_all()
        for i in lst :
            if sa.get_stud() == i.get_stud() and sa.get_assign() == i.get_assign() :
                return True
        return False

    def fetch_association(self,stud,assign):
        '''

        Args:
            studId:int - sduent's id in the association
            assignId: int - assignment's id in the association

        Returns:

        '''
        lst=self.get_all()
        for assoc in lst :
            if assoc.get_stud() == stud and assoc.get_assign() == assign :
                return assoc
        raise ObjectException("There is no association between"+str(stud)+"and"+str(assign))

    def update(self,assoc,upAssoc):
        """
        updated the current association
        Args:
            assoc: object type StudAssign
            upAssoc: object type StudAssign
        """
        foundA=self.fetch_association(assoc.get_stud(),assoc.get_assign())
        foundA.update(upAssoc)

    def search_by_index(self,assoc):

        lst=self.get_all()
        for i in range(0,len(lst)) :
            if lst[i] == assoc :
                return i
        raise ObjectException("Nothing to be found!!!")

    def RepoRemove(self,stud,assign):
        """
        removes from repository an association based on student's id and assignment's id
        Returns:
        """
        assoc=self.fetch_association(stud,assign)
        i=self.search_by_index(assoc)
        lst=self.get_all()
        lst.pop(i)

    def remove_stud(self,stud):
        '''
        Deletes the association StudAssign in which object stud is found
        Args:
            stud:student to be searched for and the association StudAssign in which it is found will be deleted
        Returns:sa=as object-if an occurence of object stud is found
        sa=False-if not even an occurence of object stud is found
        '''
        lst=self.get_all()
        for i in range(0,len(lst)):
            if lst[i].get_stud() == stud :
                return lst.pop(i)
        return False

    def remove_by_stud(self,stud):
        '''
        removes objects from listby assign
        '''
        appeared=True
        while appeared == True :
            appeared=self.remove_stud(stud)
    def remove_assign(self,assign):
        '''
        Deletes the association StudAssign in which object stud is found
        Args:
            stud:student to be searched for and the association StudAssign in which it is found will be deleted
        Returns:sa=as object-if an occurence of object stud is found
        sa=False-if not even an occurence of object stud is found
        '''
        lst=self.get_all()
        for i in range(0,len(lst)):
            if lst[i].get_assign() == assign :
                return lst.pop(i)
        return False

    def remove_by_assign(self,assign):
        '''
        removes objects from listby assign
        '''
        appeared=True
        while appeared == True :
            appeared=self.remove_assign(assign)


    """
    def fetch_by_stud(self, stud):
        '''
        gets an object studassign by student
        '''
        
        lst=self.get_all()
        for st in lst :
            if st.fetch_stud() == stud :
                return st
        return False

    def fetch_by_assign(self, assign):
        '''
        searches an object studassign by assign
        '''
        lst=self.get_all()
        print(len(lst))
        for st in range(0,len(lst)) :
            if lst[st].fetch_assign() == assign :
                return lst[st]
        return False
    def remove_by_assign(self,assign):
        '''
        removes objects from list by assign
        '''
        sa=True
        bef_len=len(self)
        s=Student(1, "d", 1)
        d=Deadlines(1,1,1)
        asg=Assignment(1, "d", 1)
        sdasg=StudAssign(s,asg,d)
        while sa == True or type(sa) == type(sdasg) :
            sa=self.fetch_by_assign(assign)
            del sa
        return not (bef_len == len(self))
    """
    def show_stud_assign(self):

        lst=self.get_all()
        for e in lst :
            print(e)

def RepoTest():
    slst=StudAssignRepo()
    s=Student(5, "John", 8)
    d=Deadlines(4,4,4)
    a=Assignment(5, "5 exercises")
    sa=StudAssign(s,a,d,9)
    
    slst.add(sa)

    assert len(slst) == 1
    s=Student(5, "John", 8)
    d=Deadlines(4,4,4)
    a=Assignment(5, "6 essays")
    sa=StudAssign(s,a,d,6)
    slst.add(sa)

    assert len(slst) == 2
    m=Student(5, "John", 8)
    assert slst.remove_by_stud(m) == True
    assert len(slst) == 0
    s=Student(5, "John", 8)
    d=Deadlines(4,4,4)
    a=Assignment(5, "5 exercises", 9)
    sa=StudAssign(s,a,d)
    
    slst.add(sa)
    assert slst.fetch_by_stud(s) == StudAssign(Student(5, "John", 8), Assignment(5, "5 exercises", 9), Deadlines(4, 4, 4))
    assert len(slst) == 1
    s=Student(5, "John", 8)
    d=Deadlines(4,4,4)
    a=Assignment(5, "6 essays", 6)
    sa=StudAssign(s,a,d)
    slst.add(sa)
    assert slst.remove_by_assign(a) == True
    
    
    
#RepoTest()
        
        
