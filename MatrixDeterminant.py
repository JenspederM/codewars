__doc__ = """

Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

A 1x1 matrix |a| has determinant a.

A 2x2 matrix [ [a, b], [c, d] ] or

|a  b|
|c  d|

has determinant: a*d - b*c.

The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants of n matrices ofn-1 x n-1 size.

For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

|a b c|  
|d e f|  
|g h i| 

the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs:

|- - -|
|- e f|
|- h i|  

Note the alternation of signs.

The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], then:

det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
"""


def minor(matrix, row, column):
    """
    Create the minor of a matrix.
    """
    minor_matrix = []
    for i in range(len(matrix)):
        if i != row:
            minor_matrix.append(matrix[i][:])
            minor_matrix[-1].pop(column)
    return minor_matrix


def determinant(matrix):
    """
    Calculate the determinant of a square matrix.
    """
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += matrix[0][i] * (-1) ** i * determinant(minor(matrix, 0, i))
        return det


if __name__ == "__main__":
    print(determinant([[1]]) == 1)
    print(determinant([[1, 3], [2, 5]]) == -1)
    print(determinant([[2, 5, 3], [1, -2, -1], [1, 3, 4]]) == -20)
