# 함수 선언
class Graph() :
    def __init__(self, size) :
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 전역 변수
G1, G3 = None, None

# 메인 
G1 = Graph(4)
