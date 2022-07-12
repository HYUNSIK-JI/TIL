import sys

# #6001 출력하기
# print("Hello")#출력
#
# #6002 출력하기
# print("Hello World")#출력
#
# #6003 출력하기
# print("Hello")
# print("World")
#
# #6004 출력하기
# print("'Hello'")
#
# #6005 출력하기
# print('"Hello World"')
#
# #6006 출력하기
# print('\"!@#$%^&*()\'')
#
# #6007 출력하기
# print("\"C:\Download\\\'hello\'.py\"")
#
# #6008 출력하기
# print('print("Hello\\nWorld")')
#
# #6009 출력하기
# print(input())
#
# #6010 [기초-입출력] 정수 1개 입력받아 int로 변환하여 출력하기(설명)(py)

# print(int(sys.stdin.readline()))
# #6011 : [기초-입출력] 실수 1개 입력받아 변환하여 출력하기(설명)(py)

# print(float(sys.stdin.readline()))

# #6012 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기1(설명)(py)

# print(int(sys.stdin.readline()))
# print(int(sys.stdin.readline()))


# #6013 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기1(py)
# a=input()
# b=input()
# print(b)
# print(a)
#
# #6014 : [기초-입출력] 실수 1개 입력받아 3번 출력하기(py)


# k=float(sys.stdin.readline())
# for _ in range(3):
#     print(k)
# #6015 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기2(설명)(py)

#
# n_list=list(map(int,sys.stdin.readline().split()))
# for i in n_list:
#     print(i)
# #6016 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기2(설명)(py)
# a,b=input().split()
# print(b,a)
#
# #6017 : [기초-입출력] 문장 1개 입력받아 3번 출력하기(설명)(py)


# s=sys.stdin.readline().rstrip()
# print(s,s,s)

# # 6018 : [기초-입출력] 시간 입력받아 그대로 출력하기(설명)(py)
# a, b = input().split(':')
# print(a, b, sep=':')
#
# # 6019 : [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기(py)
# y, m, d = input().split('.')
# print(d,m,y,sep="-")
#
# # 6020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기(py)

#
# number=sys.stdin.readline().split("-")
# for i in number:
#     print(i,end="")
#
# # 6021 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기(설명)(py)

# s=sys.stdin.readline().rstrip()
# for i in s:
#     print(i)
#
# # 6022 : [기초-입출력] 연월일 입력받아 나누어 출력하기(설명)(py)

#
# a=sys.stdin.readline().rstrip()
# for i in range(0,6,2):
#     print(a[i:i+2],end=" ")
#
# # 6023 : [기초-입출력] 시분초 입력받아 분만 출력하기(py)

#
# s=sys.stdin.readline().rstrip().split(":")
# print(s[1])
#
# # 6024 : [기초-입출력] 단어 2개 입력받아 이어 붙이기(설명)(py) 해결

#
# a,b=sys.stdin.readline().split()
# print(a+b)
# # 6025:

#
# a,b=map(int,sys.stdin.readline().split())
#
# print(a+b)
#
# # 6026 : [기초-값변환] 실수 2개 입력받아 합 계산하기(설명)(py)
# answer=0
# for _ in range(2):
#     answer+=float(input())
# print(answer)
#
# # 6027: [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1(설명)(py)
# a = int(input())
# print('%x'%a)
#
# # 6028:[기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2(설명)
# n=int(input())
# print("%X" %n)
#
# #6029 : [기초-값변환] 16진 정수 입력받아 8진수로 출력하기(설명)(py)
# a = input()
# n = int(a, 16)
# print('%o' % n)
#
# #6030:[기초-값변환] 영문자 1개 입력받아 10진수로 변환하기(설명)(py)
# print(ord(input()))
#
# #6031 : [기초-값변환] 정수 입력받아 유니코드 문자로 변환하기(설명)(py)
# print(chr(int(input())))
#
# # 6032 : [기초-산술연산] 정수 1개 입력받아 부호 바꾸기(설명)(py)
# print(-int(input()))
#
# # 6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기(설명)(py)
# print(chr(ord(input())+1))
#
# # 6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기(설명)(py)
# a,b=map(int,input().split())
# print(a-b)
#
# # 6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기(설명)(py)
# a,b=map(float,input().split())
# print(a*b)
#
# # 6036 : [기초-산술연산] 단어 여러 번 출력하기(설명)(py) 해결
# word,n = input().split()
# print(word*int(n))
#
# # 6037 : [기초-산술연산] 문장 여러 번 출력하기(설명)(py)
# n=int(input())
# s=input()
# print(n*s)
# # 6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기(설명)(py)
# a,b=map(int,input().split())
# print(a**b)
#
# # 6039 : [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기(py)
# a,b=map(int,input().split())
# print(a**b)
#
# # 6040 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기(설명)(py)
# a,b=map(int,input().split())
# print(a//b)
#
# # 6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기(설명)(py)
# a,b=map(int,input().split())
# print(a%b)
#
# # 6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기(설명)(py)
# a=float(input())
# print(format(a, ".2f"))
#
# # 6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)
# a,b=map(float,input().split())
# print(format(a/b, ".3f"))
#
# # 6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)

#
# a,b=map(int,sys.stdin.readline().split())
#
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# k=a/b
# print(f"{k:.2f}")
#
# # 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)\
# a,b,c=map(float,input().split())
# k=a+b+c
# p=round(k/3,3)
# print("%d" %k,end=" ")
# print("%.2f" %p)
# # 6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기(설명)(py)

#
# n=int(sys.stdin.readline())
# print(n<<1)
#
# # 6047 : [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기(설명)(py)

#
# a,b=map(int,sys.stdin.readline().split())
# print(a<<b)
#
# # 6048 : [기초-비교연산] 정수 2개 입력받아 비교하기1(설명)(py)

#
# a,b=map(int,sys.stdin.readline().split())
#
# if a<b:
#     print("True")
# else:
#     print("False")
# # 6049 : [기초-비교연산] 정수 2개 입력받아 비교하기2(설명)(py)

#
# a,b=map(int,sys.stdin.readline().split())
#
# if a==b:
#     print("True")
# else:
#     print("False")
#
# #6050 : [기초-비교연산] 정수 2개 입력받아 비교하기3(설명)(py)

#
# a,b=map(int,sys.stdin.readline().split())
# if a<=b:
#     print("True")
# else:
#     print("False")
#
# #6051 : [기초-비교연산] 정수 2개 입력받아 비교하기4(설명)(py)

#
# a,b=map(int,sys.stdin.readline().split())
# if a==b:
#     print("False")
# else:
#     print("True")
#
# # 6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기(설명)(py)
# if int(input()):
#     print("True")
# else:
#     print("False")
#
# # 6053 : [기초-논리연산] 참 거짓 바꾸기(설명)(py)
# if not int(input()):
#     print("True")
# else:
#     print("False")
#
# # 6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)

#
# a,b=map(int,sys.stdin.readline().split())
#
# if a and b:
#     print("True")
# else:
#     print("False")
#
# # 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)

#
# a,b=map(int,sys.stdin.readline().split())
#
# if a or b:
#     print("True")
# else:
#     print("False")
#
# # 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)
#

#
# a,b=map(int,sys.stdin.readline().split())
#
# if bool(a)!=bool(b):
#     print("True")
# else:
#     print("False")
#
# # 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)

#
# a,b=map(int,sys.stdin.readline().split())
#
# if bool(a)==bool(b):
#     print("True")
# else:
#     print("False")
#
# # 6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)
#

#
# a,b=map(int,sys.stdin.readline().split())
#
# if not bool(a) and not bool(b):
#     print("True")
# else:
#     print("False")
#
# # 6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기(설명)(py)
#

#
# n=int(sys.stdin.readline())
# print(~n)
#
# # 6060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기(설명)(py)
# a,b=map(int,input().split())
# print(a&b)
#
# # 6061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기(설명)(py)
# a,b=map(int,input().split())
# print(a|b)
#
# # 6062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기(설명)(py)
# a,b=map(int,input().split())
# print(a^b)
#
# # 6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)

# n_list=list(map(int,sys.stdin.readline().split()))
# print(max(n_list))
#
# # 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)
#

# n_list=list(map(int,sys.stdin.readline().split()))
# print(min(n_list))
#
# # 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)
#

#
# Numbers=list(map(int,sys.stdin.readline().split()))
#
# for i in Numbers:
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")
# # 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)

#
# n=int(sys.stdin.readline())
#
# if n<0 :
#   if n%2==0 :
#     print('A')
#   else :
#     print('B')
# else :
#   if n%2==0 :
#     print('C')
#   else :
#     print('D')
#
# # 6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)

#
# n=int(sys.stdin.readline())
#
# if n>=90 :
#   print('A')
# else :
#   if n>=70 :
#     print('B')
#   else :
#     if n>=40 :
#       print('C')
#     else :
#       print('D')
# # 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(py)
# word=input()
#
# if word=="A":
#     print("best!!!")
# elif word=="B":
#     print("good!!")
# elif word=="C":
#     print("run!")
# elif word=="D":
#     print("slowly~")
# else:
#     print("what?")
#
# # 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)

#
# n=int(sys.stdin.readline())
#
# if n//3==1:
#     print("spring")
# elif n//3==2:
#     print("summer")
# elif n//3==3:
#     print("fall")
# else:
#     print("winter")
#
# # 6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기(설명)(py)

#
# while True:
#     n=int(sys.stdin.readline())
#     if n==0:
#         break
#     else:
#         print(n)
# # 6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1(설명)(py)

#
# for i in range(int(sys.stdin.readline()),0,-1):
#     print(i)
#
# # 6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(py)

#
# for i in range(int(sys.stdin.readline())-1,-1,-1):
#     print(i)
#
# # 6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)
#
# w=ord(input())
#
# for i in range(97,w+1):
#     print(chr(i),end=" ")
#
# # 6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1(py)
# for i in range(0,int(input())+1):
#     print(i)
#
# # 6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2(설명)(py)
# for i in range(0,int(input())+1): print(i)
#
# # 6077 : [기초-종합] 짝수 합 구하기(설명)(py)

#
# n=int(sys.stdin.readline())
# hap=0
# for i in range(1,n+1):
#     if i%2==0:
#         hap+=i
# print(hap)
#
# # 6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기(py)

#
# while True:
#     x=sys.stdin.readline().rstrip()
#     if x!="q": print(x)
#     else:
#         print(x)
#         break
# # 6079 : [기초-종합] 언제까지 더해야 할까?(py)

#
# n=int(sys.stdin.readline())
# hap=0
# cnt=0
#
# while hap<n:
#     cnt+=1
#     hap+=cnt
# print(cnt)
#
# # 6080 : [기초-종합] 주사위 2개 던지기(설명)(py)

#
# n,m=map(int,sys.stdin.readline().split())
#
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(i,j)
# # 6081 : [기초-종합] 16진수 구구단 출력하기(py)
# n=int(input(),16)
# for i in range(1,16):
#     print("%X*%X=%X" %(n,i,(n*i)))
#
# # 6082 : [기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)
# for i in range(1,int(input())+1):
#     i=str(i)
#     cnt=i.count("3")+i.count("6")+i.count("9")
#
#     if cnt==0: print(i,end=" ")
#     else: print("X"*cnt,end=" ")
#
#
# # 6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)

#
# a,b,c=map(int,sys.stdin.readline().split())
#
# for i in range(a):
#     for j in range(b):
#         for z in range(c):
#             print(i,j,z)
# print(a*b*c)
#
#
# # 6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)
# h,b,c,s = map(int,input().split())
# m = (h* b * c * s)/8/1024/1024
# print('%.1f MB' %m)
#
#
# # 6085 : [기초-종합] 그림 파일 저장용량 계산하기(py)
# w,h,b=map(int,input().split())
# m=(w*h*b)/8/1024/1024
# round(m,3)
# print('%.2f MB' %m)
#
# # 6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)
# n=int(input())
# answer=0
# k=1
# while answer<n:
#     answer+=k
#     k+=1
# print(answer)
#
# # 6087 : [기초-종합] 3의 배수는 통과(설명)(py)

#
# n=int(sys.stdin.readline())
#
# for i in range(1,n+1):
#     if i%3==0:
#         continue
#     else:
#         print(i,end=" ")
#
# # 6088 : [기초-종합] 수 나열하기1(py)

#
# a,d,n=map(int,sys.stdin.readline().split())
# hap=a+(d*(n-1))
# print(hap)
#
# # 6089 : [기초-종합] 수 나열하기2(py)

# a,b,c=map(int,sys.stdin.readline().split())
# dp=[1]*11
# dp[1]=a
# for i in range(2,11):
#     dp[i]=dp[i-1]*b
# print(dp[c])
#
# # 6090 : [기초-종합] 수 나열하기3(py)

#
# a,m,d,n=map(int,sys.stdin.readline().split())
# dp=[1]*11
# dp[0]=a
# for i in range(1,11):
#     dp[i]=(dp[i-1]*m)+d
# print(dp[n-1])
#
# 6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)

# from math import gcd
#
# def solution(arr):
# 	answer=arr[0]
#
# 	for num in arr:
# 		answer=answer*num//gcd(answer,num)
# 	return answer
# numbers=list(map(int,sys.stdin.readline().split()))
# print(solution(numbers))
#
# 6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)

#
# number=[0]*24
# n=int(input())
#
# a=list(map(int,sys.stdin.readline().split()))
#
# for i in a:
#     number[i]+=1
# number.pop(0)
# for i in number:
#     print(i,end=" ")
#
# 6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)
# n=int(input())
# a=list(map(int,input().split()))
# a.reverse()
# print(*a)
#
# 6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)
# n=int(input())
# a=list(map(int,input().split()))
# print(min(a))


# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)
# checkerboard=[[0]*19 for _ in range(19)]
# n=int(input())
#
# for _ in range(n):
#     a,b=map(int,input().split())
#     checkerboard[a-1][b-1]=1
# for i in range(19):
#     print(*checkerboard[i])


# 6096 : [기초-리스트] 바둑알 십자 뒤집기(py)
# from collections import deque
#
# dx=[0,0,1,-1]
# dy=[1,-1,0,0]
#
# def check(a,b):
#     queue=deque()
#     queue.append((a,b))
#
#     while queue:
#         x,y=queue.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             while 0<=nx<19 and 0<=ny<19:
#                 if maps[nx][ny]==1:
#                     maps[nx][ny]=0
#                 else:
#                     maps[nx][ny]=1
#                 nx+=dx[i]
#                 ny+=dy[i]
#
# maps=[]
# for _ in range(19):
#     w=list(map(int,input().split()))
#     maps.append(w)
# n=int(input())
#
# for _ in range(n):
#     x,y=map(int,input().split())
#     check(x-1,y-1)
# for i in range(19):
#     print(*maps[i])


# 6097 : [기초-리스트] 설탕과자 뽑기(py)
# h,w=map(int,input().split())
# maps=[[0]*w for _ in range(h)]
#
# n=int(input())
#
# for _ in range(n):
#     l,d,a,b=map(int,input().split())
#     a,b=a-1,b-1
#     maps[a][b]=1
#     l-=1
#     while l>0:
#         if d==0:
#             b+=1
#             maps[a][b]=1
#             l-=1
#         else:
#             a+=1
#             maps[a][b]=1
#             l-=1
# for i in range(h):
#     print(*maps[i])

# 6098 : [기초-리스트] 성실한 개미(py)
# maps=[list(map(int,input().split())) for _ in range(10)]
#
# x,y=1,1
# maps[1][1]=9
#
# while True:
#     if maps[x][y+1]==0:
#         y+=1
#         maps[x][y] = 9
#
#     elif maps[x][y+1]==1:
#         if maps[x+1][y]==1:
#             break
#         elif maps[x+1][y]==2:
#             x += 1
#             maps[x][y]=9
#             break
#         else:
#             x += 1
#             maps[x][y]=9
#     else:
#         y += 1
#         maps[x][y] = 9
#         break
#
# for i in range(10):
#     print(*maps[i])