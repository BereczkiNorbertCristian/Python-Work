
class gradeDTO :

    def __init__(self,student,avgGrade):
        '''
        constructor for DTO grade
        Args:
            student: object type student
            avgGrade: int
        Returns:

        '''
        self.__stud=student
        self.__avgGrade=avgGrade

    def get_stud(self):
        '''
        getter for student
        Returns:object type student
        '''
        return self.__stud

    def get_avgGrade(self):
        '''
        getter for average Grade
        Returns:int avgGrade
        '''
        return self.__avgGrade





















