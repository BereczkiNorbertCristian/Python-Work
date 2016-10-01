'''
Created on Oct 31, 2015

@author: Norbi
'''


class Students:
    '''
    Student object contains 3 fields
    +__name
    +__id
    +__group
    Methods:
    
    '''
    def __init__(self,id_student,name,group):
        self.__id=id_student
        self.__name=name
        self.__group=group
    
    def __eq__(self,other):
        if other == None:
            return False
        return self.get_id == other.get_id
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_group(self):
        return self.__group
    
    def set_id(self,id_student):
        self.__id=id
        
    def set_name(self,name):
        self.__name=name
        
    def set_group(self,group):
        self.__group=group
    
    def __str__(self):
        my_string=""
        my_string="Name:" + str(self.get_name()) 
        my_string+= " " + "ID:" + str(self.get_id()) 
        my_string+= " " + "Group:" + str(self.get_group())
        return my_string    
        
        
class Assignments:
    '''
    Object assignmet has 4 entities
    +__studentid
    +__description
    +__dedline
    +__grade
    '''
    
    def __init__(self,studentid,description,deadline,grade):
        self.__studid=studentid
        self.__description=description
        self.__deadline=deadline
        self.__grade=grade
    
    def __eq__(self,other):
        return self.get_studid == other.get_studid and self.get_description == other.get_description
    
    def get_id(self):
        return self.__studid
    
    def get_description(self):
        return self.__description
    
    def get_deadline(self):
        return self.__deadline
    
    def get_grade(self):
        return self.__grade
    
    def set_id(self,studid):
        self.__studid=studid
        
    def set_description(self,description):
        self.__description=description
        
    def set_deadline(self,deadline):
        self.__deadline=deadline
    
    def set_grade(self,grade):
        self.__grade=grade
    
    def __str__(self):
        
        my_string = "Student ID:" + str(self.__studid)
        my_string += " " + "Description:" + self.__description
        my_string += " " + "Deadline" + str(self.__deadline)
        my_string += " " + "Grade" + str(self.__grade)
        return my_string
        
        
        
class Deadlines:
    '''
    deadline object with 3 entities:
    --day
    --month
    --year
    '''
    def __init__(self,day,month,year):
        self.__day=day
        self.__month=month
        self.__year=year
        
    def __eq__(self,other):
        return self.get_day() == other.get_day() and self.get_month() == other.get_month() and self.get_year() == other.get_year()
        
    def get_day(self):
        return self.__day
    
    def get_month(self):
        return self.__month
    
    def get_year(self):
        return self.__year
    
    def set_day(self,day):
        self.__day=day
        
    def set_month(self,month):
        self.__month=month
        
    def set_year(self,year):
        self.__year=year
        
    def __str__(self):
        my_string=str(self.__day) + "." + str(self.__month) + "." + str(self.__year)
        return my_string
    