#using a try and except
try: #enables exception handling keywords
    number=int(input("Enter a number:"))
    print("The number entered is", number)
#using value error
except ValueError as ex:
    print("Exception:", ex)