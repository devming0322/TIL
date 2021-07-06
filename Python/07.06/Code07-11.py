# 함수 선언
def isQueueFull() :
	global SIZE, queue, front, rear
	if ( (rear + 1) % SIZE == front) :
		return True
	else :
		return False

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

def enQueue(data) :
	global SIZE, queue, front, rear
	if (isQueueFull()) :
		print('QUEUE FULL !')
		return
	rear = (rear + 1) % SIZE
	queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print('QUEUE EMPTY !')
		return None
	front = (front + 1) % SIZE
	data = queue[front]
	queue[front] = None
	return data

# 전역 변수
SIZE = 7
queue = [ None for _ in range(SIZE)]
front=rear=0

# 메인