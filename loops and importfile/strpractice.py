name=input("enter you r name : ")

date=input("enter the date : ")
templet='''
Dear <|name|>
You are selected in the selection process,
so please join at the date of <|date|>
'''
print(templet.replace('<|name|>',name).replace('<|date|>',date))