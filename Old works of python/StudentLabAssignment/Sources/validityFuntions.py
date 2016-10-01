'''
Created on Oct 31, 2015

@author: Norbi
'''
def read_positive_integer(message):
    n=-1
    while n < 0 :
        try:
            n=int (input (message))
            return n
        except ValueError:
            print("Please insert a number that is positive")
    
    
def read_day(message):
    day=-1
    while not (day>1 and day<32):
        try:
            day=int(input(message))
            return day
        except ValueError:
            print("Please introduce a day betweem 1-31")    
            
def read_month(message):
    month=-1
    while month < 1 or month > 12 :
        try:
            month=int(input(message))
            return month
        except ValueError:            
            print("Please introduce a month between 1-12")
            
def read_year(message):
    return read_positive_integer(message)

def simple_read(message):
     
    n=input(message)
    return n
 
def read_good_option(op_list):
    option= int (input("choose option:"))
    
    while not option in op_list: 
        
        option=int(input("Please introduce an option between" + str(op_list)))
    
    return option
            
            