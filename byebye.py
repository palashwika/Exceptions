valid=False
while not valid: #using nested while loop, while true
    try:
        n=int(input("Enter a number: "))
        #enter a even number
        while n%2==0:

            print("bye")
        #valid=True #if we did not have this statement it will keep running until user enters an even number; infinite loop
    except ValueError: #printed when anything apart from a number is inputted
        print("Invalid")

