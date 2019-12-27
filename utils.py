import numpy as np

molecular_weights = {
    "A": 89.0935,
    "R": 174.2017,
    "N": 132.1184,
    "D": 133.1032,
    "C": 121.1590,
    "E": 147.1299,
    "Q": 146.1451,
    "G": 75.0669,
    "H": 155.1552,
    "I": 131.1736,
    "L": 131.1736,
    "K": 146.1882,
    "M": 149.2124,
    "F": 165.1900,
    "P": 115.1310,
    "S": 105.0930,
    "T": 119.1197,
    "W": 204.2262,
    "Y": 181.1894,
    "V": 117.1469,
    "X": 100.00,
}


def featurize_sequence_(x, expected_size=99):
    """
    :param x: a string in a pandas DataFrame cell
    """
    feats = np.zeros(len(x))
    for i, letter in enumerate(x):
        feats[i] = molecular_weights[letter]
    return feats.reshape(1, -1)


from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score


def fit_model(data, features, target):
    import janitor
    model = RandomForestRegressor(n_estimators=300)
    
    resistance_data = features.join(data[target]).dropna()
    X, y = resistance_data.get_features_targets(target_column_names=target)
    
    model.fit(X, y)
    return model


def cross_validate(data, features, target):
    import janitor
    model = RandomForestRegressor(n_estimators=500)
    
    resistance_data = features.join(data[target]).dropna()
    X, y = resistance_data.get_features_targets(target_column_names=target)
    
    return -cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=5)


class SequenceError(Exception):
    pass

def predict(model, sequence):
    """
    :param model: sklearn model
    :param sequence: A string, should be 99 characters long.
    """
    if len(sequence) != 99:
        raise ValueError(f"sequence must be of length 99. Your sequence is of length {len(sequence)}")
    
    if not set(sequence).issubset(set(molecular_weights.keys())):
        invalid_chars = set(sequence).difference(molecular_weights.keys())
        raise SequenceError(f"sequence contains invalid characters: {invalid_chars}")
    
    seqfeat = featurize_sequence_(sequence)
    return model.predict(seqfeat)
