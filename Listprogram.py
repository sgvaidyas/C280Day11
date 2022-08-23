l =  [11, 2, 333, 1, 44, 5, 66, 777,-1]


'''
i=0
while (i<len(l)):
    j=2
    while(i+j<=len(l)-1):
        if l[i]>l[i+j]:
           l[i],l[i+j] = l[i+j],l[i]
        j+=2
    print(l)
    i+=1
'''
for i in range(len(l)):
    for j in range(2,len(l)-i,2):
        if l[i]>l[i+j]:
           l[i],l[i+j] = l[i+j],l[i]
    print(l)
