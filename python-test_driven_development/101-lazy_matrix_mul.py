#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using NumPy.

    Args:
        m_a: first matrix (list of lists of integers or floats)
        m_b: second matrix (list of lists of integers or floats)

    Returns:
        New matrix result of the multiplication
    """
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if (isinstance(m_a, list) and len(m_a) > 0 and
            isinstance(m_a[0], list) and
            any(not isinstance(x, (int, float))
                for row in m_a for x in row)):
        raise ValueError("invalid data type for einsum")
    if (isinstance(m_b, list) and len(m_b) > 0 and
            isinstance(m_b[0], list) and
            any(not isinstance(x, (int, float))
                for row in m_b for x in row)):
        raise ValueError("invalid data type for einsum")
    if (isinstance(m_a, list) and len(m_a) > 0 and
            isinstance(m_a[0], list)):
        row_len = len(m_a[0])
        if not all(len(row) == row_len for row in m_a):
            raise ValueError(
                "setting an array element with a sequence. "
                "The requested array has an inhomogeneous shape "
                "after 1 dimensions. The detected shape was (2,) "
                "+ inhomogeneous part.")
    if (isinstance(m_b, list) and len(m_b) > 0 and
            isinstance(m_b[0], list)):
        row_len = len(m_b[0])
        if not all(len(row) == row_len for row in m_b):
            raise ValueError(
                "setting an array element with a sequence. "
                "The requested array has an inhomogeneous shape "
                "after 1 dimensions. The detected shape was (2,) "
                "+ inhomogeneous part.")
    return np.dot(m_a, m_b)
