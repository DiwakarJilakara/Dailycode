source=[3,6,'n']
destination=[1,0]
requireddirection=[]
k=0
power=200
listoddirections=['e','n','w','s']
if(destination[0]-source[0]>0):
    requireddirection.append('e')
elif(destination[0]-source[0]<0):
    requireddirection.append('w')
if(destination[1]-source[1]>0):
    requireddirection.append('n')
elif(destination[1]-source[1]<0):
    requireddirection.append('s')
while(len(requireddirection)!=0):
    for i in range(4):
        if(listoddirections[i]==source[2]):
            k=i
            break;
    if(source[2] in requireddirection):
        requireddirection.remove(source[2])
    elif(listoddirections[(k+1)%4] in requireddirection):
        power-=5
        requireddirection.remove(listoddirections[(k+1)%4])
        source[2]=listoddirections[(k+1)%4]
    elif(listoddirections[(k+3)%4] in requireddirection):
        power-=5
        requireddirection.remove(listoddirections[(k+3)%4])
        source[2]=listoddirections[(k+3)%4]
    elif(listoddirections[(k+2)%4] in requireddirection):
        power-=10
        requireddirection.remove(listoddirections[(k+2)%4])
        source[2]=listoddirections[(k+2)%4]
k=abs((destination[0]-source[0]))
power=power-(k*10)
k=abs((destination[1]-source[1]))
power=power-(k*10)
print(power)





