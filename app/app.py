import streamlit as st
import pandas as pd
import numpy as np
import pickle
import mlflow
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration with a title, icon, and layout
st.set_page_config(
    page_title="Video Game Sales Forecasting Dashboard",
    page_icon=":video_game:",
    layout="wide"
)

# Sidebar – Logo and Model Selection
st.sidebar.image("logo.jpg", use_column_width=True)
st.sidebar.title("Forecasting Options")

# Dropdown for selecting the forecasting model
model_options = ["ARIMA", "Holt-Winters (ETS)", "SES", "SARIMA"]
selected_model = st.sidebar.selectbox("Select Forecasting Model", model_options)

# Input for forecast horizon (number of months)
forecast_horizon = st.sidebar.number_input("Forecast Horizon (months)", min_value=1, max_value=12, value=4, step=1)

# Run Forecast Button
if st.sidebar.button("Run Forecast"):
    st.write("### Running Forecast Using **{}** Model".format(selected_model))
    
    # Determine model file path based on selection
    if selected_model == "ARIMA":
        model_file = "models/arima_model.pkl"
    elif selected_model == "Holt-Winters (ETS)":
        model_file = "models/hw_model.pkl"
    elif selected_model == "SES":
        model_file = "models/ses_model.pkl"
    elif selected_model == "SARIMA":
        model_file = "models/sarima_model.pkl"
    else:
        st.error("Selected model is not available.")
    
    # Load the pickled model
    try:
        with open(model_file, "rb") as f:
            model = pickle.load(f)
        st.success("Model loaded successfully!")
    except Exception as e:
        st.error(f"Error loading model: {e}")
    
    # Forecasting – assumes the model has a .forecast() method
    try:
        forecast = model.forecast(steps=forecast_horizon)
        forecast_index = pd.date_range(start=datetime.datetime.today(), periods=forecast_horizon+1, freq='M')[1:]
        forecast_df = pd.DataFrame({"Forecast": forecast}, index=forecast_index)
        
        st.write(f"### Forecast for Next {forecast_horizon} Months:")
        st.dataframe(forecast_df)
        
        # Plot the forecast results
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(forecast_df.index, forecast_df["Forecast"], marker="o", linestyle="-", color="red", label="Forecast")
        ax.set_title("Forecasted Video Game Sales")
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales")
        ax.legend()
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error during forecasting: {e}")

# Main dashboard display
st.write("## Video Game Sales Forecasting Analysis Dashboard")
st.markdown("""
This dashboard provides insights into historical video game sales and allows you to forecast future sales using various time series models. The models (ARIMA, Holt-Winters, SES, SARIMA) were developed and tracked using **MLflow**.

**Instructions:**
- Use the sidebar to select a forecasting model.
- Adjust the forecast horizon.
- Click "Run Forecast" to view predictions and charts.
""")

# (Optional) Additional dashboard elements, interactive charts, or MLflow model metrics can be added here.
