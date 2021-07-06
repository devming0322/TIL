# 함수 선언
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear != SIZE-1) :
        return False
    elif (rear == SIZE -1) and (front == -1) :
        return True
    else :
        for i in range(front+1, SIZE) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

def enQueue(data) : 
    global SIZE, queue, front, rear
    if(isQueueFull()) :
        print('QUEUE FULL !')
        return
    rear +=1
    queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print('QUERE EMPTY !')
		return None
	front += 1
	data = queue[front]
	queue[front] = None
	return data


# 전역 변수
SIZE = 7
queue = [ None for _ in range(SIZE)]
front=rear=1

# 메인
# queue = ['화사','솔라','문별','휘인','선미']
# front = -1
# rear = 4

# print('큐 꽉?',isQueueFull())
# print('큐 빔?',isQueueEmpty())

print(queue)
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
print(queue)

retData = deQueue()
print('추출..>',retData)
print(retData)