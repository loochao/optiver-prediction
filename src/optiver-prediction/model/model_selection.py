import numpy as np
import pandas as pd
from sklearn.model_selection import KFold


class GroupKFold:
    """
    GroupKFold with random shuffle with a sklearn-like structure
    """

    def __init__(self, n_splits: int = 5, shuffle: bool = True, random_state: int = 42):
        self.n_splits = n_splits
        self.shuffle = shuffle
        self.random_state = random_state

    def get_n_splits(self, X: pd.DataFrame = None, y: pd.Series = None, group=None):
        return self.n_splits

    def split(self, X: pd.DataFrame, y: pd.Series, group: pd.Series):
        kf = KFold(
            n_splits=self.n_splits, shuffle=self.shuffle, random_state=self.random_state
        )
        unique_ids = group.unique()
        for fold, (tr_group_idx, va_group_idx) in enumerate(kf.split(unique_ids)):
            # split group
            tr_group, va_group = unique_ids[tr_group_idx], unique_ids[va_group_idx]
            train_idx = np.where(group.isin(tr_group))[0]
            val_idx = np.where(group.isin(va_group))[0]
            yield train_idx, val_idx
