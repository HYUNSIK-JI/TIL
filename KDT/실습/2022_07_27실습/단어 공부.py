word = input().upper()

check = [0] * 26

for i in word:
    check[ord(i) - 65] += 1

# print(check)

mx = max(check)
cnt = 0
for i in check:
    if i == mx:
        cnt += 1

if cnt > 1:
    print("?")
else:
    print(chr(check.index(mx) + 65))