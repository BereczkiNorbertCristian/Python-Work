
from copy import deepcopy

startPos = 0
runLength = 1

def compute_minrun(n):

    # computes the minrun

    r=0
    while n >= 64 :
        r|=n & 1
        n=n>>1

    return n+r

def overlord_timsort(mlst,cmp_funct):

    copyLst=deepcopy(mlst)
    mergeStates=[]
    minrun=compute_minrun(len(copyLst))
    if len(copyLst) <= 64 :
        run=compute_next_run(copyLst,0,cmp_funct)
        binary_insertion(copyLst,cmp_funct,0,run,len(copyLst))
        return copyLst
    else :
        iterNo=0
        while iterNo < len(copyLst) :

            nextRun=compute_next_run(copyLst,iterNo,cmp_funct)
            #print(nextRun)
            #print(mergeStates)

            if nextRun < minrun:
                binary_insertion(copyLst,cmp_funct,iterNo,iterNo+nextRun,iterNo+minrun+1)
                nextRun=minrun

            #print(copyLst)

            if iterNo + nextRun >len(copyLst) :
                nextRun=len(copyLst)-iterNo

            mergeStates.append((iterNo,nextRun))
            decide_merge_pattern(copyLst,mergeStates,cmp_funct)
            iterNo=iterNo + nextRun

        merge_collapse(copyLst,mergeStates,cmp_funct)
        return copyLst


def merge_collapse(lst,statesStack,cmp_funct):


    while len(statesStack) > 1 :
        print("GOT INTO MERGE COLLAPSE")
        merge_process(lst,statesStack,cmp_funct)



def decide_merge_pattern(lst,statesStack,cmp_funct):

    #statesStack[-1]-top of the stack
    #statesStack[-2]-the elmenet beneath the top of the stack
    #statesStack[-3]-...

    global runLength
    global startPos

    performedMerge=True
    while len(statesStack) > 2 and performedMerge == True :

        performedMerge=False

        if statesStack[-3][runLength] <= statesStack[-2][runLength] + statesStack[-1][runLength] or statesStack[-2][runLength] <= statesStack[-1][runLength] :

            performedMerge=True

            if statesStack[-3][runLength] < statesStack[-1][runLength] :
                #merge left
                c=statesStack.pop()
                merge_process(lst,statesStack,cmp_funct)
                statesStack.append(c)

            else :
                #merge right
                newState=merge_process(lst,statesStack,cmp_funct)
                statesStack.append(newState)

    if len(statesStack) == 2 :

        newState=merge_process(lst,statesStack,cmp_funct)
        statesStack.append(newState)

minGallop=7


def merge_process(lst,statesStack,cmp_funct):

    global runLength
    global startPos


    B=statesStack.pop()
    A=statesStack.pop()
    '''
    print(lst[A[startPos]])
    print(lst[A[startPos]+1])
    print(lst[B[startPos]])
    print(lst[B[startPos]+1])
    '''
    iA=0
    iB=0

    winA=0
    winB=0

    tempArray=[]

    while iA+iB<A[runLength]+B[runLength]  :

        if winA >= minGallop or winB >=minGallop :
            while (winA >=minGallop or winB >= minGallop) and A[startPos]+iA < len(lst) and (B[startPos]+iB) < len(lst) :

                winA=gallop(lst,A[startPos]+iA,A[runLength],lst[B[startPos]+iB],cmp_funct)
                winB=gallop(lst,B[startPos]+iB,B[runLength],lst[A[startPos]+iA],cmp_funct)

                print("winA:{0} winB:{1}".format(winA,winB))

                if winA >= winB :
                    winB=0
                else:
                    winA=0

                for j in range (0,winA):
                    tempArray.append(lst[A[startPos]+iA])
                    iA+=1

                for j in range (0,winB):
                    tempArray.append(lst[B[startPos]+iB])
                    iB+=1
            if A[startPos]+iA >= len(lst) or (B[startPos]+iB) >= len(lst):
                break
        else :

            if iA<A[runLength] and ( iB>=B[runLength] or cmp_funct(lst[A[startPos]+iA],lst[B[startPos]+iB])==True ) :
                winA+=1
                winB=0
                tempArray.append(lst[A[startPos]+iA])
                iA+=1
            else :
                winA=0
                winB+=1
                tempArray.append(lst[B[startPos]+iB])
                iB+=1
                #minGallop+=1
    for i in range (0,A[runLength]+B[runLength]) :

        if i >= len(lst) or i >= len(tempArray):
            break

        lst[i]=tempArray[i]

    return (A[startPos],A[runLength]+B[runLength])



def gallop(lst,startPosition,length,element,cmp_funct) :

    j=0
    beg=0
    end=0
    while (j<<1) +1 < length and startPosition+(j<<1)+1 < len(lst) :
        if cmp_funct( lst[startPosition+j],element)==True and cmp_funct(element,lst[startPosition+(j<<1)+1]):
            if j>=0 :
                beg=j+startPosition
                end=(j<<1) + 1 +startPosition
                break

        else :
            j=(j<<1)+1
    while beg < end and beg > 0 and end > 0 :

        mid = (beg+end) // 2
        if cmp_funct(lst[mid-1],element) and cmp_funct(element,lst[mid]) :

            return mid-startPosition
        elif cmp_funct(lst[mid-1],element) == True :
            end = mid - 1
        elif cmp_funct(element,lst[mid+1]) == True :
            beg = mid + 1
        else :
            break
    return 0


def binary_insertion(lst,cmp_funct,trueStart,iterStart,iterEnd):

    for i in range(iterStart,iterEnd):
        if i >= len(lst) :
            break
        element=lst[i]
        left=trueStart
        right=i-1

        while left <= right :
            mid=(left+right)//2
            if cmp_funct(element,lst[mid]) == True :
                for j in range (right+1,mid ,-1) :
                    lst[j]=lst[j-1]
                lst[mid]=element
                right=mid-1
            else :
                left=mid+1







def compute_next_run(lst,iterStart,cmp_funct):

    iterNo=iterStart + 2
    c1=cmp_funct(lst[iterNo-1],lst[iterNo])
    c2=cmp_funct(lst[iterNo-2],lst[iterNo-1])
    needsReverse=False

    while iterNo < len(lst) and ((c1==True and c2==True) or (c1==False and c2==False)) :
        if c1 ==False :
            needsReverse=True
        iterNo+=1
        if iterNo >= len(lst) :
            break
        c1=cmp_funct(lst[iterNo-1],lst[iterNo])
        c2=cmp_funct(lst[iterNo-2],lst[iterNo-1])

    if  iterNo-iterStart == 2 and cmp_funct(lst[iterNo-2],lst[iterNo-1])== False:
        needsReverse=True

    if needsReverse == True :
        for i in range(0,(iterNo-iterStart)//2):
            lst[i+iterStart],lst[iterNo-1-i] = lst[iterNo-1-i] , lst[i+iterStart]



    return iterNo - iterStart


def is_greater(a,b):
    if a <= b :
        return True
    return False
#test compute_next_run()
'''
testList=[2,1,3,4,3]
print(compute_next_run(testList,0,is_greater))
print(testList)
'''
#test binary_insertion
'''
testList=[1,2,3,4,3,8,5,99,33,44,88,55]
n=len(testList)
newLst=overlord_timsort(testList,is_greater)
#binary_insertion(testList,is_greater,0,4,n)
print(newLst)
'''
import random
testList=[]
#testList.append(2)
#testList.append(4)
for i in range (0,600):
    testList.append(random.randint(1,50000))
print(testList)


#testList=[30335, 44956, 7027, 17303, 37125, 34636, 8408, 34374, 31772, 5724, 41931, 28616, 22239, 18651, 29757, 22070, 40467, 16559, 24742, 12249, 36082, 49026, 8839, 33071, 29291, 28827, 30530, 14673, 30969, 15969, 39191, 26139, 48970, 28844, 33076, 6196, 27878, 1201, 47886, 43341, 2408, 13433, 42515, 5247, 9022, 17545, 24743, 435, 14694, 15882, 15865, 47394, 31466, 22661, 19170, 45115, 16695, 48042, 23679, 9242, 1200, 34017, 34694, 10153, 48095, 20527, 18700, 12257, 12819, 2935, 5225, 40200, 28559, 2832, 18115, 37209, 21769, 9977, 5016, 31785, 21829, 11494, 49460, 38427, 46583, 11445, 2180, 38675, 2182, 35584, 41265, 27050, 4573, 40813, 15170, 23269, 17246, 845, 22296, 47208, 17029, 46218, 11769, 27043, 6238, 41403, 29324, 16473, 16722, 22942, 15715, 47271, 24705, 23143, 6052, 43145, 1072, 44999, 21417, 18482, 39186, 47709, 20213, 8465, 22508, 6887, 846, 24975, 18210, 37589, 39660, 45903, 36945, 38313, 30051, 7969, 31975, 10977, 820, 6916, 41260, 31756, 798, 33666, 36206, 15879, 42434, 37673, 6377, 21435, 13103, 5884, 33799, 4195, 723, 8724, 29803, 10266, 19047, 1466, 47317, 45884, 43421, 16226, 13748, 45477, 12055, 38768, 3902, 42831, 34087, 5963, 16090, 366, 15343, 46280, 219, 14757, 7888, 14870, 29611, 23936, 11878, 19244, 11982, 29172, 36524, 37849, 44412, 39497, 3689, 28305, 7281, 40656, 11555, 31046, 11890, 18735, 27731, 11626]
testedLst2=sorted(deepcopy(testList))

print("______________________")
print("PYTHON SORT:")
print(testedLst2)

print("MY TIMSORT:")
testedLst=overlord_timsort(testList,is_greater)
print(testedLst)
notpoint=[]
for i in range(0,600):
    notpoint.append(0)
for i in range (0,600):
    if not testedLst[i]==testedLst2[i]:
        notpoint[i]=i


print(notpoint)

assert testedLst == testedLst2