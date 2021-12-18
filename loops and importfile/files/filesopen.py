fhand=open("D:\python practice\myfile.txt",'r')
count =0
for line in fhand:
 count+=1
 print("Line Number ",count, ":", line)
print("Total lines=",count)
s="hello how are you?"
fhand.write(s)
fhand.read(s)
