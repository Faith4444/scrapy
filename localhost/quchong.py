#coding=utf-8
f=open('ecshop_url_txt')
f2=open('rs.txt','w')
tmp=set()
while 1:
    line=f.readline()
    tmp.add(line)
    if line =='':
        break

for x in tmp:
    f2.write(x)
f.close()
f2.close()