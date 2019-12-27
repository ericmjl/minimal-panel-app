from utils import featurize_sequence_, molecular_weights, predict
import pytest
from hypothesis import given, strategies as st
import joblib
import gzip
import pickle as pkl

@given(
    st.text(alphabet=list(molecular_weights.keys()), min_size=0, max_size=200)
)
def test_featurize_sequence_(sequence):
    feats = featurize_sequence_(sequence)
    assert feats.shape[-1] == len(sequence)


@given(sequence=st.text(alphabet=list(molecular_weights.keys()), min_size=99, max_size=99))
def test_predict(sequence):
    """
    Baseline test that under ideal situations,
    i.e. len(sequence) == 99 and
    set(sequence).issubset(molecular_weights.keys()),
    that the function executes correctly.
    """
    with gzip.open("data/models/ATV.pkl.gz", "rb") as f:
        model = pkl.load(f)

    preds = predict(model, sequence)