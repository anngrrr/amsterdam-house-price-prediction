import pandas as pd
from geopy.distance import distance

def create_house_age(df: pd.DataFrame, year_column: str = "year_built") -> pd.DataFrame:
    """Добавляет колонку 'house_age' на основе указанного года постройки"""
    current_year = pd.Timestamp.now().year
    df["house_age"] = current_year - df[year_column]
    return df

def add_price_per_sqm(df: pd.DataFrame, price_col: str = "price", area_col: str = "area") -> pd.DataFrame:
    """Добавляет колонку 'price_per_sqm' на основе цены и площади"""
    df["price_per_sqm"] = df[price_col] / df[area_col]
    return df

def add_area_per_room(df, area_col="area", rooms_col="rooms"):
    """Добавляет колонку 'area_per_room' на основе площади и количества комнат"""
    df["area_per_room"] = df[area_col] / df[rooms_col]
    return df

def add_zip_prefix(df, zip_col="zip", n_digits=4):
    """Добавляет колонку 'zip_prefix' с первыми цифрами индекса для группировки по районам"""
    df["zip_prefix"] = df[zip_col].astype(str).str[:n_digits]
    return df

def add_geo_bins(df, lat_col="lat", lon_col="lon", bin_size=0.01):
    """Добавляет колонки 'lat_bin' и 'lon_bin' с округлёнными координатами для пространственной агрегации"""
    df["lat_bin"] = (df[lat_col] / bin_size).round(0) * bin_size
    df["lon_bin"] = (df[lon_col] / bin_size).round(0) * bin_size
    return df

def add_distance_to_center(df, lat_col="lat", lon_col="lon", center_coords=(52.3676, 4.9041)):
    """Добавляет колонку 'distance_to_center_km' с расстоянием до центра города"""
    df["distance_to_center_km"] = df.apply(
        lambda row: distance((row[lat_col], row[lon_col]), center_coords).km,
        axis=1
    )
    return df
