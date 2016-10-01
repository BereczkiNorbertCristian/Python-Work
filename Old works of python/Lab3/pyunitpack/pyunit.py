from UI.Console import *
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

import unittest

class TestAll(unittest.TestCase):

    def setUp(self):
        self.undoCtrl=UndoController()
        self.stud_repo=student_repository()
        self.assign_repo=assignment_repository()
        self.studassign_repo=StudAssignRepo()

        self.ctrl_studassign=StudAssignCtrl(self.studassign_repo,self.stud_repo,self.assign_repo,self.undoCtrl)
        self.ctrl_stud=StudController(self.stud_repo,self.undoCtrl,self.studassign_repo)
        self.ctrl_assign=AssignController(self.assign_repo,self.undoCtrl,self.studassign_repo)
        self.ui=Console(self.ctrl_stud,self.ctrl_assign,self.ctrl_studassign,self.undoCtrl)





    def testAll(self):




        self.ctrl_stud.add_stud(Student(1,"peter",1))
        self.ctrl_stud.add_stud(Student(2,"marry",2))
        self.ctrl_stud.add_stud(Student(3,"hansel",3))
        self.ctrl_assign.add_assign(Assignment(1,"6 problems"))
        self.ctrl_assign.add_assign(Assignment(2,"10 exercises"))
        self.ctrl_assign.add_assign(Assignment(3,"9 essays"))
        d=Deadlines(2,2,2)
        grade=9
        self.ctrl_studassign.associate(1,1,d,6)
        self.ctrl_studassign.associate(1,2,d,grade)
        self.ctrl_studassign.associate(1,3,d,grade)
        self.ctrl_studassign.associate(3,2,d,grade)
        self.ctrl_studassign.associate(3,1,d,grade)
        self.ctrl_studassign.associate(2,3,d,grade)
        self.ctrl_studassign.associate(2,1,d,grade)

        # Search by fetches if students really exist
        self.assertEqual(self.ctrl_stud.fetch_stud(1), Student(1,"peter",1))
        self.assertEqual(self.ctrl_assign.fetch_assign(2), Assignment(2,"10 exercises"))
        self.assertEqual(self.ctrl_studassign.fetch_association(1,2) , StudAssign(Student(1,"peter",1),Assignment(2,"10 exercises"),d,9))


        self.assertEqual( len(self.studassign_repo), 7)
        self.undoCtrl.undo()
        self.assertEqual( len(self.studassign_repo), 6)
        self.ctrl_stud.remove_by_id(3)
        self.assertEqual( len (self.studassign_repo) , 4)
        self.assertEqual( len (self.stud_repo) , 2 )
        self.undoCtrl.undo()
        self.assertEqual( len(self.stud_repo) , 3 )
        self.assertEqual( len(self.studassign_repo) , 6 )
        self.undoCtrl.redo()
        self.assertEqual( len(self.studassign_repo) ,4)
        self.assertEqual( len(self.stud_repo) , 2 )



