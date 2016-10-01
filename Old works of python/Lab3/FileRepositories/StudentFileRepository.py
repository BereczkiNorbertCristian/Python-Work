
from Domain.domstud import *
from Repository.repostud import *

class StudentFileRepository(student_repository) :
    _file_name="Students.txt"
    """
    _file_name file's name from which we will read
    """
    def __init__(self):
        '''
        constructor for file repo
        '''
        student_repository.__init__(self)
        self._loadFromFile()

    def add(self,student):
        '''
        Args:
            student:object type student
        adds a student to the repo
        '''
        student_repository.add(self,student)
        self._storeToFile()

    def update(self,newStud) :
        '''
        updated a student with a new student's atributes
        Args:
            newStud:object type student
        '''
        student_repository.update(self,newStud)
        self._storeToFile()

    def remove_by_id(self,studid):
        '''
        removes a student based on his id
        Args:
            studid: int
        '''
        student_repository.remove_by_id(self,studid)
        self._storeToFile()

    def showstuds(self):
        '''
        shows the list of students
        '''
        student_repository.showstuds(self)

    def _storeToFile(self):
        '''
        stores to file the information in the repository
        Output:write in file f the repo
        '''
        f=open(self._file_name,"w")
        students=student_repository.get_all(self)
        print(len(students))
        for s in students :
            sf=str(s.get_id()) + ";" + s.get_name() + ";" + str(s.get_group()) + "\n"
            f.write(sf)
        f.close()

    def fetch_stud(self, studid):
        '''
        searches for a student in the repository based on his id and the returns the object
        Args:
            studid:int

        Returns:object type student

        '''
        return student_repository.fetch_stud(self,studid)

    def _loadFromFile(self):
        '''
        read from file
        Input:information which will be stored in the repository
        '''
        print("XXXXXX")
        try :
            f= open(self._file_name,"r")
        except IOError:
            return
        line=f.readline().strip()
        while line != "" :
            t=line.split(";")
            s=Student(int (t[0]),t[1],int(t[2]))
            student_repository.add(self,s)
            line=f.readline().strip()
        f.close()

