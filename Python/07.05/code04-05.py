# 클래스 또는 함수 선언부
class Node() :
    def __init__(self) :
        self.data = None
        self.link = None

def printNodes(start) : 
    current = start
    print(current.data, end=' ')
    while current.link != None :
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre

    if head.data == findData :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = head
            head = node
            return

    node = Node()
    node.data = insertData
    current.link = node

def deleteNode(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData :
        node = Node()
        node.link = head
        del(current)
        return
    
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return
            
# 전역변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # DB, 크롤링데이터

# import random
# dataArray = [random.randint(1,100) for _ in range(15)]

# 메인 코드
if __name__ == '__main__' : # C, Java, C++ > main() 함수
    
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] :
        pre = node
        node = Node()
        node.data = data    # 정연, 쯔위, ....
        pre.link = node

printNodes(head)

insertNode('민규','화사')
printNodes(head)

insertNode('다현','문별')
printNodes(head)

insertNode('휘인','지효')
printNodes(head)

deleteNode('다현')
printNodes(head)

deleteNode('쯔위')
printNodes(head)

deleteNode('솔라')
printNodes(head)

