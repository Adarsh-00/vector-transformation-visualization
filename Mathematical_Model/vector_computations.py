import numpy as np

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