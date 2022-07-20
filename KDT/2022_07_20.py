#1933. 간단한 N의 약수
# divisor=[]
# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         divisor.append(i)
# for i in range(len(divisor)):
#     print(divisor[i],end=' ')

# 2019 더블더블
# a=int(input())
# for i in range(a+1):
# 	print(2**i,end=" ")

# 2050 알파벳을 숫자로 변환
# a=int(input())
# for i in range(a+1):
# 	print(2**i,end=" ")

# 1986 지그재그 숫자
# for test_case in range(1,int(input())+1):
#     n=int(input())
#     answer=0
#     for i in range(1,n+1):
#         if i%2==0:
#             answer-=i
#         else:
#             answer+=i
#     print(f"#{test_case} {answer}")

# 1284 수도 요금 경쟁
for test_case in range(1,int(input())+1):
	P,Q,R,S,W=map(int,(input()).split())

	a_price=P*W

	if W>R:
		b_price=Q+(W-R)*S
	else:
		b_price=Q

	low_price=min(a_price,b_price)

	print(f'#{test_case} {low_price}')