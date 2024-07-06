------MedInsight Pro - Disease Prediction and Information Center
MedInsight Pro is a web-based application developed using Streamlit that predicts the risk of three diseases: Diabetes, Heart Disease, and Parkinson's Disease. This application uses pre-trained machine learning models to provide predictions and personalized health recommendations based on user inputs.

----Table of Contents
Features
Installation
Usage
Models
Input Validation
Risk Score Calculation
Personalized Recommendations
Application Pages
Requirements

-----Features
Disease Prediction: Predicts the risk of Diabetes, Heart Disease, and Parkinson's Disease.
Personalized Recommendations: Provides health recommendations based on the prediction results and user inputs.
Educational Information: Offers detailed information about each disease, including causes, precautions, and risk factors.
User-Friendly Interface: Interactive and easy-to-use web interface developed using Streamlit.
Installation
To install and run this application locally, follow these steps:

----Clone this repository:

git clone [https://github.com/your-username/medinsight-pro.git](https://github.com/SaiNagaAnirudh13/MedInsight-Pro)
cd medinsight-pro

----Install the required packages:

pip install -r requirements.txt

-----Run the Streamlit application:

streamlit run app.py

-----Usage

Open the web application in your browser (usually http://localhost:8501).

Navigate through the main page to read about each disease.

Click the buttons to proceed to the prediction page for the desired disease.

Fill in the required input fields and submit the form to get the prediction results and personalized recommendations.

------Models

The application uses pre-trained machine learning models stored as .sav files. The models are loaded at the start of the application:

with open('path_to_model/diabetes_model.sav', 'rb') as f:
    diabetes_model = pickle.load(f)
with open('path_to_model/heart_disease_model.sav', 'rb') as f:
    heart_disease_model = pickle.load(f)
with open('path_to_model/parkinsons_model.sav', 'rb') as f:
    parkinsons_model = pickle.load(f)
    
------Input Validation
The input validation function ensures that all inputs are numeric and valid:

def validate_input(inputs):
    try:
        inputs = [float(x) if isinstance(x, (int, float)) else x for x in inputs]
        return inputs
    except ValueError as e:
        st.error(f"Input error: {e}. Please enter valid numeric values.")
        return None
}

-----Risk Score Calculation
The risk score is calculated based on the validated inputs:

def calculate_risk_score(model, validated_input):
    risk_score = sum(validated_input) / len(validated_input)
    return risk_score

    
-----Personalized Recommendations
Recommendations are provided based on the prediction results and user inputs:

def provide_recommendations(model, prediction_result, user_input):
    recommendations = ""
    if model == diabetes_model:
        if prediction_result == 1:
            if user_input[1] > 140:
                recommendations += "Monitor and control your glucose levels more closely, as high glucose levels increase the risk of complications.\n"
            # Additional recommendations...
    elif model == heart_disease_model:
        # Recommendations for heart disease...
    elif model == parkinsons_model:
        # Recommendations for Parkinson's disease...
    return recommendations

    
-----Application Pages
Main Page
The main page provides information about each disease and buttons to navigate to the prediction pages.

Disease Prediction Pages
Each disease prediction page collects user inputs, validates them, and uses the corresponding model to make predictions. The results are displayed along with a risk score and personalized recommendations.

-----Requirements

Python 3.7 or higher
Streamlit 1.21.0
Scikit-learn 1.3.0
Pandas 2.1.1
Numpy 1.25.0
