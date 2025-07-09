import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle
import numpy as np

def train_and_save_model():
    df = pd.read_csv("student-mat.csv", sep=";")

    # Select features and target
    features = ["studytime", "absences", "G1", "G2"]
    target = "G3"

    X = df[features]
    y = df[target]

    # Save input data for reference
    X.to_csv("train_features.csv", index=False)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluation
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Model Evaluation Metrics:")
    print(f"R² Score (Accuracy): {r2:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")

    # Save model
    with open("regressor.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_and_save_model()
