import numpy as np 

# TODO 1: Write the two kernels, multiply them with the block, and add the results to get
def soble1_reponse(block: np.ndarray) -> tuple[float, float, float]:
    """Return gx, gy, and edge strength,"""
    raise NotImplementedError("TODO: complete the soble calculation")

problem_5_input = np.array([[20, 20, 200], [20,20,200], [20, 20, 200]], dtype=np.float32)

# TODO 2:Remove the # symbols and run the given test.
# gx, gy, strength = sobel_response(problem_5_inout)
# assert gx == 720.0  and gy == 0.0
print("Problem 5 passed")