


class Pything:

    def __init__(self,studId,valoare):

        self.__id=studId
        self.__valoare=valoare

    def get_id(self):

        return self.__id

    def __repr__(self):

        return "ID:{0}  VALOARE:{1}".format(self.__id,self.__valoare)

from random import randint

lst=[]
for i in range (0,33):

    pp=Pything(randint(0,1000),randint(0,500))
    lst.append(pp)

x=[1,2,34,55,102]

x+=[y for y in lst if y.get_id()%2 == 0]


print(x)


def f():
    return 1
def g(x=1):
    return x + 1
def h(x=1, y=2):
    return x + y
l = [f, g, h]
for e in l:
    print(e())
h = lambda x = 1, y = 2: x * y
print(l[2](3), h(), h(3), h(x=3), h(y=3))
print(h([2, 3]))
print(h(*[2, 3]))


print("{0}{1}{2}".format(1,2,3))

