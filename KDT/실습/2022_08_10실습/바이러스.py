import sys
input = sys.stdin.readline

def dfs(start):
    global cnt
    visit[start] = True

    # 1번 컴퓨터에 연결된 모든 컴퓨터 번호들을 i에 대입
    for i in graph[start]:
        # 그 곳이 방문되지 않은 곳이라면
        if not visit[i]:
            # 감염된 컴퓨터 + 1
            cnt += 1
            # 감염된 컴퓨터와 연결 된 곳 찾기.
            dfs(i)
    return cnt
com = int(input())

graph = [[] for _ in range(com + 1)]
visit = [False] * (com + 1)

# 무방향 인접 리스트 만들기
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 바이러스에 감염 된 컴퓨터 갯수 파악
cnt = 0
print(dfs(1))