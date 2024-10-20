import numpy as np  #Import NumPy for matrix and array operations
import matplotlib.pyplot as plt  #Import Matplotlib for plotting

#Function for translation of a point in 3D space
def translation(point, t_x, t_y, t_z):
    #Create a translation matrix
    translation_matrix = np.array([t_x, t_y, t_z])
    #Perform the translation by adding the translation matrix to the original point
    translated_point = point + translation_matrix
    return translated_point  #Return the translated point


#Function for scaling a point in 3D space
def scaling(point, s_x, s_y, s_z):
    # Create a scaling matrix
    scaling_matrix = np.array([s_x, s_y, s_z])
    #Perform the scaling by multiplying the point's coordinates by the scaling matrix
    scaled_point = point * scaling_matrix
    return scaled_point  #Return the scaled point


#Function for rotating a point around the Z-axis by a given angle (in radians)
def rotation_across_z(point, theta):
    #Create the rotation matrix for rotating around the Z-axis
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                [np.sin(theta), np.cos(theta), 0],
                                [0, 0, 1]])
    #Perform the rotation by multiplying the rotation matrix with the point's coordinates
    rotated_point = np.dot(rotation_matrix, point)
    return rotated_point  #Return the rotated point


#Function to plot the original and transformed points on a 3D scatter plot
def plot_points(original_point, transformed_point, title):
    fig = plt.figure()  #Create a new figure for the plot
    ax = fig.add_subplot(111, projection='3d')  #Add a 3D subplot to the figure

    #Plot the original point in red and label it as "Original"
    ax.scatter(original_point[0], original_point[1], original_point[2], color='r', label='Original Point')
    ax.text(original_point[0], original_point[1], original_point[2], "Original", color='r')  #Annotate the point

    #Plot the transformed point in blue and label it as "Transformed"
    ax.scatter(transformed_point[0], transformed_point[1], transformed_point[2], color='b', label='Transformed Point')
    ax.text(transformed_point[0], transformed_point[1], transformed_point[2], "Transformed", color='b')  #Annotate the point

    #Set labels for the X, Y, and Z axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    #Set the title of the plot (either "Translation", "Scaling", or "Rotation")
    ax.set_title(title)
    #Add a legend to the plot to distinguish between the original and transformed points
    plt.legend()
    plt.show() #Display the plot

# Main function to get user input and perform the chosen transformations
def main_with_options():
    #Prompt the user to input the X coordinate of the original point
    x = float(input("Enter the X coordinate of the point: "))
    #Prompt the user to input the Y coordinate of the original point
    y = float(input("Enter the Y coordinate of the point: "))
    #Prompt the user to input the Z coordinate of the original point
    z = float(input("Enter the Z coordinate of the point: "))

    #Create a NumPy array to represent the original point in 3D space
    original_point = np.array([x, y, z])
    transformed_point = original_point  #Start with the original point

    #Display options for the user to choose transformations
    print("\nWhat transformations would you like to apply?")
    print("1. Translation")
    print("2. Scaling")
    print("3. Rotation around Z-axis")
    print("4. Apply all transformations")

    #Get the user's choice of transformation
    choice = int(input("\nEnter the number corresponding to your choice (1-4): "))

    #Perform translation if the user chooses option 1 or 4
    if choice == 1 or choice == 4:
        #Prompt the user to input translation values for X, Y, Z
        t_x = float(input("Enter translation value for X: "))
        t_y = float(input("Enter translation value for Y: "))
        t_z = float(input("Enter translation value for Z: "))

        #Apply the translation
        transformed_point = translation(transformed_point, t_x, t_y, t_z)
        plot_points(original_point, transformed_point, "Translation")

    #Perform scaling if the user chooses option 2 or 4
    if choice == 2 or choice == 4:
        #Prompt the user to input scaling factors for X, Y, Z
        s_x = float(input("Enter scaling factor for X: "))
        s_y = float(input("Enter scaling factor for Y: "))
        s_z = float(input("Enter scaling factor for Z: "))

        #Apply the scaling
        transformed_point = scaling(transformed_point, s_x, s_y, s_z)
        plot_points(original_point, transformed_point, "Scaling")

    #Perform rotation if the user chooses option 3 or 4
    if choice == 3 or choice == 4:
        #Prompt the user to input the rotation angle (in radians) for the Z-axis
        theta = float(input("Enter the rotation angle (in radians) around Z-axis: "))

        #Apply the rotation
        transformed_point = rotation_across_z(transformed_point, theta)
        plot_points(original_point, transformed_point, "Rotation across Z-axis")

#Uncomment this line to run the program locally
main_with_options()
