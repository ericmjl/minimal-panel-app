import numpy as np

molecular_weights = {
    'A':89.0935,
    'R':174.2017,
    'N':132.1184,
    'D':133.1032,
    'C':121.1590,
    'E':147.1299,
    'Q':146.1451,
    'G':75.0669,
    'H':155.1552,
    'I':131.1736,
    'L':131.1736,
    'K':146.1882,
    'M':149.2124,
    'F':165.1900,
    'P':115.1310,
    'S':105.0930,
    'T':119.1197,
    'W':204.2262,
    'Y':181.1894,
    'V':117.1469,
    'X':100.00
}


def featurize_sequence_(x):
    """x: a string in a pandas DataFrame cell"""
    feats = np.zeros(len(x))
    for i, letter in enumerate(x):
        feats[i] = molecular_weights[letter]
    return feats