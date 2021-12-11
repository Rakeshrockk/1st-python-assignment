def countChar(st,ch):
 count=0
 for i in st:
    if i==ch:
        count+=1
 return count
st=input("Enter a string:")
ch=input("Enter a character to be counted:")
c=countChar(st,ch)
print("{0} appeared {1} times in {2}".format(ch,c,st))