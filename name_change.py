import os

path='./datasets/source_pose/'


f=os.listdir(path)
k=0
print(len(f))
for j in f:
    oldname=path+f[k]
    newname=path+str(f[k]).zfill(20)
    os.rename(oldname,newname)
    print(oldname,'=====>',newname)
    k+=1

x=os.listdir(path)
x.sort()

n=0

for i in x:
    oldname=path+x[n]
    newname=path+'{:05}.png'.format(n)
    os.rename(oldname,newname)
    print(oldname,'=====>',newname)
    n+=1