#!/usr/bin/python3
"""Defines matrix multiplication function by using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of 2  matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
