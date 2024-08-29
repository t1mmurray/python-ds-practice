def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    n = len(matrix)  # Number of rows (or columns) in the square matrix
    
    top_left_to_bottom_right = 0
    top_right_to_bottom_left = 0
    
    for i in range(n):
        top_left_to_bottom_right += matrix[i][i]  # Elements from top-left to bottom-right
        top_right_to_bottom_left += matrix[i][n - 1 - i]  # Elements from top-right to bottom-left
    
    return top_left_to_bottom_right + top_right_to_bottom_left

# # Example square matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Get the sums of the diagonals
# sum_diag1, sum_diag2 = diagonal_sums(matrix)
# print("Sum of top-left to bottom-right diagonal:", sum_diag1)  # Output: 15
# print("Sum of top-right to bottom-left diagonal:", sum_diag2)  # Output: 15