def solution(lst):
    answer = []
    for i in range(len(lst)):
        for j in range(i + 1 ,len(lst)):
            k = lst[i] + lst[j]
            if k not in answer:
                answer.append(k)
    answer.sort()
    return answer
print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
