# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential # type: ignore
from keras.layers import LSTM, Dense # type: ignore
from sklearn.preprocessing import MinMaxScaler

# Step 2: Load and Prepare Dataset
df = pd.read_csv("data/preprocessed/Dataset.csv")  # Adjust path if needed

# Rename columns for consistency
df.rename(columns={
    "Total Current Annual Ground Water Extraction": "Water_Consumption",
    "Recharge from rainfall During Monsoon Season": "Rainfall",
}, inplace=True)

# Select relevant features
features = ["Water_Consumption", "Rainfall"]
df = df[features]

# Normalize the data
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(df_scaled, columns=df.columns)
# Handle NaN values before creating sequences
df_scaled = df_scaled.dropna()  # Remove rows with NaN values
# OR
df_scaled.fillna(df_scaled.mean(), inplace=True)  # Replace NaNs with mean values


# Step 3: Convert Data into Sequences for LSTM
def create_sequences(data, time_steps=10):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:i+time_steps])
        y.append(data[i+time_steps, 0])  # Predicting "Water_Consumption"
    return np.array(X), np.array(y)

# Convert dataset into time-series sequences
time_steps = 10
X, y = create_sequences(df_scaled.values, time_steps)

# Debugging: Check dataset shapes
print("X shape:", X.shape)  # <-- Add at line ~40
print("y shape:", y.shape)  # <-- Add at line ~41

print("Any NaNs in dataset before training?:", df_scaled.isnull().values.any())

# Split into train and test sets (80% training, 20% testing)
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Debugging: Print training and test set shapes
print("X_train shape:", X_train.shape)  # <-- Add at line ~48
print("y_train shape:", y_train.shape)  # <-- Add at line ~49
print("X_test shape:", X_test.shape)    # <-- Add at line ~50
print("y_test shape:", y_test.shape)    # <-- Add at line ~51

# Step 4: Define and Train the LSTM Model
model = Sequential([
    LSTM(1, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])),
    LSTM(1, return_sequences=False),
    Dense(25),
    Dense(1)
])

# Compile the model
model.compile(optimizer="adam", loss="mse")

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=16, verbose=1)

# Debugging: Print history keys
print("Available history keys:", history.history.keys())  # <-- Add at line ~69

# Save the trained model
model.save("water_forecast_lstm.h5")

# Step 5: Evaluate and Plot Predictions
y_pred = model.predict(X_test)

# Reverse scaling for proper comparison
y_test_actual = scaler.inverse_transform(np.hstack((y_test.reshape(-1,1), np.zeros((y_test.shape[0], 1)))))[:, 0]
y_pred_actual = scaler.inverse_transform(np.hstack((y_pred, np.zeros((y_pred.shape[0], 1)))))[:, 0]

# Debugging: Print first 10 values for verification
print("First 10 actual values:", y_test_actual[:10])  
print("First 10 predicted values:", y_pred_actual[:10])  

# Plot actual vs predicted values
plt.figure(figsize=(10,5))
plt.plot(y_test_actual, label="Actual", linestyle="-", color="blue")
plt.plot(y_pred_actual, label="Predicted", linestyle="dashed", color="orange", marker="o")  # Add markers for visibility
plt.ylim(min(min(y_test_actual), min(y_pred_actual)), max(max(y_test_actual), max(y_pred_actual)))  # Adjust Y-axis
plt.legend()
plt.title("Water Demand Forecasting")
plt.show() 

# Step 6: Plot Loss Curve
if 'loss' in history.history and 'val_loss' in history.history:  # <-- Add at line ~91
    plt.figure(figsize=(8,4))
    plt.plot(history.history['loss'], label='Training Loss', color='blue')
    plt.plot(history.history['val_loss'], label='Validation Loss', color='red')
    plt.legend()
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.title("Loss Curve")
    plt.grid()
    plt.show()
else:
    print("Loss values not found in history. Check training process!")
