

class Lab:

    def __init__(self,studentId,labNumber,problemNumber):
        '''
        fields:
        :param studentId:int
        :param labNumber:int
        :param problemNumber:string
        :return:
        '''
        self.__studId=studentId
        self.__lNr=labNumber
        self.__pNr=problemNumber

    def get_studId(self):
        '''
        getter for student id
        :return: int
        '''
        return self.__studId

    def get_labNr(self):
        '''
        getter for lab number
        :return: int
        '''
        return self.__lNr

    def get_problemNr(self):
        '''
        getter for problem number
        :return: int
        '''
        return self.__pNr

    def __eq__(self, other):
        '''
        verifies equality
        :param other:
        :return: true if equl false otherwise
        '''
        return self.__lNr == other.get_labNr() and self.__studId == other.get_studId()



    def __repr__(self):
        '''
        formater
        :return:
        '''
        return "LAB:    StudentId:{0}   Lab Number:{1}  Problem Number{2}".format(self.__studId,self.__lNr,self.__pNr)



