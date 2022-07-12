w,h,b=map(int,input().split())
m=(w*h*b)/8/1024/1024
round(m,3)
print('%.2f MB' %m)