# 🌊 Water Demand Forecasting Using LSTM

This project predicts **annual groundwater consumption** using an LSTM (Long Short-Term Memory) neural network. It leverages historical data including **rainfall patterns** to forecast future water consumption trends — a critical application for sustainable water resource management.

---

## 📁 Dataset

- Source: `data/preprocessed/Dataset.csv`
- Features used:
  - `Water_Consumption`: Total current annual groundwater extraction
  - `Rainfall`: Recharge from rainfall during the monsoon season

---

## 🔧 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn (MinMaxScaler)
- TensorFlow / Keras
- Matplotlib

---

## 📈 Model Overview

An LSTM-based sequential model is used with the following structure:

```text
Input → LSTM(1, return_sequences=True) → LSTM(1) → Dense(25) → Dense(1)
