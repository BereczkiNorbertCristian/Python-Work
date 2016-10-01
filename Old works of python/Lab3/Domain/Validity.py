'''
Created on Nov 11, 2015

@author: Norbi
'''


class Validator :
    @staticmethod
    def read_positive_integer(message):
        """
        Reads a positive integer
        input:message
        output:n as integer no
        """
        n=-1
        while n < 0 :
            try:
                n=int (input (message))
            except ValueError:
                print("Please insert a number that is positive")
    
        return n
    @staticmethod
    def read_day(message):
        """
        Args:message-string
        Reads day between 1-31
        """
        day=-1
        while not (day>1 and day<32):
            try:
                day=int(input(message))
            except ValueError:
                print("Please introduce a day betweem 1-31")
        return day
    @staticmethod        
    def read_month(message):
        """
        Args:message-string
        Reads a month between 1-12
        Returns:month-int between 1->12
        """
        month=-1
        while month < 1 or month > 12 :
            try:
                month=int(input(message))
                return month
            except ValueError:            
                print("Please introduce a month between 1-12")
    @staticmethod        
    def read_year(message):
        """
        Args:message-string to be shown to user
        reads a year
        Returns:positive integer
        """
        return Validator.read_positive_integer(message)
    @staticmethod
    def simple_read(message):
        '''

        Args:
            message:string

        Returns:n-anything that was read from user (string)

        '''
        n=input(message)
        return n
    @staticmethod
    def read_grade(grade_list):
        try :
            grade=int(input("Introduce grade:"))
        except ValueError :
            print("""Don't be hasty!
You have not introduced antyhing.""")
            return 

        print(grade_list)

        while not grade in grade_list and not grade == None :
            try:
                grade=int (input("Please introduce a grade between" + str(grade_list)))
            except ValueError:
                print("You have not inserted a number!")
                grade=-1
        
        return grade
        
    @staticmethod
    def read_good_option(op_list):
        """
        Reads an option between list op_list
        if enter is pressed too early then message
        Returns:option-int between op_list
        """
        try :
            option= int (input("choose option:"))
        except ValueError :
            print("""Don't be hasty!
You have not introduced antyhing.""")
            return 
        
        while not option in op_list: 
            try :
                option=int(input("Please introduce an option between" + str(op_list)))
            except ValueError:
                print("You have not introduced an integer!")
                option=-1
        return option
    @staticmethod
    def sverifyid(verifstud,studrepo):
        """
        Verifies if id of student is in the list of students
        Input:student and repository of students
        Output:0 if founnd
        1 if not found
        """
        if not studrepo.get_all() :
            return True
    
        for stud in studrepo.get_all() :
            if verifstud.get_id() == stud.get_id() :
                return False
            return True

    @staticmethod
    def averifyid(verifassign,assignrepo):
        """
        Verifies if id is in list of assignments
        Input: student with the id which will be verified, repository of assginments
        Output:0 if found
        1 if not found
        """
        if not assignrepo.get_all() :
            return True
    
        for assign in assignrepo.get_all() :
            if verifassign.get_id() == assign.get_id() :
                return False
            return True

def veriftest():
    m=student_repository()
    s=Student(5, "john", 7)
    s1=Student(6, "marry", 8)
    
    m.add(s)
    m.add(s1)
    
    ver=Student(5, "", 0)
    Validator.sverifyid(ver, m)
    
#veriftest()

class ObjectException(Exception):
    
    def __init__(self,msg):
        self.__msg=msg
        
    def __str__(self):
        return self.__msg

class studValidator :

    @staticmethod
    def validStud(stud):
        """
        verifies if the atributes of stud are corectly introduced by certain rules
        Args:stud:object type Student
        Returns:
            object:
        """
        errMsg=""
        if not isinstance(stud,Student) :
            errMsg="The object is not type Student!"
        if not isinstance(stud.get_id(),int) or stud.get_id()<0 :
            errMsg+="Student Id is not a positive integer!"
        try :
            stud.get_name().isalpha
        except AttributeError :
            errMsg+="You have not introduced a name!"
        if not isinstance(stud.get_group(),int) or stud.get_group()<1 :
            errMsg+="Student's groud is not a positive integer!"

        if len(errMsg)>0 :
            raise ObjectException(errMsg)
from Domain.domstud import *
def teststudValidator():
    x=Student(-3,3,0)
    try:
        studValidator.validStud(x)
        assert False
    except ObjectException as e:
        if e == "Student Id is not a positive integer!You have not introduced a name!Student's groud is not a positive integer!" :
            assert True
        else:
            False
teststudValidator()