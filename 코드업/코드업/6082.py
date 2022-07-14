for i in range(1,int(input())+1):
    i=str(i)
    cnt=i.count("3")+i.count("6")+i.count("9")

    if cnt==0: print(i,end=" ")
    else: print("X"*cnt,end=" ")