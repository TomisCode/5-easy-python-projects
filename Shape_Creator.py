def main_menu( length=0, height=0, width=0, radius=0):
    try:
    while option != 6:
          #The main menu, where the user can input data to make different shapes
          print("1. Square")
          print("2. Rectangle")
          print("3. Circle")
          print("4. Cube")
          print("5. Cylinder")
          print("-"*80)
          print("6. Exit the program")
          option = 0
          #Asking the user to select from the main menu to start the program
          option = int(input("Please select an option from the menu above: "))
   
          #A while loop that will continue until the user selects option 6
          if option == 1:
             #If the user selected option 1, run the code for square
             length = int(input("Enter a length for the square: "))
             #Calculating the area of square
             square_area = length * length
             print("The area of your square is", (square_area))
          if option == 2:
             #If the user selected option 2, run the code for rectangle
             length = int(input("Enter a length for the rectangle: "))
             width = int(input("Enter a height for the rectangle: "))
             #Calculating the area of rectangle
             rectangle_area = length * width
             print("The area of your rectangle is: ", (rectangle_area))
          if option == 3:
             #if the user selected option 3, run the code for circle
             radius = int(input("Enter a radius for the circle: "))
             #Calculating the area of circle
             circle_area = 3.14 * radius * radius
             print("The area of your circle is: ", (circle_area))
          if option == 4:
             #If the user selected option 4, run the code for cube
             length = int(input("Enter a length for the cube: "))
             #Calculating the area of cube
             cube_area = length * length * 6
             print("The are of your cube is: ", (cube_area))
          if option == 5:
             #If the user selected option 5, run the code for cylinder
             height = int(input("Enter the height for the cylinder: "))
             radius = int(input("Enter a radius for the cylinder: "))
             #Calculating the area of cylinder
             cylinder_area = 2 * 3.14 * radius * height + 2 * 3.14 * radius * radius
             print("The are of your cylinder is: ", (cylinder_area))
     except: 
            print("An error occurred")

#Making sure that the program always starts at the main menu      
main_menu()
