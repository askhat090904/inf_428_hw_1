import numpy as np
import unittest

def time_to_cyclic_features(hour):
    radians = hour * (2 * np.pi / 24)
    sin_time = np.sin(radians)
    cos_time = np.cos(radians)
    return sin_time, cos_time


class TestCyclicFeatures(unittest.TestCase):

    def test_midnight(self):
        sin_time, cos_time = time_to_cyclic_features(0)
        self.assertAlmostEqual(sin_time, 0, places=7)
        self.assertAlmostEqual(cos_time, 1, places=7)

    def test_noon(self):
        sin_time, cos_time = time_to_cyclic_features(12)
        self.assertAlmostEqual(sin_time, 0, places=7)
        self.assertAlmostEqual(cos_time, -1, places=7)

    def test_evening(self):
        sin_time, cos_time = time_to_cyclic_features(18)
        self.assertAlmostEqual(sin_time, -1, places=7)
        self.assertAlmostEqual(cos_time, 0, places=7)

    def test_difference(self):
        sin_time_23, cos_time_23 = time_to_cyclic_features(23)
        sin_time_1, cos_time_1 = time_to_cyclic_features(1)

        angle_diff = np.arccos(sin_time_23 * sin_time_1 + cos_time_23 * cos_time_1)

        expected_diff = 2 * np.pi / 24 * 2
        self.assertAlmostEqual(angle_diff, expected_diff, places=7)


if __name__ == '__main__':
    unittest.main()
