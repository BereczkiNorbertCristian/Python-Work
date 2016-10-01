from copy import deepcopy

def evaluate(lst,backList):
    '''
    Evaluates the sum
    :param lst:list type
    :param backList: list type
    :return: int -> the sum of the elements in the list lst based on the signs from backList
    '''
    sum=lst[0]
    for i in range(1,len(lst)):
        if backList[i-1] == 0:
            sum-=lst[i]
        else :
            sum+=lst[i]
    return sum

def back(i,lst,backList,solLst):
    '''
    :param i: int
    :param lst: list type
    :param backList: list type
    :param sol: int
    :return:
    '''
    if i < len(lst)-1 :
        backList[i]=0
        back(i+1,lst,backList,solLst)
        backList[i]=1
        back(i+1,lst,backList,solLst)
    else :
        evaluatedSum=evaluate(lst,backList)
        if evaluatedSum > 0 :
            solLst.append(deepcopy(backList))


def main():
    '''
    reads and writes and calls the function back to compute all the posibilities
    :return:
    '''
    n=int(input("How many numbers do you want to insert? n= "))
    lst=[]
    while n > 0 :
        lst.append(int(input("Introduce new number:")))
        n-=1

    backList=[0,0,0,0,0,0,0,0,0,0]
    saveLst=[]
    back(0,lst,backList,saveLst)

    print(len(saveLst))

#main()

def tests():

    n=3
    lst=[1,-1,1]
    backList=[0,0,0,0,0,0,0,0,0,0]
    testLst=[[0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0]]
    savLst=[]
    back(0,lst,backList,savLst)
    assert len(testLst) == len(savLst)
    assert testLst == savLst

tests()



