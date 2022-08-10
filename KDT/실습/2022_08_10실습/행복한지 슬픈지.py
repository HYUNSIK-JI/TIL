import sys

input = sys.stdin.readline
sentence = input().rstrip()

happy = sentence.count(":-)")
sad = sentence.count(":-(")

if happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
elif not happy and not sad:
    print("none")
elif happy == sad:
    print("unsure")