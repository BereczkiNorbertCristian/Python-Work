

from FileRepository.fileTasks import taskFile
from Controller.controllerTasks import taskCtrl
from UI.consoleTasks import Console

repo=taskFile()
ctrl=taskCtrl(repo)
console=Console(ctrl)

#console.main()


#________________________________________________________________________________________________

'''
from datetime import datetime

dt1=datetime(1,1,1,hour=4,minute=30)
dt2=datetime(1,1,1,hour=2,minute=40)

dtt=dt1-dt2

print(((dtt.total_seconds())//60)//60)


dtt=datetime.strptime("08:50","%H:%M")



print(dtt.strftime("minute:%M and hour:%H"))

'''

class A:
    def f(selfself,l,nr):
        l.append(nr)

class B:
    def g(self,l,nr):
        nr=nr-1
        l=l+[-2]

a=A()
b=B()
l=[1,2]

c=-1
a.f(l,6)
b.g(l,c)
print(l,c)