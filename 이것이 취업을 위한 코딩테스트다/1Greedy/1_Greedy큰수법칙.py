#n,m,k=map(int, input().split())
#data = list(map(int,input().split()))

n,m,k=5,8,3
data=[2,4,5,4,6]
data.sort(reverse=True)
first=data[0]
second=data[1]
res=0

while m!=0:
    for i in range(k):
        if m==0:
            break
        res+=first
        m-=1
    res+=second
    m-=1
print(res)

# count=int(m/(k+1))*k
# count+=m%(k+1)

# result=0
# result+=count*first
# result+=(m-count)*second

