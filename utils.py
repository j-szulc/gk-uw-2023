from imports import *



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

def get_not_nan(arr):
    return arr[~np.isnan(arr)]

def add_respecting_nans(arr1, arr2):
    """
    :param arr1: N, M
    :param arr2: N, M
    :return: Result of addition, where NaNs are treated as zero. Result has NaN iff both arrays have NaN at that position.
    """
    nans_1 = np.isnan(arr1)
    nans_2 = np.isnan(arr2)
    arr1[nans_1 & ~nans_2] = 0
    arr2[~nans_1 & nans_2] = 0
    return arr1 + arr2

def reflect(v, n):
    """
    :param v: N, 3
    :param n: N, 3
    :return: N, 3
    """
    return v - 2 * np.sum(v * n, axis=1, keepdims=True) * n

def project(v, n):
    """
    :param v: N, 3
    :param n: N, 3, normalized
    :return: N, 3
    """
    return np.sum(v * n, axis=1, keepdims=True) * n
