name1="Poojitha".lower()
name2="pravallika".lower()
count=0
if len(name1)>len(name2):
    target=name1
else:
    target=name2
if target==name1:
    ref=name2
else:
    ref=name1
for i in range(len(ref)):
    if target.count(ref[i])==ref.count(ref[i]):
        count+=target.count(ref[i])
    else:
        if target.count(ref[i])>ref.count(ref[i]):
            count+=ref.count(ref[i])
        else:
            count+=target.count(ref[i])
count=count*2
fcount=(len(name1)+len(name2))-count
ctr=0
l=['f','l','a','m','e','s']
dicti={'f':'friends','l':'love','a':'affection','m':'marriage','e':'enemy','s':'siblings'}
tcount=fcount
while len(l)!=1:
   fcount=12
   tcount=fcount
   if tcount>len(l):
       while tcount>len(l):
           tcount=fcount-len(l)
           fcount=fcount-len(l)
   ctr=0
   while ctr!=tcount:
      ctr+=1
   if ctr==tcount:
       l.remove(l[ctr-1])
       if ctr!=len(l):
           l=l[ctr-1:]+l[:ctr-1]
print(dicti[l[0]]) 

