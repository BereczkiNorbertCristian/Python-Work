'''
Created on Nov 11, 2015

@author: Norbi
'''
from Repository.repoassign import assignment_repository
from Repository.repostudassign import StudAssignRepo
from Repository.repostud import student_repository
from Ctrl.ctrlstud import StudController
from Ctrl.ctrlassign import AssignController
from Ctrl.ctrlstudassign import StudAssignCtrl
from UI.Console import Console
from Ctrl.UndoController import *
from Ctrl.ChangeHistory import *

from FileRepositories.StudentFileRepository import *
from FileRepositories.AssignmentFileRepository import *
from FileRepositories.AssociationFileRepository import *

if __name__ == '__main__':

    undoCtrl=UndoController()
    option=int(input("Choose option 1 if you want in-memory storage for data or choose option 2 if you want file-memory storage:"))
    if option == 2 :
        stud_repo=StudentFileRepository()
        assign_repo=AssignmentFileRepository()
        studassign_repo=AssociationFileRepository(stud_repo,assign_repo)
    else :
        stud_repo=student_repository()
        assign_repo=assignment_repository()
        studassign_repo=StudAssignRepo()


    ctrl_studassign=StudAssignCtrl(studassign_repo,stud_repo,assign_repo,undoCtrl)
    ctrl_stud=StudController(stud_repo,undoCtrl,studassign_repo)
    ctrl_assign=AssignController(assign_repo,undoCtrl,studassign_repo)
    ui=Console(ctrl_stud,ctrl_assign,ctrl_studassign,undoCtrl)

    ui.main_menu()

