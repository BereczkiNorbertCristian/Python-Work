
from Repository.repositoryTasks import taskRepo
from Domain.domainTasks import Task


class taskFile(taskRepo):

    _fName="Tasks.txt"

    def __init__(self):

        super().__init__()
        self._loadFromFile()

    def _loadFromFile(self):


        try:
            f=open(self._fName,"r")
        except IOError:
            print("Couldn't open file!!!")

        line=f.readline().strip()
        while line != "" :
            components=line.split(",")
            super().add(components[0],components[1])

            line=f.readline().strip()

        f.close()

    def add(self,comp0,comp1):

        super().add(comp0,comp1)
        self._saveToFile()

    def _saveToFile(self):

        f=open(self._fName,"w")

        allTasks=super().get_all()
        for task in allTasks:
            line=""
            line+=task.get_text()+","+task.get_status()+"\n"
            f.write(line)

        f.close()




