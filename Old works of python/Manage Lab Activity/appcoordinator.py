

from repos.labRepo import LabRepo
from repos.studentRepo import StudentRepo
from controllers.controller import Controller
from ui.ui import Console


studRepo=StudentRepo()
labRepo=LabRepo()
ctrl=Controller(labRepo,studRepo)
consl=Console(ctrl)

consl.run()

