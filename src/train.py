from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

def scale_features(X: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Масштабирует числовые признаки"""
    scaler = StandardScaler()
    X[columns] = scaler.fit_transform(X[columns])
    return X

def train_test_split_data(X, y, test_size=0.2, random_state=42):
    """Разделяет выборку"""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
