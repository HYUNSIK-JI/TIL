a,b,c=map(int,input().split())
dp=[1]*11
dp[1]=a
for i in range(2,11):
	dp[i]=dp[i-1]*b
print(dp[c])