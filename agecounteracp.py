try:    
    age=int(input("Enter your age: "))
except ValueError:
    print("Value Error! Please enter an integer value")
else:
    if age%2==0:
        print("Your age is an even number !")
    else:
        print("Your age is an odd number !")
       


   


    