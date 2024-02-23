import collections

file=open("temp.txt",'r')

c=dict()

for i in file:

    i=i.strip()
    # i=i.lower()

    words=i.split(" ")

    for w in words:
        if w in c:
            c[w]+=1
        else:
            c[w]=1

sorted_c=sorted(c.items(),key=lambda x:x[1])

res=dict(list(sorted_c)[-5:])

print(res)


