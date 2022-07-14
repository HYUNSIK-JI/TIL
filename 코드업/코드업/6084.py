h,b,c,s = map(int,input().split())
m = (h* b * c * s)/8/1024/1024
print('%.1f MB' %m)