import sys
import re

input = sys.stdin.readline

# 문서
document = input().rstrip()
# 찾을 문자열
find = input().rstrip()
#찾을 문자열로 매치를 정해둔뒤 document안에 찾을문자열이 중복이면 [] 리스트 형태로 변환
print(len(re.compile(find).findall(document)))