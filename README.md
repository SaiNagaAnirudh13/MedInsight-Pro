🌟 MedInsight Pro - Disease Prediction and Information Center 🌟(https://medinsight-pro-5.onrender.com/)

MedInsight Pro is a web-based application developed using Streamlit that predicts the risk of three diseases: Diabetes, Heart Disease, and Parkinson's Disease. This application uses pre-trained machine learning models to provide predictions and personalized health recommendations based on user inputs.

🌟 Features

Disease Prediction: Predicts the risk of Diabetes, Heart Disease, and Parkinson's Disease.

Personalized Recommendations: Provides health recommendations based on the prediction results and user inputs.

Educational Information: Offers detailed information about each disease, including causes, precautions, and risk factors.

User-Friendly Interface: Interactive and easy-to-use web interface developed using Streamlit.

🛠️ Installation

To install and run this application locally, follow these steps:

🔧 Clone this repository:

Clone the repository using the command: git clone https://github.com/SaiNagaAnirudh13/MedInsight-Pro

Navigate to the project directory: cd medinsight-pro

📦 Install the required packages:

Run the following command to install the required packages:

pip install -r requirements.txt

🚀 Run the Streamlit application:

Run the following command to start the application:

streamlit run app.py

🖥️ Usage

Open the web application in your browser ([usually http://localhost:8501](https://medinsight-pro-5.onrender.com/)).

Navigate through the main page to read about each disease.

Click the buttons to proceed to the prediction page for the desired disease.

Fill in the required input fields and submit the form to get the prediction results and personalized recommendations.

🔍 Models

The application uses pre-trained machine learning models stored as .sav files. The models are loaded at the start of the application and are used to make predictions for each disease.

✅ Input Validation

Input validation ensures that all inputs are numeric and valid, preventing errors and ensuring accurate predictions.

📊 Risk Score Calculation

The risk score is calculated based on the validated inputs, providing an estimate of the user's risk level for each disease.

💡 Personalized Recommendations

Recommendations are provided based on the prediction results and user inputs. These recommendations help users understand their health risks and provide actionable steps to improve their health.

📄 Application Pages

🏠 Main Page

The main page provides information about each disease and buttons to navigate to the prediction pages.

🔮 Disease Prediction Pages

Each disease prediction page collects user inputs, validates them, and uses the corresponding model to make predictions. The results are displayed along with a risk score and personalized recommendations.

📋 Requirements

Python 3.7 or higher

Streamlit 1.21.0

Scikit-learn 1.3.0

Pandas 2.1.1

Numpy 1.25.0
