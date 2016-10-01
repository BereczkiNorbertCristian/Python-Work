
import re
from Validator.Validator import *

class Console:

    optionComponents=0

    def __init__(self,ctrl):

        self.__ctrl=ctrl


    def add(self):

        self.__ctrl.save_forUndo()
        self.__ctrl.add(self.optionComponents[1].strip("> "))

    def filter(self):

        self.__ctrl.set_filter(self.optionComponents[1].strip("> "))
        self.__ctrl.next()

    def change_status(self):

        self.__ctrl.redoZero()
        self.__ctrl.save_forUndo()
        task=self.__ctrl.get_currentTask()
        task.set_status(self.optionComponents[1].strip("> "))
        self.__ctrl.set_filter(self.optionComponents[1].strip("> "))

    def change_text(self):

        self.__ctrl.redoZero()
        self.__ctrl.save_forUndo()
        task=self.__ctrl.get_currentTask()
        task.set_text(self.optionComponents[1].strip("> "))

    def report(self):

        filtereList=self.__ctrl.get_filteredList()

        for task in filtereList :
            print(task)


    def main(self):


        option = -1
        self.__ctrl.next()
        while option != None :

            task=self.__ctrl.get_currentTask()
            print(task)

            option = input("Introduce your option:")

            try:
                Validator.validate(option)

                self.optionComponents=option.split("<")


                if self.optionComponents[0].strip() == "add":
                    self.add()
                elif option.strip() == "prev":
                    pass
                    self.__ctrl.prev()
                elif option.strip() == "next":
                    self.__ctrl.next()
                elif option.strip() == "exit":
                    exit()
                elif self.optionComponents[0].strip() == "filter" :
                    self.filter()
                elif self.optionComponents[0].strip() == "status" :
                    self.change_status()
                elif self.optionComponents[0].strip() == "text":
                    self.change_text()
                elif option.strip() == "delete":
                    self.__ctrl.save_forUndo()
                    self.__ctrl.delete()
                elif option.strip() == "report" :
                    self.report()
                elif option.strip() == "undo":
                    self.__ctrl.undo()
                elif option.strip() == "redo" :
                    self.__ctrl.redo()



            except TaskException as e:
                print (e)



