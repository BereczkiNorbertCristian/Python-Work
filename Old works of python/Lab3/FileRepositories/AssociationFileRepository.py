

from Domain.domstudassign import *
from Repository.repostudassign import *
from Domain.domdeadline import *

class AssociationFileRepository(StudAssignRepo) :
    _fName="Associations.txt"
    """
    _fName -file's name from which we will read and write
    """
    def __init__(self,repoS,repoA) :
        '''

        Args:
            repoS:repository of students
            repoA:repository of assignments
        and initialises the repo with what it loads from the file

        '''
        StudAssignRepo.__init__(self)
        self.__repoS=repoS
        self.__repoA=repoA
        self._loadFromFile()


    def add(self,sa) :
        '''
        adds an association to the repository
        Args:
            sa:object type StudAssign
        '''
        StudAssignRepo.add(self,sa)
        self._storeToFile()

    def RepoRemove(self,studId,assignId):
        '''
        removes from the repository the association with studId and assignId
        Args:
            studId:int
            assignId: int
        '''
        StudAssignRepo.RepoRemove(self,studId,assignId)
        self._storeToFile()

    def remove_stud(self,stud):
        '''
        removes an association by a student
        Args:
            stud:object type Student
        '''
        assoc=StudAssignRepo.remove_stud(self,stud)
        self._storeToFile()
        return assoc

    def remove_assign(self,assign):
        '''
        removes an association by it's assign
        Args:
            assign:object type assign
        '''
        return StudAssignRepo.remove_assign(self,assign)
        self._storeToFile()

    def update(self,assoc,upAssoc) :
        '''
        updates an association by a new one by copying the new one's attributes
        Args:
            assoc: object type StudAssign
            upAssoc: object type StudAssign
        '''
        StudAssignRepo.update(self,assoc,upAssoc)
        self._storeToFile()

    def _storeToFile(self):
        '''
        Writes into the file the information in the repository
        '''
        f=open(self._fName,"w")
        assocs=StudAssignRepo.get_all(self)
        for sa in assocs :
            ddl=str(sa.get_deadline().get_day()) + ";" +str(sa.get_deadline().get_month()) + ";"+str(sa.get_deadline().get_year())
            assocf=str(sa.get_stud().get_id()) + ";" + str(sa.get_assign().get_id()) + ";" +ddl + ";" + str(sa.get_grade()) + "\n"
            f.write(assocf)
        f.close()

    def _loadFromFile(self):
        '''
        reads from file and stores that information in the repository
        '''
        try:
            f=open(self._fName,"r")
        except IOError:
            return

        line=f.readline().strip()
        while line != "" :
            t=line.split(";")
            t[0]=int(t[0])
            t[1]=int(t[1])
            s=self.__repoS.fetch_stud(t[0])
            a=self.__repoA.fetch_assign(t[1])
            d=Deadlines(int(t[2]),int(t[3]),int(t[4]))
            assoc=StudAssign(s,a,d,int(t[5]))
            StudAssignRepo.add(self,assoc)
            line=f.readline().strip()
        f.close()
