import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

data_path = "train/"

def load_data(data_path):
    data = []
    for filename in os.listdir(data_path):
        if filename.endswith("_scaled.txt"):
            filepath = os.path.join(data_path, filename)
            df = pd.read_csv(filepath, header=None)
            data.append(df)
    return pd.concat(data, axis=0, ignore_index=True)

if __name__ == '__main__':
    data = load_data(data_path)

    X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :-1], data.iloc[:, -1], test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print("MSE:", mse)

    joblib.dump(model, "model.joblib")