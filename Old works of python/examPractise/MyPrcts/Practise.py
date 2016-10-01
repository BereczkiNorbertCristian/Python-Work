
import re


global_var="World"
print("What I say: %s"%global_var ,"Because it's interesting")
print("Hello from practise!")

def ff(cl):


    local_var=300
    #global_var=200
    print(local_var)
    #print(global_var)

    print (locals())
    print(globals())
    cl=[2,3]
    print(id(cl))


ff(global_var)
print(id(global_var))

print(global_var)
print(id(global_var))

#_____________________________________________________________________________________________

lst=list(range(2,19))
print(lst)

#lst= global_var,33,'mov'

newLst=[x for x in lst if x>10]
print(newLst)



class myCls:

    nrInst=0
    def __init__(self,a):

        self.__mm=a
        myCls.nrInst+=1


obj1=myCls(1)
obj2=myCls(2)

print(obj1.nrInst)




#============================================================================================================================

import re

line="08:30"

correctLine=r"(..):(..)"



if re.match(correctLine,line) :
    match=re.match(correctLine, line)

    print("Line is correct!!!")

    print("First group:%s" % match.group(1))
    print("Second group:%s" % match.group(2))
    try:
        nr1=int(match.group(1))
        nr2=int(match.group(2))
        print(nr1+nr2)
    except ValueError :
        print("There are letters in the line you introduced!")



else :
    print("Line is not correct!!!")




import datetime

dt1=datetime.time(hour=4,minute=3,second=5)
dt2=datetime.time(hour=3,minute=9,second=8)


print(dt1)
dt1=datetime.time.strptime("03,04","%H,%M")
print(dt1)
#print(dt1-dt2)

print(dt2.minute)





