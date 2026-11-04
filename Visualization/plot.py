import matplotlib.pyplot as plt
import numpy as np

def setup_plotting(dimension):
    if dimension == 2:
        figure, axis = plt.subplots()

    elif dimension == 3:
        figure = plt.figure()
        axis = figure.add_subplot(111, projection="3d")
    else:
        figure, axis = plt.subplots()
    
    plt.ion()
    return figure, axis

def plot(axis, dimension, vector, composition):
    axis.clear()

    if dimension == 2:
        # Plotting basis vector
        colors = ["red", "green"]
        basis_str = ["î", "ĵ"]

        for i in range(2):
            basis = composition[:,i]
            axis.quiver(0,0, basis[0], basis[1], angles="xy", scale_units="xy", scale=1, color=colors[i])
            axis.text(basis[0], basis[1], f"{basis_str[i]}", color= colors[i])

        axis.quiver(0, 0, vector[0], vector[1], angles="xy", scale_units="xy", scale=1, color="blue")

        axis.scatter(0, 0, color="red", s=50)
        axis.text(0,0, "(0, 0)", color="red")

        axis.scatter(vector[0], vector[1], color="green", s=50)
        axis.text(
            vector[0], vector[1],
            f"O ({vector[0]:.2f}, {vector[1]:.2f})",
            color="green"
        )
        limit = max(5, np.max(abs(vector))*1.2)
        axis.set_xlim(-limit, limit)
        axis.set_ylim(-limit, limit)
        axis.set_aspect("equal", adjustable="box")

        # axis.axhline(0, color="black")
        # axis.axvline(0, color="black")
        axis.grid(True)

    elif dimension == 3:
        # plotting basis vectors
        colors = ["red", "green", "purple"]
        basis_str = ["î", "ĵ", "k̂"]

        # Plot the transformed basis vectors
        for i in range(3):

            basis = composition[:, i]

            axis.quiver(
                0, 0, 0,
                basis[0], basis[1], basis[2],
                color=colors[i],
                arrow_length_ratio=0.12,
                linewidth=2
            )

            axis.text(
                basis[0], basis[1], basis[2],
                f" {basis_str[i]}",
                color=colors[i]
            )

        # Plotting vector
        axis.quiver(
            0, 0, 0,
            vector[0], vector[1], vector[2],
            color="blue",
        )

        axis.text(
            vector[0], vector[1], vector[2],
            f" v = {np.round(vector, 2)}",
            color="blue"
        )


        limit = max(5, np.max(np.abs(vector)) * 1.3)

        axis.set_xlim(-limit, limit)
        axis.set_ylim(-limit, limit)
        axis.set_zlim(-limit, limit)
        axis.set_box_aspect((1, 1, 1))
        axis.set_xlabel("X")
        axis.set_ylabel("Y")
        axis.set_zlabel("Z")
        axis.grid(True)

    else:
        nd_plot(axis, vector, dimension, composition)

    axis.set_title(f"Current vector: {np.round(vector, 3)}")


def nd_plot(axis, vector, dimensions, composition):

    x = np.arange(dimensions) # array for x coordinates

    # plot basis vectors
    for i in range(dimensions):
        basis = composition[:, i]
        axis.plot(x, basis, marker="o", linewidth=1.5, alpha=0.65, label=f"Basis e{i+1}")

    # plotting vector
    axis.plot(x, vector, marker="o", linewidth=2.5, color="Black", label=f"vector")

    limit = max(5, np.max(abs(vector))*1.3)
    axis.set_ylim(-limit, limit)

    axis.axhline(0, color="black", linewidth=0.8)
    axis.grid(True, axis="y", alpha=0.3)

    for ax in x:
        axis.axvline(ax, color="gray")

    axis.legend()