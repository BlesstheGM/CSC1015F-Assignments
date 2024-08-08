# program to do basic vector calculations
# Blessing Hlongwane
# HLNBLE002
# 23 April 2023

import math

def dot_product(vector1, vector2):
    # Function to calculate the dot product
    Vz1 = 0
    Vz2 = 0    
    # Function to add the vectors
    vector1 = vector1.split()
    vector2 = vector2.split()
    if len(vector1) == 3:
        Vz1 = eval(vector1[2])
        Vz2 = eval(vector2[2])
    else:
        pass
    Vx1 = eval(vector1[0])
    Vy1 = eval(vector1[1])  
    Vx2 = eval(vector2[0])
    Vy2 = eval(vector2[1])  
    product = (Vx1 * Vx2 + Vy1 * Vy2 + Vz1 * Vz2  )
    return product    
    
def vector_add(vector1, vector2):
    Vz1 = 0
    Vz2 = 0    
    # Function to add the vectors
    vector1 = vector1.split()
    vector2 = vector2.split()
    if len(vector1) == 3:
        Vz1 = eval(vector1[2])
        Vz2 = eval(vector2[2])
    else:
        pass
    Vx1 = eval(vector1[0])
    Vy1 = eval(vector1[1])  
    Vx2 = eval(vector2[0])
    Vy2 = eval(vector2[1])  

    if Vz1 != 0:
        magnitude = (Vx1 + Vx2, Vy1 + Vy2, Vz1 + Vz2 )
    else:
        magnitude = (Vx1 + Vx2, Vy1 + Vy2 )
    return magnitude
    
def magnitude(vectors):
    # Function to calculate the magnitude of the vectors and round off to 1
    vectors = vectors.split()
    Vx = eval(vectors[0])
    Vy = eval(vectors[1])
    if len(vectors) == 3:
        Vz = eval(vectors[2])
    else:
        Vz = 0
    magnitude = math.sqrt(Vx**2 + Vy**2 + Vz**2)
    return round(magnitude, 1)

def scalar_multiplication(vector1, scalar):
    # Function to calculate the scalar multiplication 
    Vz1 = 0
    # Function to add the vectors
    vector1 = vector1.split()
    if len(vector1) == 3:
        Vz1 = eval(vector1[2])
    else:
        pass
    Vx1 = eval(vector1[0])
    Vy1 = eval(vector1[1])  
    
    if Vz1 > 0:
        magnitude = eval(scalar)*Vx1 , eval(scalar) * Vy1, eval(scalar) * Vz1
    else:
        magnitude = eval(scalar)*Vx1 , eval(scalar) * Vy1
    return magnitude

def cross_product(vector1, vector2):
    # Function to calculate the cross product
    vector1 = vector1.split()
    Vx1 = eval(vector1[0])
    Vy1 = eval(vector1[1])  
    Vz1 = eval(vector1[2])
    vector2 = vector2.split()
    Vx2 = eval(vector2[0])
    Vy2 = eval(vector2[1])  
    Vz2 = eval(vector2[2])
    product = (Vy1 * Vz2 - Vz1* Vy2, Vz1*Vx2 - Vx1*Vz2, Vx1 * Vy2 - Vy1*Vx2)
    return product
    
while True:
    # Contains all of our options 
    options = {1:'Magnitude of a vector', 2:'Vector addition', 3:'Scalar multiplication', 4:'Dot product of two vectors', 5:'Cross product of two 3-dimensional vectors', 6:'Exit'}
    print("Choose an option:")
    print("1. {}".format(options[1])) 
    print("2. {}".format(options[2]))
    print("3. {}".format(options[3]))
    print("4. {}".format(options[4]))
    print("5. {}".format(options[5]))
    print("6. {}".format(options[6]))
    user_input = input("")
    # Different options dependent on which option an user chose
    if user_input == '1':
        vectors = input("Enter the components of the vector separated by spaces:\n")
        print("Magnitude of the vector is:", magnitude(vectors))
        
    elif user_input == '2':
        vector1 = input("Enter the components of the first vector separated by spaces:\n")
        vector2 = input("Enter the components of the second vector separated by spaces:\n")
        if len(vector1) != len(vector2):
            print("Error: Vectors must have the same length.")
        else:
            print("Sum of the vectors is:", vector_add(vector1, vector2))
            
    elif user_input == '3':
        vector1 = input("Enter the components of the vector separated by spaces:\n")
        scalar = input("Enter the scalar:\n")
        print("Scalar multiplication of the vector is:", scalar_multiplication(vector1, scalar))
                
    elif user_input == '4':
        vector1 = input("Enter the components of the first vector separated by spaces:\n")
        vector2 = input("Enter the components of the second vector separated by spaces:\n")
        if len(vector1) != len(vector2):
            print("Error: Vectors must have the same length.")
        else:
            print("Dot product of the vectors is:", dot_product(vector1, vector2))        
               
    elif user_input == '5':
        vector1 = input("Enter the components of the first 3-dimensional vector separated by spaces:\n")
        vector2 = input("Enter the components of the second 3-dimensional vector separated by spaces:\n") 
        if len(vector1) != len(vector2):
            print("Error: Vectors must have the same length and 3-dimensional.")
        else:
            print("Cross product of the vectors is:", cross_product(vector1, vector2))
              
    elif user_input == '6':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please choose a valid option.")