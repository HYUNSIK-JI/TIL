# swea 0번
# for test_case in range(1,int(input())+1):
# 	a,b=map(int,input().split())
# 	i,j=divmod(a,b)
# 	print(f"#{test_case} {i} {j}")
#
# swea 1번
# for i in range(int(input()),-1,-1):
#     print(i,end=' ')
#
# swea 2번
# for test_case in range(1,int(input())+1):
#     n_list=list(map(int,input().split()))
#     print(f"#{test_case} {round(sum(n_list)/len(n_list))}")
#
# swea 3번
# for test_case in range (1,int(input())+1):
#     a,b=map(int,input().split())
#     if a>b:
#         print(f'#{test_case} {">"}')
#     elif a==b:
#         print(f'#{test_case} {"="}')
#     else:
#         print(f'#{test_case} {"<"}')
#
# 문제 20. 각 자릿수의 합 구하기
# n=int(input())
# answer=0
# for i in str(n):
#     answer+=int(i)
# print(answer)
#
# 문제 21.숫자 뒤집기
# n=int(input())
# answer=0
#
# while n>0:
#     k=n%10
#     answer=(answer*10)+k
#     n//=10
# print(answer)