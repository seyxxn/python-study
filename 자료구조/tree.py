# 트리
# 계층적 관계를 표현하는 '비선형' 자료구조

# 트리의 개념
# 1. 트리는 하나의 루트 노드를 갖는다.
# 2. 루트 노드는 0개 이상의 자식 노드를 갖고 있다.
# 3. 그 자식 노드 또한 0개 이상의 자식 노드를 갖고 있고, 이는 반복적으로 정의된다.

# 일상생활에서의 트리
# 비선형 자료구조로 계층적 관계를 표현함
# ex) 디렉토리 구조, 조직도

# 트리 용어
# 루트 노드 : 부모가 없는 노드, 트리는 하나의 루트 노드만을 가진다.
# 단말 노드 : 자식이 없는 노드, '말단 노드' 또는 '잎 노드'라고도 부른다.
# 내부 노드 : 단말 노드가 아닌 노드
# 간선 : 노드를 연결하는 선
# 형제 : 같은 부모를 가지는 노드
# 노드의 크기 : 자신을 포함한 모든 자손 노드의 개수
# 트리의 높이 : 한 노드와 단말노드 사이의 최대 깊이 (무조건하나, 정해져있음, 공통적)
# 노드의 깊이 : 루트에서 어떤 노드에 도달하기 위해 거쳐야하는 간선의 개수 (노드에 따라 다름)
# 노드의 레벨 : 트리의 특정 깊이를 가지는 노드의 집합(depth가 같은 노드의 집합)
# 노드의 차수 : 하위 트리 개수 / 간선 수 = 각 노드가 지닌 가지의 수
# 트리의 차수 : 트리의 최대 차수
# 서브 트리 
# path(경로) : 한 노드(부모)에서 다른 노드(자식)에 이르는 노드들의 순서


# 1. 딕셔너리 사용
# tree = {}
# tree[1] = [2,3]
# tree[2] = [4,5]
# tree[3] = [6,7]
# tree[4] = [8]
# print(tree[1])

# 2. 트리 클래스 사용
# 이진 트리 사용
# 노드가 최대 두개의 자식노드 left, right를 갖춘 tree 자료구조

from pickle import BININT2


class NodeBT :
    def __init__(self, value = None):
        self.value = value
        self.left = None # left subtree
        self.right = None # right subtree
    def __repr__(self) :
        return f'{self.value}'

bt1 = NodeBT(1)
bt2 = NodeBT(2)
bt3 = NodeBT(3)
bt4 = NodeBT(4)
bt5 = NodeBT(5)
bt6 = NodeBT(6)

bt1.left = bt2
bt1.right = bt3
bt2.left = bt4
bt2.right = bt5
bt3.left = bt6

print(bt1)
print(bt1.left)
print(bt1.left.right)