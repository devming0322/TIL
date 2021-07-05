def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else :
        return False

def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print('STACK FULL!')
        return
    top += 1
    stack[top] = data

def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False

def pop() :
    global SIZE, stack, top
    if(isStackEmpty()) :
        print('STACK EMPTY!')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


SIZE = 5
stack = ['커피','녹차','꿀물','콜라',None]
top = 3

print(stack)
push('환타')
print(stack)
push('사이다')


print(stack)
retData = pop()
print('추출데이터 >', retData)
print(stack)
retData = pop()