## 📂 `Amsterdam House Price Prediction`

### 🧠 Project Goal

Predict property prices in Amsterdam based on open tabular data.
The project showcases practical mastery of **machine learning**, **data analysis**, **regular feature engineering**, and **visualisation** tools.

This is not just a model; it is a **full pipeline**, from raw data to a visual comparison of models.

---

## 🔍 What the Project Does

| Capability                          | Summary                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------ |
| 📊 **EDA**                          | Feature-rich notebook with plots, head previews, correlations, and trends |
| 🧼 **Data Cleaning**                | Separated into a reusable module                                          |
| 🧪 **Feature Engineering**          | Building age, price per square metre, and more                            |
| 🔧 **Modular Model Training**       | Linear Regression, Ridge, Random Forest, Decision Tree                    |
| 📈 **Result Visualisation**         | Predictions and errors plotted for inspection                             |
| 🌲 **Feature Importance**           | Clear importance plots for every model                                    |
| 💾 **Model Saving**                 | Every model is stored under a unique name                                 |
| ♻ **Data Reuse**                    | Preprocessed data cached and reloaded when needed                         |
| 🧠 **Quality Metrics**              | MAE, RMSE, R² collected in a comparison table                             |

---

## 📁 Project Structure

```
Amsterdam-House-Price-Prediction/
│
├── data/                    # Raw and preprocessed datasets
│   ├── amsterdam.csv        # Original data kept untouched
│   └── cleaned.csv          # Cleaned data saved as pickle/parquet
│
├── models/                  # Serialized trained models
│
├── notebooks/
│   ├── eda.ipynb            # Exploratory analysis with charts
│   └── models_and_experiments.ipynb  # Model training, comparison, and visualisation
│
├── src/
│   ├── preprocessing.py     # Data cleaning and preparation
│   ├── features.py          # Feature generation
│   ├── train.py             # Train a single model
│   ├── evaluate.py          # MAE, RMSE, R² metrics
│   └── utils.py             # Model save/load helpers and utilities
│
└── README.md                # What you're reading right now
```

---

## 📊 Models Used

* `LinearRegression`
* `Ridge(alpha=1.0)`
* `DecisionTreeRegressor (max_depth=5)`
* `RandomForestRegressor (n_estimators=50)`

## 📦 Tech Stack

| Category          | Tools                           |
| ----------------- | ------------------------------- |
| Language          | `Python 3.10+`
| Environment tool  | `uv`
| ML/Regression     | `scikit-learn`
| Data processing   | `pandas`, `numpy`
| Visualisation     | `matplotlib`, `seaborn`
| Model storage     | `joblib` or `pickle`
| Jupyter           | for experiments and visualisation |

---

## 🚀 How to Run

1. Install dependencies with `uv sync`
2. Open `notebooks/eda.ipynb` for analysis and feature engineering
3. Open `notebooks/models_and_experiments.ipynb` for training and visualisation

---

## 🧑‍💻 Author

**Anna Grabetski**
*ML Engineer / Data Scientist*
📫 [LinkedIn](linkedin.com/in/anngrabetski/)
🐍 I love clean code and insightful charts.
