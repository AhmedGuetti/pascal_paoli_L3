import unittest

# Import the function to be tested
from graph import *

class TestMatriceIncidence(unittest.TestCase):

    def test_square_matrix_atelier(self):
        # Test with a square adjacency matrix
        adj_matrix = np.array([ [0, 1, 1, 0, 0],
                                [0, 0, 1, 0, 1],
                                [0, 0, 0, 1, 0],
                                [0, 0, 0, 0, 1],
                                [0, 0, 1, 0, 0]])
        incidence_matrix = matriceIncidence(adj_matrix)
        expected_result = np.array([[1, 1, 0, 0, 0, 0, 0],
                                    [-1, 0, 1, 1, 0, 0, 0],
                                    [0, -1, -1, 0, 1, 0, -1],
                                    [0, 0, 0, 0, -1, 1, 0],
                                    [0, 0, 0, -1, 0, -1, 1]])
        self.assertTrue(np.array_equal(incidence_matrix, expected_result))


    def test_square_matrix(self):
        # Test with a square adjacency matrix
        adj_matrix = np.array([[0, 1, 1],
                                [1, 0, 0],
                                [1, 0, 0]])
        incidence_matrix = matriceIncidence(adj_matrix)
        print(incidence_matrix)
        expected_result = np.array([[1, 1],
                                    [-1, 0],
                                    [0, -1]])
        self.assertTrue(np.array_equal(incidence_matrix, expected_result))

    def test_non_square_matrix(self):
        # Test with a non-square adjacency matrix
        adj_matrix = np.array([[0, 1],
                                [1, 0],
                                [1, 0]])
        result = matriceIncidence(adj_matrix)
        self.assertEqual(result, None)

    def test_symmetric_matrix(self):
        # Test with a symmetric adjacency matrix
        adj_matrix = np.array([[0, 1, 1],
                                [1, 0, 1],
                                [1, 1, 0]])
        incidence_matrix = matriceIncidence(adj_matrix)
        expected_result = np.array([[1, 1, 1],
                                    [-1, -1, -1],
                                    [0, 0, 0]])
        self.assertTrue(np.array_equal(incidence_matrix, expected_result))

    def test_asymmetric_matrix(self):
        # Test with an asymmetric adjacency matrix
        adj_matrix = np.array([[0, 1, 0],
                                [0, 0, 1],
                                [0, 0, 0]])
        incidence_matrix = matriceIncidence(adj_matrix)
        print(incidence_matrix)
        expected_result = np.array([[1, 1],
                                    [-1, 0],
                                    [0, -1]])
        self.assertTrue(np.array_equal(incidence_matrix, expected_result))




if __name__ == '__main__':
    unittest.main()


    