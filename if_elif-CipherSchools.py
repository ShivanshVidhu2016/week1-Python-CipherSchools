age=int(input("enter your age:"))
if age==0 or age<0:
    print("you can't watch")
elif 0<age<=3:    
    print("ticket price: FREE")
elif 3<age<=10:
    print("tickect price: 150")  
elif 10<age<=60:
    print("tickect price: 250")    
else:
    print("tickect price: 200")      