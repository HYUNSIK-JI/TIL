change = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()
for i in change:
    word = word.replace(i,".")

print(len(word))