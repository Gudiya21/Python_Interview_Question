def jump(self,a):
    l=len(a)
    count=0
    pos=0
    for i in range(1,l):
        a[i]=max(i+a[i],a[i-1])
    while pos<l-1:
        if pos>=a[pos]:
            return -1
        if pos<a[pos]:
            count+=1
            pos=a[pos]
        return(count)
print(jump())
