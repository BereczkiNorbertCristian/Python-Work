'''
Created on Nov 9, 2015

@author: Norbi
'''

from Domain.StudentD import *
from Validity.MyValidFuntions import ObjectException
class StudValid :
    @staticmethod
    def valid_stud(student):
        error_msg=""
        
        if student.get_id() == "" :
            error_msg+="You have not introduced an id!"
        else :
            try :
                int(student.get_id())
            except ValueError :
                error_msg+="You have not introduced a number for the id!"
            
        if student.get_name() == "" :
            error_msg+="You have not introduced a name!"
            
        if student.get_group() == "" :
            error_msg+="You have not introduced a group!"
        else :  
            try :
                int(student.get_group())
            except ValueError:
                error_msg+="You have not introduced a number for the group"
        
        if len(error_msg)>0 :
            raise ObjectException(error_msg)

def test_stud_valid():
    '''
    sa=Students(12,"John",9)
    try :
        StudValid.valid_stud(Students(3,"car",8))
    except ObjectException as e:
        print(e)
    
    assert not len(StudValid.valid_stud(Students("","Marry",8))) == 0
    assert StudValid.valid_stud(Students("","Marry",8)) == "You have not introduced an id!"
    assert StudValid.valid_stud(Students("ana","Carrie",9)) == "You have not introduced a number for the id!"           
    '''
    pass
test_stud_valid()

class AssignValid :
    @staticmethod
    def valid_assign(assign):
        error_msg=""
        
        if assign.get_id() == "":
            error_msg+="The assignment cannot be without an id!"
        else :
            try :
                int(assign.get_id())
            except ValueError:
                error_msg+="The you do not have a number for the id!"
        
        if assign.get_description() == "" :
            error_msg+="The assignment does not have a name!"
            
        if assign.get_grade() == "":
            error_msg+="The assignment does not have a grade!"
        
        pass
        



