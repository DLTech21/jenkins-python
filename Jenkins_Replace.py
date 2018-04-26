import sys
import re

args = sys.argv
regex=args[1]
filename=args[2]
target=args[3]

pattern2 = re.compile(r''+regex)

old_file=filename
fopen=open(old_file,'r')
w_str=""
for line in fopen:
     line=pattern2.sub(target,line)
     w_str+=line
print w_str
wopen=open(old_file,'w')
wopen.write(w_str)
fopen.close()
wopen.close()