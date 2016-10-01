
from Domain.domainTasks import Task
from copy import deepcopy


class taskRepo:


    def __init__(self):

        self.__data=[]
        self.__idCounter=0
        self.__currentIndex=0
        self.__undoStack=[]
        self.__redoStack=[]


    def get_idCounter(self):

        return self.__idCounter

    def inc_idCounter(self):

        self.__idCounter+=1

    def add(self,comp0,comp1):

        self.redoZero()
        self.__idCounter+=1
        self.__data.append(Task(self.__idCounter,comp0,comp1))

    def get_all(self):

        return self.__data

    def get_currentTask(self):

        return self.__data[self.__currentIndex]

    def save_forUndo(self):

        self.__undoStack.append(deepcopy(self.__data))


    def next(self,filter):

        length=len(self.__data)
        for i in range(1,length+1) :
            if self.__data[(self.__currentIndex+i)%length].get_status() == filter:
                self.__currentIndex=(self.__currentIndex+i)%length
                break

    def redoZero(self):

        self.__redoStack=[]

    def undo(self):

        if len(self.__undoStack) > 0 :
            self.__redoStack.append(deepcopy(self.__data))

            self.__data=self.__undoStack.pop()
        else :
            print("There isn't possible to do any more undo's!!!!")

    def redo(self):

        if len(self.__redoStack) > 0:
            self.__undoStack.append(deepcopy(self.__data))
            self.__data=self.__redoStack.pop()

        else :
            print("You cannot redo any more!!!")

    def prev(self,filter):

        length=len(self.__data)
        for i in range(1,length+1) :

            if self.__data[(self.__currentIndex-i)%length].get_status() == filter:
                self.__currentIndex=(self.__currentIndex-i)%length
                break

    def delete(self):

        self.__undoStack.append(deepcopy(self.__data))
        self.__data.pop(self.__currentIndex)





