L = int(input())
n = int(input())
x=[]
for i in range(0,n):
  x.append(int(input()))

x.sort()
ans=[]
ans.append(x[0])
j=0
for i in range(1,n):
  if x[i] > ans[j]+L:
    ans.append(x[i])
    j+=1

for i in ans:
  print(i)