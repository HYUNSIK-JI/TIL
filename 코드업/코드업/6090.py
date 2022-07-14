a,m,d,n=map(int,input().split())
dp=[1]*11
dp[0]=a

for i in range(1,11):
	dp[i]=(dp[i-1]*m)+d
print(dp[n-1])