lst=[15,0,105]
l=len(lst)
i=0
m=-1
while i<l-1:
    j=i+1
    while j<1:
        s=set(str(lst[i]))
        t=set(str(lst[j]))
        if not len(s.interaction(t)):
            tmp=lst[i]+lst[j]
            m=max(m,temp)
        j+=1
    i+=1
print(m)   
