import os
import pandas as pd
from sklearn.impute import SimpleImputer

def load_data(filepath: str) -> pd.DataFrame:
    """Загружает CSV-файл"""
    return pd.read_csv(filepath)

def preprocess_columns(df: pd.DataFrame, rename_map: dict) -> pd.DataFrame:
    """Приводит заголовки к нижнему регистру и переименовывает колонки по заданному словарю"""
    df.columns = df.columns.str.lower()
    rename_map = {k.lower(): v.lower() for k, v in rename_map.items()}
    df.rename(columns=rename_map, inplace=True)
    return df

def clean_data(df: pd.DataFrame, target_column: str = "price") -> pd.DataFrame:
    """Удаляет строки с пустыми значениями в целевой колонке"""
    return df.dropna(subset=[target_column])

def impute_missing(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Заполняет пропущенные значения медианой"""
    imputer = SimpleImputer(strategy="median")
    df[columns] = imputer.fit_transform(df[columns])
    return df

def save_cleaned_data(df: pd.DataFrame, path: str = "data/cleaned.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

def load_cleaned_data(path: str = "data/cleaned.csv") -> pd.DataFrame:
    return pd.read_csv(path)

def split_data(df: pd.DataFrame, target_column: str):
    """Разделяет датафрейм на признаки и целевую переменную"""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y
