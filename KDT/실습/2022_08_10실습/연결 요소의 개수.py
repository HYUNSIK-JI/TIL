# 이 문제는 서로 연결 되지 않는 숫자가 몇 인지 파악해야하는 문제이다.
# 즉 1 ~ n + 1 까지 한번씩 돌려서 서로 연결 되지 않는 부분을 찾는 것이다.
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

def DFS(start):
    visit[start] = True
    for i in graph[start]:
        if not visit[i]:
            DFS(i)
n, m = map(int, input().split())
# 인접 리스트를 위한 리스트 선언
graph = [[] for _ in range(n + 1)]
# 방문 리스트
visit = [False] * (n + 1)
# 연결 되지 않는 곳이 몇개 인지 파악을 위한 cnt 변수
cnt = 0

#인접 리스트 만들기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if not visit[i]:
        # 서로 연결 되지 않는 부분이였기 때문에 cnt + 1 해준다.
        cnt += 1
        DFS(i)
print(cnt)