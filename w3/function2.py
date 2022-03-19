def Rectangle(width, height):
    # calculate the area
    Area = width * height
    # calculate the Perimeter
    Perimeter = 2 * (width + height)
  
    print("\n Area is: %.2f" %Area)
    print(" Perimeter is: %.2f" %Perimeter)
     
width = float(input('Enter the Width: '))
height = float(input('Enter the Height: '))
 
Rectangle(width, height)