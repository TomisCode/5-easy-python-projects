def add(x, y):
    #This function will add two given numbers
    return x + y

def subtract(x, y):
    #This function will subtract two given numbers
    return x - y

def multiply(x, y):
    #This function will multiply two given numbers
    return x * y

def divide(x, y):
    #This function will divide two given numbers 
    return x / y

print("Welcome, which operation do you want to check out? ")
print("-"*80)
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("-"*80)

while True:
    #Asking the user to input some numbers
    #The user can only type in numbers
    choice = input("Please select an option from the list above: ")
    
    #Checking if the option is one of these, and if it is run the code below
    if choice in ('1', '2', '3', '4'):
        try:
            number1 = float(input("Please enter the first number: "))
            number2 = float(input("Please enter the second number: "))
        except ValueError:
            print("Invalid input. Please try again with a real number...")
            continue
    
        if choice == '1':
            print(number1, "+", number2, "=", add(number1, number2))

        elif choice == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))

        elif choice == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))

        elif choice == '4':
            print(number1, "/", number2, "=", divide(number1, number2))
        
        #Ask if the user wants to do another calculation
        #break loop if the answer is no
        continue_calculation = input("Do you want to continue with another calculation? ")
        if continue_calculation == "no":
            break
    else: 
        print("Invalid Input...")
