def selectionSort(ary) :
    n = len(ary)    # 4개
    for i in range (0, n-1) :   # 사이클 (큰 반복 3회)
        minIdx = i
        for k in range(i+1, n) :    # 작은 반복
            if(ary[minIdx] > ary[k]) : 
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return ary


# 전역 변수
import random
dataAry = [random.randint(80, 185) for _ in range(8)]

# 메인
print('정렬 전...', dataAry)

dataAry = selectionSort(dataAry)

print('정렬 후...', dataAry)