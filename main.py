import numpy as np
import matplotlib.pyplot as plt
from Mathematical_Model.vector_computations import (input_vector, take_input_tranformation, perform_transformation)
from Visualization.plot import (plot, setup_plotting)

def main():
    dimensions = int(input("In what dimention do you want to visulaize the transformations (eg. 2,3,4 etc): "))

    vector = input_vector(dimensions)
    composition = np.eye(dimensions)

    fig, ax = setup_plotting(dimensions)

    plot(ax, dimensions, vector, composition)
    plt.show(block=False)

    while(True):
        choice = input("\nAdd transformation? (yes/no): ").strip().lower()

        if choice not in ("yes", "no"):
            print("Please enter yes or no.")
            continue

        if choice == "no":
            break

        transformation = take_input_tranformation(dimensions)
        composition, transformed_vector = perform_transformation(vector, composition, transformation)
        print(composition)
        print(transformed_vector)

        if fig is not None and plt.fignum_exists(fig.number):
            plot(ax, dimensions, transformed_vector, composition)
            fig.canvas.draw_idle()
            plt.pause(0.1)

    if fig is not None and plt.fignum_exists(fig.number):
        plt.ioff()
        plt.show()

if __name__ == "__main__":
    main()