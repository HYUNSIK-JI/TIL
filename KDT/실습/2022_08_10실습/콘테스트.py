w, k = [], []
for i in range(1, 21):
    if i <= 10:
        w.append(int(input()))
    else:
        k.append(int(input()))
w.sort(reverse=True)
k.sort(reverse=True)
print(sum(w[:3]), sum(k[:3]))