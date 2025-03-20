# project3_timeseries

# 🎮 Time Series Forecasting: Video Game Sales Forecast Dashboard

Welcome to the **Video Game Sales Forecasting** project repository!  
This project leverages **Time Series Analysis & Machine Learning** models to **forecast monthly sales of video games**, empowering data-driven inventory planning and strategic decision-making.

---

## 📌 Project Objectives
- Analyze historical video game sales data.
- Forecast future sales using Time Series models: **ARIMA, SARIMA, Holt-Winters (ETS), and SES**.
- Build and deploy a **Streamlit dashboard app** for interactive forecasting and scenario analysis.

---

## 📂 Repository Structure
├── app.py # Streamlit dashboard application 

├── notebook.ipynb # Jupyter notebook for modeling & EDA 

├── models/ │

├── arima_model.pkl │ 

├── hw_model.pkl │

├── ses_model.pkl │

├── sarima_model.pkl │

└── feature_columns.pkl # Feature list used by ML models 

├── data/ │

└── video_game_sales.csv # Original dataset

├── setup.sh # Heroku/Streamlit setup file 

├── requirements.txt # Python dependencies 

├── Procfile # Deployment configuration for Heroku 

├── runtime.txt # Python runtime version 

└── README.md # Documentation guide


---

## 🚀 Live Application Deployment

👉 **Streamlit App:** [Click here to access the dashboard](https://app-url.streamlit.app)

📁 **Presentation Slides:** [Presentation Link](https://docs.google.com/presentation/d/1T1R03PfBVLdO4LheKfUVgDa1RBPbi5ey/edit?usp=sharing&ouid=100420815063974730723&rtpof=true&sd=true)

📄 **Project Documentation:** [Detailed Docs](https://docs.google.com/document/d/1kMVjdIpV878mbpRF_yTIqVGuxLGnRzs1p_bEJGka_Xo/edit?usp=sharing)

---

## 📊 Features of the Dashboard
- **Interactive Forecasting**: Choose forecasting models (ARIMA, SARIMA, SES, Holt-Winters).
- **Custom Scenario Inputs**: Select Day of Week, Holiday, Promotion, Game Category, and Platform.
- **Forecast Horizon**: Predict 1 to 12 months into the future.
- **Dynamic Visualizations**: View line plots of forecasted sales over time.
- **Feature Importance Visualization**: Analyze impact of features using ML models (XGBoost, Random Forest).

---

## 📈 Models Implemented

### Classical Time Series Models:
- **ARIMA** (AutoRegressive Integrated Moving Average)
- **SARIMA** (Seasonal ARIMA)
- **SES** (Simple Exponential Smoothing)
- **Holt-Winters Exponential Smoothing** (Additive & Multiplicative)


All models were evaluated using metrics:
- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Square Error)**
- **R² Score (Coefficient of Determination)**

---

## ⚙️ Installation & Setup Guide

### ✅ Step 1: Clone the Repository

git clone [https://github.com/your-username/video-game-sales-forecast.git](https://github.com/timeseriesgp3/project3_timeseries.git)
cd video-game-sales-forecast

### ✅ Step 2: Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### ✅ Step 3: Install Dependencies

pip install -r requirements.txt

### ✅ Step 4: Run the Streamlit App Locally

streamlit run app.py

### 🌍 Deployment (Streamlit Cloud or Heroku)
For deployment:

Ensure setup.sh, Procfile, and runtime.txt are included.
Push to a Heroku-connected GitHub repo.
Set web: streamlit run app.py in Procfile.

### Recommendation
- Implement **machine learning forecasting models** such as **Random Forest, Decision Trees, and XGBoost** with feature importance.


### 📚 References & Tools
Python, Pandas, Numpy
Matplotlib, Seaborn
Statsmodels
Scikit-learn
Streamlit
MLflow (for tracking & versioning)


### 🤝 Contribution Guide
Want to contribute?
Fork the repository
Create your feature branch git checkout -b feature/new-feature
Commit your changes git commit -m 'Add new feature'
Push to branch git push origin feature/new-feature
Open a Pull Request


### 📜 License
This project is licensed under the MIT License — feel free to use and modify it.

### 📬 Contact & Support
💬 GitHub Issues: Submit your issue here
📧 Email: ibrahim5322022@hotmail.com
