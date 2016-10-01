'''
Created on Oct 31, 2015

@author: Norbi
'''
from copy import deepcopy
from Repository import *
from Domain import *
from validityFuntions import *
from Controller import StudController
from asgcontrol import *

class Console:
    
    def __init__(self,stud_controller,assign_controller):
        
        self.__ctrl_stud = stud_controller
        self.__ctrl_assign = assign_controller
        
    def read_student(self):
    
        studid=read_positive_integer("Introduce student's ID:")
        name=simple_read("Introduce student's name:")
        group=read_positive_integer("Introduce student's group:")
        
        return Students(studid,name,group)
    
    
    def add_student(self):
        
        stud=Console.read_student(self)
        self.__ctrl_stud.add_stud(stud)
    
    def remove_stud_by_id(self):
        
        studid=read_positive_integer("Please insert the id of the student you want ot be removed")
        self.__ctrl_stud.remove_by_id(studid)
        
    def update_stud(self):
    
        studid=read_positive_integer("Introduce student's ID which will be updated:")
        name=simple_read("Introduce student's name:")
        group=read_positive_integer("Introduce student's group:")
        
        self.__ctrl_stud.update(studid,name,group)
    
    def fetch_stud(self):
        
        studid = read_positive_integer("Student's id who will be fetched")
        student=self.__ctrl_stud.get_by_id(studid)
        print(str(student))
    
    def undo_student(self):
        
        self.__ctrl_stud.undo()
    
    def read_assignment(self):
        
        studid = read_positive_integer("Introduce student's id for the assignment")
        description = simple_read("Introduce a description")
        day=read_day("Introduce day for deadline")
        month=read_month("Introduce month for deadline")
        year=read_year("Introduce year for deadline")
        
        d=Deadlines(day,month,year)
        print("Grade:")
        grade=read_good_option([1,2,3,4,5,6,7,8,9])
        
        return Assignments(studid,description,d,grade)
    
    def add_assign(self):
        
        assign=Console.read_assignment(self)
        self.__ctrl_assign.add_assign(assign)
        
    def remove_assign_by_id(self):
        
        studid=read_positive_integer("Id to be removed")
        self.__ctrl_assign.remove_by_id(studid)
    
    def update_assign(self):
        
        studid = read_positive_integer("Introduce student's id for the assignment to be updated")
        description = simple_read("Introduce a description")
        day=read_day("Introduce day for deadline")
        month=read_month("Introduce month for deadline")
        year=read_year("Introduce year for deadline")
        
        d=Deadlines(day,month,year)
        
        grade=read_good_option([1,2,3,4,5,6,7,8,9])
        
        self.__ctrl_assign.update(studid,description,d,grade)
        
    def fetch_assign(self):
        
        studid=read_positive_integer("Introduce student's id to be fetched")
        assign=self.__ctrl_assign.get_assign(studid)
        print(str(assign))
        
    def undo_assign(self):
        
        self.__ctrl_assign.undo()
    
    def show_students(self):
        
        self.__ctrl_stud.showstuds()
    
    def show_assignments(self):
        
        self.__ctrl_assign.showassigns()
    
    def main_menu(self):
        option=-1
        
        while not option == 0 :
            print("""
            1---Add student
            2---Add assignment
            3---Remove student by id
            4---Remove assignment by id
            5---Update student by id
            6---Update assignment by id
            7---Fetch student by id
            8---Fetch assignment by id
            9---Undo
            10---Show students
            11---Show Assignments
            0---Exit
            """)
            option=read_good_option([0,1,2,3,4,5,6,7,8,9,10,11])
            
            if option == 1:
                self.add_student()
            elif option == 2:
                self.add_assign()
            elif option == 3:
                self.remove_stud_by_id()
            elif option == 4 :
                self.remove_assign_by_id()
            elif option == 5 :
                self.update_stud()
            elif option == 6 :
                self.update_assign()
            elif option == 7 :
                self.fetch_stud()
            elif option == 8:
                self.fetch_assign()
            elif option == 9 :
                if option % 2 == 0 :
                    self.undo_assign()
                else :
                    self.undo_student()
            elif option == 10 :
                Console.show_students(self)
            elif option == 11 :
                Console.show_assignments(self)

stud_repo=student_repository()
assign_repo=assignment_repository()
ctrl_stud=StudController(stud_repo)
ctrl_assign=AssignController(assign_repo)
ui=Console(ctrl_stud,ctrl_assign)
ui.main_menu()
        
        
        
        