'''Chained Condition statement combined with AND operator'''
marks=int (input("Enter the marks obtain"))
if (marks>=90):
    print("exam passed with s grade")
elif(marks>=80 and marks<90):
    print("exam passed with distinction ")   
elif(marks>=70 and marks<80):
    print("exam passed with first class")
elif(marks>=55 and marks<70):
    print("exam start with second class")         
elif(marks>=35 and marks<55):
    print("just pass")
else:
    print("Fail")        