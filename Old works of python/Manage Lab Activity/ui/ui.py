
from validation.validation import TeacherException
from domains.Lab import Lab
class Console:


    def __init__(self,ctrl):

        self.__ctrl=ctrl

    def show_students(self):

        students=self.__ctrl.get_all()

        for student in students:

            print(student)

    def show_labs(self):

        labs=self.__ctrl.get_allLabs()

        for lab in labs:
            print (lab)

    def add(self):

        try:
            studentId=int(input("Introduce student ID:"))
            labNumber=int(input("Introduce Lab Number:"))
            problemNumber=input("Introduce problem number:")

            self.__ctrl.add(Lab(studentId,labNumber,problemNumber))

        except ValueError:
            print("You have not introduced an integer for id or lab number!!!")
        except TeacherException as e:
            print(e)

    def oneStud_allLabs(self):

        try:
            studId=int(input("Introduce student's id:"))
            labs=self.__ctrl.oneStud_allLabs(studId)
            for lab in labs:
                print(lab)
        except ValueError:
            print("You have not introduced an integer id!!!")
        except TeacherException as e :
            print(e)

    def allStud_oneLab(self):

        try:

            labNr=int(input("Introduce lab number(integer):"))
            students=self.__ctrl.allStud_oneLab(labNr)
            for student in students:
                print(student)
        except ValueError:
            print("You have not introduced an integer!!!")


    def run(self):

        menu="""

        1---Show all students
        2---Assign a lab activity
        3---Show lab activities for a given student
        4---Show all students with the lab assignemnt for a given lab number
        5---Show all labs
        0---Exit

        """

        option = -1

        while option != 0 :

            print (menu)

            option=input("Introduce your option:")

            if option.strip() == "1":
                self.show_students()
            elif option.strip() == "2" :
                self.add()
            elif option.strip() == "5" :
                self.show_labs()
            elif option.strip() == "0":
                self.__ctrl.save()
                exit()
            elif option.strip() == "3":
                self.oneStud_allLabs()
            elif option.strip() == "4":
                self.allStud_oneLab()
            else :
                print("Not valid option!!!")
                continue




