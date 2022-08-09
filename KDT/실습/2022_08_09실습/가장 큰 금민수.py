n = int(input())
while True:
    if len(str(n)) == str(n).count("4") + str(n).count("7"):
        print(n)
        break
    n -= 1