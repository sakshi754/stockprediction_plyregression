# Stock Price Prediction using Polynomial Regression
RUN https://stockpredictionplyregression-3ezmjtf3vvlappgckm3ajws.streamlit.app/

This Streamlit web application predicts stock prices for the next 30 days using **Polynomial Regression**. The user inputs a stock ticker, and the app retrieves historical stock data, applies polynomial regression, and visualizes future price predictions.

## Features
- **User Input:** Enter any stock ticker.
- **Data Retrieval:** Fetches historical stock data using `yfinance`.
- **Polynomial Regression:** Uses machine learning to predict stock prices.
- **Graphical Visualization:** Displays a prediction graph for the next 30 days.

## Installation
To run this app locally, follow these steps:

### **1. Clone the Repository**
```sh
git clone <your-repo-url>
cd stockprediction_polyregression
```

### **2. Set Up a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate it (Mac/Linux)
venv\Scripts\activate  # Activate it (Windows)
```

### **3. Install Dependencies**
Make sure you have **Python 3.x** installed, then run:
```sh
pip install -r requirements.txt
```

## Running the App
Run the following command:
```sh
streamlit run stock.py
```
This will launch the app in your default web browser.

## Deployment on Streamlit Cloud
1. Push the code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and connect your GitHub repo.
3. Select the **branch** and set the main file as `stock.py`.
4. Click **Deploy** and wait for it to be live!

## Requirements
- Python 3.x
- Libraries: `streamlit`, `yfinance`, `numpy`, `pandas`, `matplotlib`, `scikit-learn`

## Troubleshooting
- If `yfinance` is missing, ensure `requirements.txt` is correctly formatted and redeploy.
- If Streamlit fails, check the logs and restart the app.

## Contributing
Feel free to fork this repo and make improvements. Contributions are welcome!

## License
This project is open-source under the MIT License.

