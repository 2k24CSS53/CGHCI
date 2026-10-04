import numpy as np

#TODO 1 Use the formula from the problem description, ten np.clip to stay in[out_min,
def contrast_stretch(
        image:np.ndarray,
        in_min: float,
        in_max: float,
        out_min:float=0.0,
        out_max: float=255.0,
)       -> np.ndarray:
        """change image values from one range to another."""
        raise NotImplementedError("TODO: complete the formula ")

        problem_4_input = np.array([50, 100, 150], dtype=np.float32)

        # TODO 2: remove the # symbols and run the given test.
        # expected =np.array([0.0, 127.5, 255.0], dtype=np.float32)
        # np.testing.assert_allclose(contrast_stretch(problem_4_input, 50,150), expected)
print("problem 4 passed")