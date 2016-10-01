

import unittest

from FileRepository.fileTasks import *
from Controller.controllerTasks import *
from UI.consoleTasks import *
from Validator.Validator import *


class TestALL(unittest.TestCase):

    def setUp(self):

        unittest.TestCase.setUp(self)
        self.repo=taskFile()
        self.ctrl=taskCtrl(self.repo)


    def testValidator(self):

        assert (len(self.repo.get_all())>0)

        option="filter<don>"
        try :
            Validator.validate(option)
            assert False
        except TaskException :
            assert True
        try:
            option="next"
            Validator.validate(option)
            assert True
        except TaskException:
            assert False
        try:
            option="status nothing>"
            Validator.validate(option)
            assert False
        except TaskException:
            assert True

    def testRemoveTaskAndUndo(self):
        ol=len(self.repo.get_all())
        print(ol)
        self.ctrl.delete()
        self.assertEqual(ol-1,len(self.repo.get_all()))
        print(len(self.repo.get_all()))
        self.ctrl.undo()
        print(len(self.repo.get_all()))
        self.assertEqual(ol,len(self.repo.get_all()))


