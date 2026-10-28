import numpy as np
import matplotlib.pyplot as plt

def input_vector(dimensions, prompt="Enter vector"):
    while True:
        values = list(map(float, input(f"{prompt} ({dimensions} values): ").split()))

        if len(values) == dimensions:
            return np.array(values)
        
        print(f"Please enter exactly {dimensions} values.")

def take_input_tranformation(dimensions):
    basis_vectors = []

    for i in range(dimensions):
        basis = input_vector(
            dimensions,
            f"Enter transformed basis vector {i + 1}"
        )
        basis_vectors.append(basis)

    return np.column_stack(basis_vectors) # convert each basis vector into coloumns
    
def perform_transformation(vector, composition, transformation):

    # A = M2.M1
    composition = transformation @ composition
    # v = A.x
    transformation = composition @ vector

    return composition, transformation

def setup_plotting(dimension):
    if dimension == 2:
        figure, axis = plt.subplots()

    elif dimension == 3:
        figure = plt.figure()
        axis = figure.add_subplot(111, projection="3d")
    else:
        return None, None
    
    plt.ion()
    return figure, axis

def plot(axis, dimension, vector, composition):
    axis.clear()

    if dimension == 2:
        axis.quiver(0, 0, vector[0], vector[1], angles="xy", scale_units="xy", scale=1, color="blue")
        limit = max(5, np.max(abs(vector))*1.2)
        axis.set_xlim(-limit, limit)
        axis.set_ylim(-limit, limit)
        axis.set_aspect("equal", adjustable="box")
        axis.axhline(0, color="black")
        axis.axvline(0, color="black")
        axis.grid(True)

    elif dimension == 3:
        axis.quiver(0,0,0, vector[0], vector[1], vector[2], color="blue")
        limit = max(5, np.max(abs(vector))*1.2)
        axis.set_xlim(-limit, limit)
        axis.set_ylim(-limit, limit)
        axis.set_zlim(-limit, limit)
        axis.set_box_aspect((1,1,1))
        axis.set_xlable("X")
        axis.set_ylable("Y")
        axis.set_zlable("Z")

    axis.set_title(f"Current vector: {np.round(vector, 3)}")

    # else:
    #     print("plotting nd")


def main():
    dimensions = int(input("In what dimention do you want to visulaize the transformations (eg. 2,3,4 etc): "))

    vector = input_vector(dimensions)
    composition = np.eye(dimensions)

    fig, ax = setup_plotting(dimensions)
    if fig is not None:
        plot(ax, dimensions, vector, composition)
        plt.show(block=False)
    else:
        print("ND mode: numerical computation only.")

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
