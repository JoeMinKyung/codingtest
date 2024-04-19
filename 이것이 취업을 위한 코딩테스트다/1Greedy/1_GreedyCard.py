n,m = map(int,input().split())
res=0

for i in range(n):
    data=list(map(int,input().split()))
    min_value=min(data)
    res=max(res,min_value)
print(res) 

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2