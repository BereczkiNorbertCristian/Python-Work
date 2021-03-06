'''
Created on Nov 3, 2015

@author: Norbi
'''
class Deadlines:
    '''
    deadline object with 3 entities:
    --day
    --month
    --year
    '''
    def __init__(self,day,month,year):
        '''
        constr for deadline
        '''
        self.__day=day
        self.__month=month
        self.__year=year
        
    def __eq__(self,other):
        '''
        verifies if 2 deadlines are equal
        '''
        return self.get_day() == other.get_day() and self.get_month() == other.get_month() and self.get_year() == other.get_year()
        
    def get_day(self):
        '''
        getter for day
        '''
        return self.__day
    
    def get_month(self):
        '''
        getter for month
        '''
        return self.__month
    
    def get_year(self):
        '''
        getter for year
        '''
        return self.__year
    
    def set_day(self,day):
        '''
        setter for day
        '''
        self.__day=day
        
    def set_month(self,month):
        '''
        setter for month
        '''
        self.__month=month
        
    def set_year(self,year):
        '''
        setter for year
        '''
        self.__year=year
        
    def __str__(self):
        '''
        returns the object in the form of a string
        '''
        my_string=str(self.__day) + "." + str(self.__month) + "." + str(self.__year)
        return my_string
    

