try:
    num1, num2 = eval(input("Enter 2 numbers, separated by a comma: "))
    result=num1/num2
    print("Result is", result)
#using multple excpet block fro different type of error

except ZeroDivisionError:
    print("Division by zero is error!!")
except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1,2")
except:
    print("Wrong input")

else: #can be used without an if, will be executed when no errors occur
    print("No exceptions")

finally: #print at the end no matter what whether error occurred or not
    print("This will execute no matter what")
    
