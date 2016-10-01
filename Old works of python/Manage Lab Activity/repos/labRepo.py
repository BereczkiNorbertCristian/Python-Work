
from validation.validation import TeacherException

class LabRepo:

    _fName="labs.txt"

    def __init__(self):

        self.__data=[]


    def add(self,lab):
        '''
        adds a lab to the repo
        :param lab: object type Lab
        :return:
        exception:raises techerException if object foun already in repo
        '''
        if lab in self.__data :
            raise TeacherException("A student cannot have 2 problems at the same lab!!!")
        else :
            self.__data.append(lab)

    def get_all(self):
        '''
        returns a list of the labs
        :return:
        '''
        return self.__data


    def save(self):
        '''
        saves to a file the repo of the labs
        :return:
        '''
        f=open(self._fName,"w")

        for lab in self.__data:

            writeString=""
            writeString+="{0},{1},{2}\n".format(lab.get_studId(),lab.get_labNr(),lab.get_problemNr())
            f.write(writeString)

        f.close()

