#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""this for Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): for The first matrix.
        m_b (list of lists of ints/floats): for The second matrix.
    """

    return (np.matmul(m_a, m_b))
