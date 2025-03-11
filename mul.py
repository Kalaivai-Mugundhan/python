try:
    num1,num2= eval(input("enter two numbers, seperated by commas:"))
    result=num1/num2
    print("Result is:",result)


#different types of errors
except ZeroDivisionError:
    print("Division by zero is error...!")

except SyntaxError:
    print("Comma is missing, enter the value using comma like 1,2...")

except:
    print('wrong input')
else:
    print("no exceptions")
finally:
    print("this will executing no mater what happens....")