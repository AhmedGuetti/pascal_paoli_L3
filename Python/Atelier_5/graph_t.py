import unittest

# Importer la fonction à tester
from graph import *

class TestMatriceIncidence(unittest.TestCase):

    def test_square_matrix_atelier(self):
        """
        Teste la création d'une matrice d'incidence à partir d'une matrice d'adjacence carrée.
        """
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
        """
        Teste la création d'une matrice d'incidence à partir d'une matrice d'adjacence carrée.
        """
        adj_matrix = np.array([[0, 1, 1],
                                [1, 0, 0],
                                [1, 0, 0]])
        incidence_matrix = matriceIncidence(adj_matrix)
        expected_result = np.array([[1, 1],
                                    [-1, 0],
                                    [0, -1]])
        self.assertTrue(np.array_equal(incidence_matrix, expected_result))

    def test_non_square_matrix(self):
        """
        Teste la création d'une matrice d'incidence à partir d'une matrice d'adjacence non carrée.
        """
        adj_matrix = np.array([[0, 1],
                                [1, 0],
                                [1, 0]])
        result = matriceIncidence(adj_matrix)
        self.assertEqual(result, None)

    def test_symmetric_matrix(self):
        """
        Teste la création d'une matrice d'incidence à partir d'une matrice d'adjacence symétrique.
        """
        adj_matrix = np.array([[0, 1, 1],
                                [1, 0, 1],
                                [1, 1, 0]])
        incidence_matrix = matriceIncidence(adj_matrix)
        expected_result = np.array([[1, 1, 1],
                                    [-1, -1, -1],
                                    [0, 0, 0]])
        self.assertTrue(np.array_equal(incidence_matrix, expected_result))

    def test_asymmetric_matrix(self):
        """
        Teste la création d'une matrice d'incidence à partir d'une matrice d'adjacence asymétrique.
        """
        adj_matrix = np.array([[0, 1, 0],
                                [0, 0, 1],
                                [0, 0, 0]])
        incidence_matrix = matriceIncidence(adj_matrix)
        expected_result = np.array([[1, 1],
                                    [-1, 0],
                                    [0, -1]])
        self.assertTrue(np.array_equal(incidence_matrix, expected_result))

if __name__ == '__main__':
    unittest.main()
