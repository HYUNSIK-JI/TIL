from math import gcd

def solution(arr):
	answer=arr[0]

	for num in arr:
		answer=answer*num//gcd(answer,num)
	return answer
numbers=list(map(int,input().split()))
print(solution(numbers))