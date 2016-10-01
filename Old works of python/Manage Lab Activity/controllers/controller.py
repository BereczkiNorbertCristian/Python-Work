
from validation.validation import TeacherException

class Controller:

    def __init__(self,labRepo,studRepo):

        self.__labRepo=labRepo
        self.__studRepo=studRepo


    def get_all(self):


        return self.__studRepo.get_all()

    def add(self,lab):

        self.__labRepo.add(lab)

    def get_allLabs(self):

        return self.__labRepo.get_all()


    def save(self):

        self.__labRepo.save()

    def oneStud_allLabs(self,studId):
        '''
        for one student 
        :param studId:
        :return:
        '''
        labs=self.__labRepo.get_all()
        safeLabs=[]
        for lab in labs:

            if lab.get_studId() == studId :
                safeLabs.append(lab)

        if len(safeLabs)>0:
            return safeLabs
        raise TeacherException("The student doesn's have any labs assigned!!!")


    def allStud_oneLab(self,labNr):
        '''
        returns a list of students for which ...
        :param labNr: int
        :return:
        '''
        labs=self.__labRepo.get_all()
        students=self.__studRepo.get_all()
        safeStudents=[]

        for lab in labs:
            if lab.get_labNr() == labNr:
                for student in students:
                    if student.get_id()==lab.get_studId() :
                        safeStudents.append(student)

        return safeStudents






