

from Domain.domassign import *
from Repository.repoassign import *

class AssignmentFileRepository(assignment_repository):
    '''
    _fName file's name from which we read and where we will write
    '''
    _fName="Assignments.txt"

    def __init__(self):
        '''
        Constructor class for file repository
        '''
        assignment_repository.__init__(self)
        self._loadFromFile()

    def add(self,assignment) :
        '''
        Args:
            assignment:object type assignment
        '''
        assignment_repository.add(self,assignment)
        self._storeToFile()


    def update(self,newAssign):
        '''
        Args:
            newAssign:object type assignment
        '''
        assignment_repository.update(self,newAssign)
        self._storeToFile()

    def remove_by_id(self,assignid):
        '''
        Args:
            assignid:int
        removed an assignment by it's id
        '''
        assignment_repository.remove_by_id(self,assignid)
        self._storeToFile()

    def _storeToFile(self):
        '''
        writes in the file the repository's information
        Output:writes repository
        '''
        f=open(self._fName,"w")
        assignments=super().get_all()
        for a in assignments :
            af=str(a.get_id()) + ";" + a.get_description() + "\n"
            f.write(af)
        f.close()

    def _loadFromFile(self):
        '''
        reads from file the repository
        Input:reads from file the repository
        '''
        try:
            f=open(self._fName,"r")
        except IOError:
            return

        line=f.readline().strip()
        while line != "" :
            t=line.split(";")
            a=Assignment(int(t[0]),t[1])
            assignment_repository.add(self,a)
            line=f.readline().strip()
        f.close()


