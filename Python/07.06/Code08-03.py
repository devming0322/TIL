class TreeNode() :
    def __init__(self) :
        self.left = None
        self.data = None
        self.right = None

# 전역 변수
memory = []
root = None

# DB, 크롤링데이터
nameAry = ['블랙핑크','마마무ㅊ','걸스데이','레드벨벳','트와이스']

# 첫번째 노드
name = nameAry[0]
node = TreeNode()
root = node
node.data = name
memory.append(node)

for name in nameAry[1:] :
    node = TreeNode()
    node.data = name
    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left

        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

    memory.append(node)

# 데이터 검색
findName = '마마무'
current = root
while True :
    if findName == current.data :
        print(findName, '찾음')
        break

    elif findName < current.data :
        if current.left == None :
            print('찾지 못함')
            break
        current = current.left

    else :
        if current.right == None :
            print('찾지 못함')
            break
        current = current.right