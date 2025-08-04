import os
import joblib

def save_model_named(model, name: str, folder: str = "models"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{name}.joblib")
    joblib.dump(model, path)
    print(f"✅ Модель сохранена: {path}")

def load_model_named(name: str, folder: str = "models"):
    path = os.path.join(folder, f"{name}.joblib")
    return joblib.load(path)

def print_evaluation(metrics: dict):
    """Красиво выводит метрики"""
    print("📊 Model Evaluation:")
    for k, v in metrics.items():
        print(f"{k}: {v}")
