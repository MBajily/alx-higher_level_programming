#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list ints/floats): first matrix.
        m_b (list ints/floats): second matrix.
    Raises:
        TypeError: If is not a list of lists of ints/floats.
        TypeError: If is empty.
        TypeError: If has different-sized rows.
        ValueError: If cannot be multiplied.
    Returns:
        A new matrix for the multiplication.
    """
    
    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")

    if (m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    if (not all((isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in m_a for num in row])):
        raise TypeError("m_a should contain only integers or floats")

    if (not all((isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in m_b for num in row])):
        raise TypeError("m_b should contain only integers or floats")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    inv_b = []
    for r in range(len(m_b[0])):
        newRow = []
        for c in range(len(m_b)):
            newRow.append(m_b[c][r])
        inv_b.append(newRow)

    result = []
    for row in m_a:
        result = []
        for col in inv_b:
            prod = 0
            for i in range(len(inv_b[0])):
                prod += row[i] * col[i]
            newRow.append(prod)
        result.append(newRow)

    return result
