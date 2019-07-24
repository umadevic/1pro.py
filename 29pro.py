#a
inp=int(input())

ii=0

nm=0

b=[]

while ii<90 and ii<inp:

  s2=0

  for j in str(inp-ii):

    s2+=int(j)

  if s2+(inp-ii)==inp:

    nm+=1

    b.append(inp-ii)

  ii+=1

print(nm)

for ii in b:

  print(ii)
