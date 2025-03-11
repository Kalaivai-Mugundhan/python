try:
    num1,num2=eval(input("enter two numbers, seperated by comma:"))
    result=num1/num2
    print("resuelt is:",result)

except ZeroDivisionError:
    print("division by zero is error...!")

except SyntaxError:
    print("Comma  is missing enter the numbers seperated by comma like 1,2")

except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what happens..")