import os
import sys
count=1
lines=''
copyline=''
numbers={'0':'1 0 0 0 0 0 0 0 0 0','1':'0 1 0 0 0 0 0 0 0 0','2':'0 0 1 0 0 0 0 0 0 0','3':'0 0 0 1 0 0 0 0 0 0'
         ,'4':'0 0 0 0 1 0 0 0 0 0','5':'0 0 0 0 0 1 0 0 0 0','6':'0 0 0 0 0 0 1 0 0 0','7':'0 0 0 0 0 0 0 1 0 0'
         ,'8':'0 0 0 0 0 0 0 0 1 0','9':'0 0 0 0 0 0 0 0 0 1'}
file=open('optdigits-orig.windep','r')
file.seek(20)
for line in file.readlines():
    if count!=33:
        templist = []
        templine = line.rstrip('\n')
        for i in templine:
            lines+= i+' '
    else:
        copyline+=numbers[line.strip()]
        copyline+='\n'
        lines+='\n'
        count=0
    count = count + 1
copy=open('output1.txt','w')
copy.write(lines)
copy.close()
copy=open('output2.txt','w')
copy.write(copyline)
copy.close()
file.close()