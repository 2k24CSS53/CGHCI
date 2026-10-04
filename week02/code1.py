import numpy as np

# TODO 1:Return 255 when a pixel is >=threshold;otherwise return 0.
def threshold_image (image: np.ndarray, threshold: int) ->np.ndarray:
    return np.where (image >= threshold,255, 0).astype(np.uint8) 

problem_1_input = np.array([[20, 128, 200], [100, 150, 250]], dtype=np.uint8)
problem_1_expected = np.array([[0, 255, 255], [0, 255, 255]], dtype=np.uint8)

# TODO 2: Remove the # symbols and run the test,
np.testing.assert_array_equal(threshold_image(problem_1_input,128),problem_1_expected)
print("problem 1 passed")