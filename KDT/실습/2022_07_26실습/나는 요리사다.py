rank = [sum(list(map(int, input().split()))) for _ in range(5)]
print(rank.index(max(rank)) + 1,max(rank))