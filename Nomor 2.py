N,M = map(int, input().split())
count = (N//4)+(M//4)
if(N%4>=2 and M%4>=2):
    count+=1
    
print(count)