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
    return np.einsum('ij,jk->ik', m_a, m_b)
