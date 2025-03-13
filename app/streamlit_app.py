import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import matplotlib.pyplot as plt

# Load model
model = joblib.load("model.pkl")

st.set_page_config(page_title="🎮 Time Series Forecast", layout="centered")

# Ribbon tabs
tabs = st.tabs(["🏠 Home", "📊 Forecast", "📁 View Data", "📝 Help", "📬 Contact"])

with tabs[0]:
    st.title("🎮 Video Game Sales Forecast App")
    st.write("Welcome to the Sales Forecast App!")
    st.image("logo.jpg", width=120)
    st.markdown("""
    This application helps you:
    - Upload sales data
    - Forecast future monthly sales
    - Visualize trends & download reports
    """)

with tabs[1]:
    st.subheader("📈 Forecast Generation")
    periods = st.slider("Select Forecast Months", 1, 12, 4)

    if st.button("Generate Forecast"):
        future_dates = pd.date_range(start=datetime.today(), periods=periods, freq='MS')
        forecast = model.forecast(steps=periods)
        forecast_df = pd.DataFrame({
            "Month": future_dates.strftime("%Y-%m"),
            "Forecasted Sales": forecast
        })
        st.dataframe(forecast_df)

        st.line_chart(forecast_df.set_index("Month"))

        # Export Downloads
        st.download_button("📥 Download Forecast CSV", forecast_df.to_csv(index=False), "forecast.csv", "text/csv")

with tabs[2]:
    st.subheader("📁 View Sample Forecast Data")
    forecast_sample = pd.read_csv("ets_forecast.csv")
    st.dataframe(forecast_sample)

with tabs[3]:
    st.subheader("📝 Help")
    st.markdown("""
    - 📌 Use **Forecast tab** to generate prediction.
    - 📁 Check **View Data** tab for sample outputs.
    - 📬 Send queries through Contact tab.
    """)

with tabs[4]:
    st.subheader("📬 Contact / Feedback")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Your Message")
    if st.button("Submit Feedback"):
        with open("app/contact_submissions.txt", "a") as f:
            f.write(f"{datetime.now()} | {name} | {email} | {message}\n")
        st.success("Feedback submitted successfully!")
