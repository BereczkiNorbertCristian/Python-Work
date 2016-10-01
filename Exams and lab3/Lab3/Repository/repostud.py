'''
Created on Nov 11, 2015

@author: Norbi
'''
from Domain.domstud import *
from Domain.Validity import *

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
        Exceptions:raises ObjectException if student already exists in the list
        """
        studValidator.validStud(student)
        if isinstance(self.fetch_stud(student.get_id()),Student) :
            raise ObjectException("Id already exists!!!")
        self.__stud_list.append(student)
    
    def __len__(self):
        '''
        returns the lenght of the stud_list
        '''
        return len(self.__stud_list)
    
    def get_all(self):
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
        input:studid-int
        """
        
        for i in range (0,len(self.__stud_list)) :
            if self.__stud_list[i].get_id() == studid :
                self.__stud_list.pop(i)
                return

        
    def update(self,newStud):
        """
        Updates the student using setters
        Input:studid-int , name-string , group-int
        Exceptions:raises ObjectException if we have no student to be updated
        """
        stud=self.fetch_stud(newStud.get_id())
        if not isinstance(stud,Student):
            raise ObjectException("There is no student with this ID!!!")
        stud.update(newStud)
    
    def fetch_stud(self, studid):
        '''
        searches for a student by a given id then returns in the stud_list of the repository
        Args:studid - int Student's Id
        returns object student if it has found it by id
        returns false if it hasn't found and id that maches the given id
        '''
        lst=self.get_all()
        for stud in lst:
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
            print(str(stud))

def testRepositoryStud():
    myrepo=student_repository()
    
    s1=Student(5, "John", 7)
    s2=Student(6, "Marry", 8)
    studValidator.validStud(s1)

    assert len(myrepo) == 0
    try :
        myrepo.add(s1)
        assert True
    except ObjectException :
        assert False
    myrepo.add(s2)
    
    assert len(myrepo) == 2
    
    myrepo.remove_by_id(5)
    
    assert len(myrepo) == 1
    
    myrepo.update(6,"Carlie",3)
    
    m=Student(6, "Carlie", 3)
    assert len(myrepo) == 1

    m=Student(6,"carlie",3)
    try:
        studValidator.validStud(m)
        False
    except ObjectException as e :
        print(e)
        assert True

    
    

    
#testRepositoryStud()



