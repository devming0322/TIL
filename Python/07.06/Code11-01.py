def findMinIdx(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if (ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx

testAry = [55, 33, 77, 99]
minPos = findMinIdx(testAry)
print('MIN..', testAry[minPos])