import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Streamlit App Title
st.title("Stock Price Prediction using Polynomial Regression")

# User input for stock ticker
ticker = st.text_input("Enter Stock Ticker:", "AAPL")

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1y")
    return df

if st.button("Predict"):
    # Fetch stock data
    df = fetch_stock_data(ticker)
    df.reset_index(inplace=True)
    df['Days'] = np.arange(len(df))
    
    # Prepare data for polynomial regression
    X = df[['Days']].values
    y = df['Close'].values
    
    poly = PolynomialFeatures(degree=3)
    X_poly = poly.fit_transform(X)
    
    model = LinearRegression()
    model.fit(X_poly, y)
    
    # Predict next 30 days
    future_days = np.arange(len(df), len(df) + 30).reshape(-1, 1)
    future_days_poly = poly.transform(future_days)
    future_prices = model.predict(future_days_poly)
    
    # Plot results
    plt.figure(figsize=(10, 5))
    future_dates = pd.date_range(pd.Timestamp.today(), periods=30, freq='D')
    plt.plot(future_dates, future_prices, label='Predicted Prices', linestyle='dashed', color='red')
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.title(f"Stock Price Prediction for {ticker} (Next 30 Days)")
    plt.legend()
    
    # Display plot in Streamlit
    st.pyplot(plt)
