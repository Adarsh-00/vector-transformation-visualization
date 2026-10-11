import numpy as np
import matplotlib.pyplot as plt

input_vector = list(map(int, input("enter your vector: ").split()))

vector = np.array(input_vector)
tail_of_vector = (0,0)

plt.quiver(tail_of_vector[0], tail_of_vector[1], vector[0], vector[1], angles='xy', scale_units = 'xy', scale = 1, color='blue')
plt.grid(True)
plt.xlim(-2,10)
plt.ylim(-2,10)
plt.axhline(0, color='black')
plt.axvline(0,color='black')
plt.show()

composition = np.array([[1,0],[0,1]])

while(True):
    x = input("Do you want to add transformation (yes/no) :")
    if x == 'yes':
    #vector transformation
        user_tras_icap = list(map(int, input("Enter x transformation cordinates").split()))
        user_tras_jcap = list(map(int, input("Enter y transformation cordinates").split()))
        
        transformation_matrix = np.array([user_tras_icap,user_tras_jcap])

        composition = transformation_matrix @ composition

        print(composition)

        trasformed_x = composition[0][0] * vector[0] + composition[1][0] * vector[1]
        trasformed_y = composition[0][1] * vector[0] + composition[1][1] * vector[1]
        # print(trasformed_x, trasformed_y)

        plt.quiver(tail_of_vector[0], tail_of_vector[1], trasformed_x, trasformed_y, angles='xy', scale_units = 'xy', scale = 1, color='blue')
        plt.grid(True)
        plt.xlim(-10,10)
        plt.ylim(-10,10)
        plt.axhline(0, color='black')
        plt.axvline(0,color='black')
        plt.show()

    else:
        break