# 이 문제는 서로 연결된 부분이 부모 노드 와 자식 노드 간의 차이(즉, 깊이 차이가 몇인지)를 물어 보는 것이다.
import sys

input = sys.stdin.readline


def DFS(start):
    # 방문 처리
    visit[start] = True
    # start 부모 노드에서 갈수 있는 자식노드들 나열
    for i in graph[start]:
        # 방문하지 않았던 자식노드라면
        if not visit[i]:
            # 부모노드에서 갈수 있는 자식노드들의 깊이 차이를 위해 answer[i] 의 자식 노드 answer[start] 부모노드에 + 1 해준다.
            answer[i] = answer[start] + 1
            DFS(i)

n = int(input())
p1, p2 = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
# p1 스타트 지점에서 들릴수 있는 곳 중에서 p1 와 깊이 차이를 나타내줄 리스트
answer = [0] * (n + 1)

# 인접 리스트 만들기
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 스타트 지점
DFS(p1)
# 도착 지점에 p1 와 연결 된 부분 있는지 없는지 파악
if answer[p2]:
    print(answer[p2])
else:
    print(-1)