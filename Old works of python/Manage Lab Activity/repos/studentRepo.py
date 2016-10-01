
from validation.validation import TeacherException
from domains.Student import Student

class StudentRepo():

    _fName="student.txt"

    def __init__(self):

        self.__data=[]
        self._loadFromFile()


    def add(self,student):
        '''
        adds to the repo a student
        :param student: object type student
        :return:
        exception: if id already raises exception
        '''
        if student in self.__data :
            raise TeacherException("Student with this id already in repo!!!")
        else:
            self.__data.append(student)

    def get_all(self):

        return self.__data

    def _loadFromFile(self):
        """
        loads from file the  data into the repo
        :return:
        exception:raises exception if could not open file
        """
        try:
            f=open(self._fName,"r")
        except IOError:
            print("FILE COULD NOT BE OPENED!!!")
            return

        line=f.readline().strip()

        while line!="":

            studId,name=line.split(" ")
            student=Student(int(studId),name)
            try:
                self.add(student)
            except TeacherException as e:
                print(e)

            line=f.readline().strip()


        f.close()