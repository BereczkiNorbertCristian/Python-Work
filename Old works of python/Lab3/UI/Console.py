'''
Created on Nov 11, 2015

@author: Norbi
'''

from Domain.domstud import *
from Domain.domassign import *
from Domain.domdeadline import *
from Domain.domstudassign import *
from Domain.Validity import *
from Repository.repoassign import *
from Repository.repostud import *
from Repository.repostudassign import *
from Ctrl.ctrlassign import *
from Ctrl.ctrlstud import *
from Ctrl.ctrlstudassign import *
from copy import deepcopy

class Console:
    @staticmethod
    def read_student():
        '''
        reads studid ,name and groud
        Returns:object type Student with it's atributes read

        '''
        studid=Validator.read_positive_integer("Introduce student's ID:")
        name=Validator.simple_read("Introduce student's name:")
        group=Validator.read_positive_integer("Introduce student's group:")

        return Student(studid, name, group)
    @staticmethod
    def read_assignment():
        """
        uses read functions to read from the user assignment elements
        returns: Assignments object newly created
        """
        studid = Validator.read_positive_integer("Introduce assignment's id for the assignment:")
        description = Validator.simple_read("Introduce a description:")


        return Assignment(studid, description)
    @staticmethod
    def read_deadline():
        '''
        reads a readline
        Returns:object type Deadline newly created with it's atributes
        '''
        day=Validator.read_day("Introduce day for deadline:")
        month=Validator.read_month("Introduce month for deadline:")
        year=Validator.read_year("Introduce year for deadline:")

        d=Deadlines(day,month,year)
        return d
    @staticmethod
    def print_menu():
        '''
        Prints a menu
        '''
        str="""
        1---Add student
        2---Add assignment
        3---Assign(associate) student to assignmet
        4---Remove student by id
        5---Remove assignment by id
        6---Remove associtation
        7---Update student by id
        8---Update assignment by id
        9---Update association
        10---Fetch student by id
        11---Fetch assignment by id
        12---Fetch association
        13---Show students
        14---Show Assignments
        15---Show StudAssign
        16---Undo
        17---Characteristics
        18---Redo

        0---Exit
        """
        print(str)

    def __init__(self,stud_controller,assign_controller,studassign_controller,undo_controller):
        '''
        contructor for console class
        Args:
            stud_controller: controller for students
            assign_controller: controller for assignments
            studassign_controller: controller meant for StudAssign's
            undo_controller: controller meant for undo

        '''
        self.__ctrl_stud = stud_controller
        self.__ctrl_assign = assign_controller
        self.__ctrl_studassign=studassign_controller
        self.__ctrl_undo=undo_controller

    def add_student(self):
        """
        adds student and if the student's id is already in the list then it enters except branch
        """
        
        stud=Console.read_student()
        try :
            self.__ctrl_stud.add_stud(stud)
        except ObjectException as e:
            print(e)
    
    def remove_stud_by_id(self):
        """
        tries to remove a student with an id (which is firstly read from the user)
        then if it doesn't already exists prints coresponding message
        """
        studid=Validator.read_positive_integer("Please insert the id of the student you want ot be removed:")
        st=self.__ctrl_stud.fetch_stud(studid)

        if not isinstance(st,Student) :
            print("We cannot remove anything because the id doesn't exist!")
        else :
            self.__ctrl_stud.remove_by_id(studid)
        
    def update_stud(self):
        """
        uses read functions to read how the student will be updated and updates the student with the given id
        """
        studid=Validator.read_positive_integer("Introduce student's ID which will be updated:")
        name=Validator.simple_read("Introduce student's new name:")
        group=Validator.read_positive_integer("Introduce student's new group:")
        newStud=Student(studid,name,group)
        try :
            self.__ctrl_stud.update(newStud)
        except ObjectException as e :
            print(e)


    def fetch_stud(self):
        '''
        searches for a student given the studid
        if found 
        '''
        studid = Validator.read_positive_integer("Student's id who will be fetched:")
        student=self.__ctrl_stud.fetch_stud(studid)
        if not isinstance(student,Student) :
            print("Student's id not found!")
        else :
            print(str(student))

    def add_assign(self):
        """
        tries to add an assginment to the repository and if it's id already exists then it goes on the except branch
        """
        assign=Console.read_assignment()
        try:
            self.__ctrl_assign.add_assign(assign)
        except ObjectException as e :
            print(e)
        
        
    def remove_assign_by_id(self):
        """
        removes assignment by id and reads the studid
        and if it doesn't exists any student with corresponding id show appropriate message
        """

        assignid=Validator.read_positive_integer("Id to be removed:")
        asg=self.__ctrl_assign.fetch_assign(assignid)
        if not isinstance(asg,Assignment) :
            print("There is no assignment to be removed!")
        else :
            self.__ctrl_assign.remove_by_id(assignid)
    
    def update_assign(self):
        """
        Updates an assignment
        reads the elements to be put in the assignment and then introduces them there
        """
        assignid = Validator.read_positive_integer("Introduce assignmet's id for the assignment to be updated:")
        description = Validator.simple_read("Introduce a description:")
        newAssign=Assignment(assignid,description)
        try:
            self.__ctrl_assign.update(newAssign)
        except ObjectException as e:
            print(e)
        
    def fetch_assign(self):
        '''
        Searches for an assignment
        if found shows the object student
        if not appropriate message
        '''
        studid=Validator.read_positive_integer("Introduce assignemt's id to be fetched")
        assign=self.__ctrl_assign.fetch_assign(studid)
        if assign == False :
            print("Assignment's id not found!")
        else :
            print(str(assign))
        

    def show_students(self):
        '''
        Shows list of students by calling students's controller method for doing that
        '''
        self.__ctrl_stud.showstuds()
    
    def show_assignments(self):
        '''
        Shows list of assignments by calling assignments's controller method for doing that
        '''
        self.__ctrl_assign.showassigns()
    def show_stud_assign(self):
        '''
        Shows list of associations by calling associations's controller method for doing that
        '''
        self.__ctrl_studassign.show_stud_assign()

    def associate(self):
        '''
        associates a student with an assignment and atributes it a deadline and a grade
        '''
        studId=Validator.read_positive_integer("Introduce student's id:")
        assignId=Validator.read_positive_integer("Introduce assignment's id:")
        d=Console.read_deadline()
        grade=Validator.read_grade([1,2,3,4,5,6,7,8,9,10])

        try :
            self.__ctrl_studassign.associate(studId,assignId,d,grade)
        except ObjectException as e :
            print(e)

    def fetch_association(self):
        '''
        Searches and prints an association if found in the repository of associations
        '''
        studId=Validator.read_positive_integer("Introduce association's student id to be fetched:")
        assignId=Validator.read_positive_integer("Introduce association's assignment id to be fetched:")
        try :
            assoc=self.__ctrl_studassign.fetch_association(studId,assignId)
            print(assoc)
        except ObjectException as e :
            print(e)
    def update_association(self):
        '''
        read the updated atributes
        searches for an association
        if found ,it updates it
        Returns:

        '''
        studId=Validator.read_positive_integer("Introduce association's student id to be updated:")
        assignId=Validator.read_positive_integer("Introduce association's assignment id to be updated:")
        d=Console.read_deadline()

        print("New grade will be introduced!")
        g=Validator.read_grade([1,2,3,4,5,6,7,8,9,10])
        stud=self.__ctrl_stud.fetch_stud(studId)
        assign=self.__ctrl_assign.fetch_assign(assignId)
        newAssoc=StudAssign(stud,assign,d,g)

        try :
            self.__ctrl_studassign.update(newAssoc)
        except ObjectException as e :
            print(e)


    def remove_association(self):
        '''
        removes an association
        Returns:nothing
        '''
        try :
            self.__ctrl_studassign.remove_association()
        except ObjectException as e :
            print(e)

    def AvgGradeBelow5(self):
        '''
        gets ,then shows a list of students with average grade below 5
        Returns:

        '''
        lst=self.__ctrl_studassign.AvgGradeBelow5()
        if len(lst) == 0:
            print("There is no student with grade below 5!!!Or list of associations is empty!!!")
        for objGrade in lst :
            print(objGrade.get_stud())
    @staticmethod
    def printListOfStuds(lst):
        '''
        print a list of students
        Args:
            lst: list of objects (usually type Student)
        '''
        if len(lst) == 0 :
            print("The list of student's is empty!!!So we haven't found an association related to the assignment introduced!!!Please think of an assignment that matches an existing association!!!")
            return
        for assoc in lst:
            print(assoc.get_stud())

    def subMenuCharacteristics(self):
        '''
        submenu for characteristics
        '''
        stt=("""
        1---Show students with average grade below 5
        2---Order of an assignment by student's name
        3---Order of an assignment by the grade
        """)
        print(stt)
        option=Validator.read_good_option([1,2,3])
        if option == 1:
            self.AvgGradeBelow5()
        elif option == 2 :
            assign=Console.read_assignment()
            lst=self.__ctrl_studassign.SortAlphabetical(assign)
            Console.printListOfStuds(lst)
        elif option == 3 :
            assign=Console.read_assignment()
            lst=self.__ctrl_studassign.SortByGrade(assign)
            Console.printListOfStuds(lst)


    def main_menu(self):
        '''
        Maine Menu
        '''
        '''
        self.__ctrl_stud.add_stud(Student(1,"peter",1))
        self.__ctrl_stud.add_stud(Student(2,"marry",2))
        self.__ctrl_stud.add_stud(Student(3,"hansel",3))
        self.__ctrl_assign.add_assign(Assignment(1,"6 problems"))
        self.__ctrl_assign.add_assign(Assignment(2,"10 exerises"))
        self.__ctrl_assign.add_assign(Assignment(3,"9 essays"))
        d=Deadlines(2,2,2)
        grade=9
        self.__ctrl_studassign.associate(1,1,d,6)
        self.__ctrl_studassign.associate(1,2,d,grade)
        self.__ctrl_studassign.associate(1,3,d,grade)
        self.__ctrl_studassign.associate(3,2,d,grade)
        self.__ctrl_studassign.associate(3,1,d,grade)
        self.__ctrl_studassign.associate(2,3,d,grade)
        self.__ctrl_studassign.associate(2,1,d,grade)
        '''
        option=-1

        while not option == 0 :
            Console.print_menu()
            option=Validator.read_good_option([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

            if option == 1:
                self.add_student()
            elif option == 2:
                self.add_assign()
            elif option == 3:
                self.associate()
            elif option == 4 :
                self.remove_stud_by_id()
            elif option == 5 :
                self.remove_assign_by_id()
            elif option == 6 :
                self.remove_association()
            elif option == 7 :
                self.update_stud()
            elif option == 8:
                self.update_assign()
            elif option == 9 :
                self.update_association()
            elif option == 10 :
                self.fetch_stud()
            elif option == 11 :
                self.fetch_assign()
            elif option == 12 :
                self.fetch_association()
            elif option == 13 :
                Console.show_students(self)
            elif option == 14 :
                Console.show_assignments(self)
            elif option == 15 :
                Console.show_stud_assign(self)
            elif option == 16 :
                undone=self.__ctrl_undo.undo()
                if undone == False :
                    print("You cannot undo anymore!!!")
            elif option == 17 :
                self.subMenuCharacteristics()
            elif option == 18 :
                redone=self.__ctrl_undo.redo()
                if redone == False :
                    print("You cannot redo anymore!!!")
            '''
            elif option == 17 :
                if len(redo_opt_lst) > 0:
                    bef_opt=redo_opt_lst.pop()
                    lst_bef_opt.append(bef_opt)
                    if bef_opt % 2 == 0 :
                        self.__ctrl_assgin.redo()
                    else :
                        self.__ctrl_stud.redo()
                else :
                    print("You cannot do redo anymore!")
            '''
            
        print("You have exited!")

        
        
