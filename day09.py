class Graph:
	def __init__(self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g) :
    print(' ', end=' ')
    for v in range(g.SIZE) :
        print(name_ary[v], end=' ')
    print()
    for row in range(g.SIZE) :
        print(name_ary[row], end=' ')
        for col in range(g.SIZE) :
            print(f"{g.graph[row][col]:2}", end=' ')
        print()
    print()

from collections import deque


def bfs(g, queue, visited, find_vtx):
    if not queue:
        return False

    current = queue.pop(0)  # 큐에서 첫 번째 요소를 꺼냄
    if current == find_vtx:  # 찾고자 하는 정점이라면 종료
        return True

    visited.add(current)  # 방문한 노드 기록

    # 인접 노드를 찾아서 방문하지 않았다면 큐에 추가
    for vertex in range(g.SIZE):
        if g.graph[current][vertex] != 0 and vertex not in visited and vertex not in queue:
            queue.append(vertex)

    return bfs(g, queue, visited, find_vtx)  # 재귀 호출


def find_vertex_bfs(g, find_vtx):
    return bfs(g, [0], set(), find_vtx)


def dfs(g, current, find_vtx, visited):
    visited.append(current)
    if current == find_vtx:
        return True
    for vertex in range(g.SIZE):
        if g.graph[current][vertex] != 0 and vertex not in visited:
            if dfs(g, vertex, find_vtx, visited):
                return True
    return False


def find_vertex(g, find_vtx):
    visited = []
    return dfs(g, 0, find_vtx, visited)


G1 = None
name_ary = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

g_size = 6
G1 = Graph(g_size)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print_graph(G1)

# 간선 목록 만들기 [가중치, 시작도시, 도착도시]
edge_ary = []
for i in range(g_size) :
	for k in range(g_size) :
		if G1.graph[i][k] != 0 :
			edge_ary.append([G1.graph[i][k], i, k])

print(edge_ary, len(edge_ary))

# 가중치 순으로 목록 정렬 (내림차순)
# from operator import itemgetter
# edge_ary = sorted(edge_ary, key = itemgetter(0), reverse = True)
edge_ary.sort(reverse=True)

print(edge_ary, len(edge_ary))

# 중복 간선 제거
new_ary = []
for i in range(0, len(edge_ary), 2) :
	new_ary.append(edge_ary[i])

print(new_ary, len(new_ary))

index = 0
while len(new_ary) > g_size - 1:	# 간선의 개수가 '정점 개수-1'일 때까지 반복
    start = new_ary[index][1]
    end = new_ary[index][2]
    save_cost = new_ary[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = find_vertex_bfs(G1, start)
    endYN = find_vertex_bfs(G1, end)

    if startYN and endYN :
        del new_ary[index]
    else:
        G1.graph[start][end] = save_cost
        G1.graph[end][start] = save_cost
        index += 1

print_graph(G1)
# 기존 DFS 탐색과 함께 BFS 탐색 결과도 확인
print("DFS 탐색 결과:", find_vertex(G1, 부산))
print("BFS 탐색 결과:", find_vertex_bfs(G1, 부산))