

class taskCtrl:

    def __init__(self,repo):

        self.__repo=repo
        self.__filter="active"

    def add(self,text):

        self.__repo.add(text,"active")

    def get_currentTask(self):

        return self.__repo.get_currentTask()

    def next(self):

        self.__repo.next(self.__filter)

    def prev(self):

        self.__repo.prev(self.__filter)

    def set_filter(self,value):

        self.__filter=value

    def delete(self):

        self.__repo.redoZero()
        self.__repo.delete()
        self.next()

    def redoZero(self):

        self.__repo.redoZero()

    def save_forUndo(self):

        self.__repo.save_forUndo()

    def undo(self):

        self.__repo.undo()
        task=self.get_currentTask()
        if task.get_status() != self.__filter :
            self.prev()

    def redo(self):
        self.__repo.redo()
        task=self.get_currentTask()
        if task.get_status() != self.__filter :
            self.next()

    def get_filteredList(self):

        newList=[]
        oldList=self.__repo.get_all()
        for task in oldList:
            if task.get_status() == self.__filter :
                newList.append(task)

        return newList
