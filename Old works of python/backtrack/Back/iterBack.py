'''
CONVENTION:
0-Negative
1-Positive
'''

from copy import copy

def solution(lst,signLst,dim):
    '''
    Evaluates the expression with the signs represented by the zeros and ones in the signLst

    :param lst:list type
    :param signLst: list type
    :param dim: int
    :return: -1 if the number of elements is less than the dimension needed
    '''
    sum=lst[0]
    if len(signLst) == dim-1 :
        for i in range (0,dim-1) :
            if signLst[i] == 0 :
                sum-=lst[i+1]
            else :
                sum+=lst[i+1]
    else :
        return -1

    return sum

def iterative(n,lst):
    '''
    Computes the
    :param n:int
    :param lst: list type
    :return: sol -> the number of ways to put + or - between the elements in the list and get the sum of them a positive number
    '''
    signLst=[-1]
    while len(signLst) > 0 :
        consistent=False
        while consistent == False and signLst[-1] < 1 :
            signLst[-1]+=1
            consistent=True
            if len(signLst) > n :
                consistent=False
        if consistent :
            if solution(lst,signLst,n) > 0 :
                yield copy(signLst)
            signLst.append(-1)
        else :
            signLst=signLst[:-1]


def main():
    '''
    Reads and calls the function iterative
    :return:nothing
    '''
    n=int(input("No. of elements:"))
    lst=[]

    for i in range(0,n) :
        lst.append(int(input("Enter number:")))
    solLst=iterative(n,lst)

    print(len(solLst))



#main()


def tests():

    n=3
    lst=[1,-1,1]
    solLst=list(iterative(n,lst))

    TrueSol=[[0,0],[0,1],[1,1]]

    assert len(solLst) == 3
    assert TrueSol == solLst


#tests()

from itertools import repeat
from itertools import compress
from itertools import zip_longest



def fibo():
    i1=0
    yield i1
    i2=1
    yield i2
    while True :
        i3=i2
        i2=i1+i2
        i1=i3
        yield i3


def main22():

    for i,v in enumerate(fibo()):
        if i == 10:
            break
        print(v)

main22()
print("______________________")

for i in repeat(5,5):
    print(i)

str="AEFD"
compLst=[1,0,1,0,1,0]
for i in compress(str,compLst) :
    print( i )

a=zip_longest(str,"xy",fillvalue="-")
for i in a :
    print( i )

































