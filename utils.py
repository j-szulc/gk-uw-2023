import numpy as np


def solve_quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    a = np.broadcast_to(a, delta.shape)
    b = np.broadcast_to(b, delta.shape)

    mask = delta >= 0
    sqrt_delta = np.sqrt(delta[mask])
    roots_minus = np.full_like(delta, np.nan)
    roots_plus = np.full_like(delta, np.nan)
    roots_minus[mask] = (-b[mask] - sqrt_delta) / (2 * a[mask])
    roots_plus[mask] = (-b[mask] + sqrt_delta) / (2 * a[mask])
    return roots_minus, roots_plus
