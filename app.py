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

st.sidebar.markdown("---")
st.sidebar.subheader("Forecast Scenario Inputs")
# Independent input variables for the forecast
# Note: Year and Month will be generated from future dates.
dayofweek_input = st.sidebar.selectbox("Day of Week (0=Monday, 6=Sunday)", list(range(7)), index=0)
promotion_input = st.sidebar.checkbox("Promotion Active?", value=False)
holiday_input = st.sidebar.checkbox("Holiday Month?", value=False)
category_input = st.sidebar.selectbox("Game Category", ["Sports", "RPG", "Simulation", "FPS", "Adventure"])
platform_input = st.sidebar.selectbox("Platform", ["Xbox", "PlayStation", "Nintendo", "PC"])

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
    
    # Generate future dates (forecast horizon)
    forecast_steps = forecast_horizon
    future_dates = pd.date_range(start=datetime.datetime.today() + pd.DateOffset(months=1), periods=forecast_steps, freq='MS')
    
    # Create a DataFrame for forecast inputs
    # Year and Month are derived from the forecast dates.
    forecast_inputs = pd.DataFrame({
        "Year": future_dates.year,
        "Month": future_dates.month,
        "DayOfWeek": [dayofweek_input] * forecast_steps,
        "Promotion": [int(promotion_input)] * forecast_steps,
        "Holiday": [int(holiday_input)] * forecast_steps,
        "Category": [category_input] * forecast_steps,
        "Platform": [platform_input] * forecast_steps
    }, index=future_dates)
    
    st.write("### Forecast Scenario Inputs")
    st.dataframe(forecast_inputs)
    
    # Ensure categorical columns are strings for one-hot encoding
    forecast_inputs["Category"] = forecast_inputs["Category"].astype(str)
    forecast_inputs["Platform"] = forecast_inputs["Platform"].astype(str)
    
    # Perform basic one-hot encoding on 'Category' and 'Platform'
    forecast_encoded = pd.get_dummies(forecast_inputs, columns=["Category", "Platform"], drop_first=True)
    
    # Reset index to remove the datetime index (which otherwise becomes an 'index' column)
    forecast_encoded = forecast_encoded.reset_index(drop=True)
    # Ensure no stray datetime columns remain
    if "index" in forecast_encoded.columns:
        forecast_encoded.drop("index", axis=1, inplace=True)
    
    # Load the model's expected feature list (assume we saved it during training)
    try:
        with open("models/feature_columns.pkl", "rb") as f:
            model_features = pickle.load(f)
    except Exception as e:
        st.warning("Feature columns file not found. Using the current encoded features.")
        model_features = forecast_encoded.columns.tolist()
    
    # Ensure forecast_encoded has all required features (fill missing with 0)
    for col in model_features:
        if col not in forecast_encoded.columns:
            forecast_encoded[col] = 0
    # Order the DataFrame columns to match training
    forecast_encoded = forecast_encoded[model_features]
    
    # Forecasting – assumes the loaded model has a .predict() method
    try:
        forecast_values = model.predict(forecast_encoded)
        # Create a DataFrame to hold forecast results using the original future_dates
        forecast_df = pd.DataFrame({
            "Forecasted Sales": forecast_values
        }, index=future_dates)
        
        st.write(f"### Forecast for Next {forecast_horizon} Months:")
        st.dataframe(forecast_df)
        
        # Plot the forecast results
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(forecast_df.index, forecast_df["Forecasted Sales"], marker="o", linestyle="-", color="red", label="Forecast")
        ax.set_title("Forecasted Video Game Sales")
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales")
        ax.legend()
        # Format x-axis to show Month and Year only
        ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))
        plt.xticks(rotation=45)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error during forecasting: {e}")

# Main dashboard display
st.write("## Video Game Sales Forecasting Analysis Dashboard")
st.markdown("""
This dashboard provides insights into historical video game sales and allows you to forecast future sales using various time series models.  
**Instructions:**
- Use the sidebar to select a forecasting model and set your forecast horizon.
- Input the independent variables (Day of Week, Promotion, Holiday, Category, Platform) that define your forecast scenario.
- Click **Run Forecast** to view predictions and interactive charts.
""")
