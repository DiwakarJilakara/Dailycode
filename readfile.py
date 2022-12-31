f=open('textfile.txt','r')
source=(f.readline().split(' '))
destination=f.readline().split(' ')
print(source,destination)