
no_1=int(input("enter the 1st number: "))
no_2=int(input("enter the 2nd number: "))
no_3=int(input("enter the 3nd number: "))
if(no_1==no_2 and no_2==no_3):
    print("All numbers are equal")
elif(no_1==no_2):
    print("First number and second  no are same")
elif(no_3==no_2):
    print("Second number and third no are same")    
elif(no_1==no_3):
    print("First number and the third nuber are same")
elif(no_1>no_2 and no_1>no_3):
    print("First number is greater than all number")
elif(no_2>no_3 and no_2>no_1):
    print("Second number is greater than all numbers") 
else:
    print("Third number is greater than all  numbers")                   

