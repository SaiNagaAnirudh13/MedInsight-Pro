import streamlit as st
import pickle

# Load models (Replace with your model paths)
with open(r'C:/Users/aniru/OneDrive/Desktop/multiple disease/saved models/diabetes_model (1).sav', 'rb') as f:
    diabetes_model = pickle.load(f)
with open(r'C:/Users/aniru/OneDrive/Desktop/multiple disease/saved models/heart_disease_model (1).sav', 'rb') as f:
    heart_disease_model = pickle.load(f)
with open(r'C:/Users/aniru/OneDrive/Desktop\/multiple disease/saved models/parkinsons_model (1).sav', 'rb') as f:
    parkinsons_model = pickle.load(f)

# Function to validate input
def validate_input(inputs):
    try:
        inputs = [float(x) if isinstance(x, (int, float)) else x for x in inputs]
        return inputs
    except ValueError as e:
        st.error(f"Input error: {e}. Please enter valid numeric values.")
        return None

# Function to calculate risk score
def calculate_risk_score(model, validated_input):
    # Replace with appropriate logic
    risk_score = sum(validated_input) / len(validated_input)
    return risk_score

# Function to provide personalized recommendations
def provide_recommendations(model, prediction_result, user_input):
    recommendations = ""

    if model == diabetes_model:
        if prediction_result == 1:
            if user_input[1] > 140:
                recommendations += "Monitor and control your glucose levels more closely, as high glucose levels increase the risk of complications.\n"
            if user_input[5] > 30:
                recommendations += "Focus on maintaining a healthy BMI with proper diet and exercise, as obesity is a risk factor for diabetes.\n"
            if user_input[7] > 40:
                recommendations += "Regularly check your blood pressure and maintain it within healthy ranges to reduce cardiovascular risks.\n"
        else:
            if user_input[1] < 100:
                recommendations += "Monitor your glucose levels to ensure they do not drop too low, especially if you are at risk of hypoglycemia.\n"
            if user_input[5] < 18.5:
                recommendations += "Ensure you are getting enough nutrients and consider consulting a nutritionist to maintain a healthy weight.\n"

    elif model == heart_disease_model:
        if prediction_result == 1:
            if user_input[3] > 140:
                recommendations += "Keep a close watch on your blood pressure and consult with a healthcare provider to manage hypertension.\n"
            if user_input[8] == 1:
                recommendations += "If you experience exercise-induced angina, consider adjusting your physical activity levels and consulting with a cardiologist.\n"
        else:
            if user_input[7] > 150:
                recommendations += "Ensure you are exercising within safe heart rate zones, and consult with a fitness trainer for personalized exercise recommendations.\n"
            if user_input[10] == 2:
                recommendations += "If you notice a downsloping ST segment during exercise, discuss this with a healthcare provider to monitor any potential heart issues.\n"

    elif model == parkinsons_model:
        if prediction_result == 1:
            if user_input[0] > 200:
                recommendations += "Monitor changes in your voice frequency (Fo) closely, as increases may indicate progression of Parkinson's disease.\n"
            if user_input[10] > 0.1:
                recommendations += "Manage and monitor any increases in Shimmer:APQ3, as it can indicate changes in vocal stability associated with Parkinson's.\n"
        else:
            if user_input[2] < 70:
                recommendations += "Consider exercises or therapies that can help maintain vocal stability and clarity, which may reduce risks associated with vocal abnormalities.\n"
            if user_input[20] < 0.1:
                recommendations += "Maintain your PPE score to minimize the risk of speech deterioration, which can affect communication abilities.\n"

    return recommendations

# Function to render the main page with disease information
def render_main_page():
    st.title("Welcome to MedInsight Pro - Disease Prediction and Information Center")
    st.markdown("---")

    st.header("About Heart Disease")
    st.write("""
    Heart disease refers to a range of conditions that affect your heart. Common types include coronary artery disease, heart attack, and heart failure. 
    Here are some details:
    - **Causes**: Factors such as high blood pressure, high cholesterol, smoking, diabetes, family history, and unhealthy diet.
    - **Precautions**: Regular exercise, balanced diet, quitting smoking, managing stress, and regular health check-ups.
    - **Risks**: Increased risk with age, family history, unhealthy lifestyle, and underlying health conditions.
    """)
    if st.button("Proceed to Heart Disease Prediction"):
        st.session_state['page'] = 'Heart Disease'

    st.markdown("---")
    
    st.header("About Diabetes")
    st.write("""
    Diabetes mellitus is a chronic condition that affects how your body turns food into energy. 
    Here are some details:
    - **Causes**: Insufficient insulin production (Type 1), insulin resistance (Type 2), genetics, and lifestyle factors.
    - **Precautions**: Healthy eating, regular physical activity, monitoring blood sugar levels, and medication as prescribed.
    - **Risks**: Increased risk with obesity, sedentary lifestyle, family history, and age.
    """)
    if st.button("Proceed to Diabetes Prediction"):
        st.session_state['page'] = 'Diabetes'

    st.markdown("---")

    st.header("About Parkinson's Disease")
    st.write("""
    Parkinson's disease is a progressive nervous system disorder that affects movement. 
    Here are some details:
    - **Causes**: Loss of nerve cells in the brain that produce dopamine, genetic factors, and environmental triggers.
    - **Precautions**: Regular exercise, balanced diet, maintaining mental health, and medication to manage symptoms.
    - **Risks**: Higher risk with age, family history, exposure to toxins, and certain genetic mutations.
    """)
    if st.button("Proceed to Parkinson's Disease Prediction"):
        st.session_state['page'] = 'Parkinsons'

# Function to render the disease prediction pages
def render_disease_prediction(selected):
    if selected == 'Diabetes':
        st.subheader('Diabetes Prediction')

        # Input fields
        with st.form(key='diabetes_form'):
            Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
            Glucose = st.number_input('Glucose Level', min_value=0)
            BloodPressure = st.number_input('Blood Pressure value', min_value=0)
            SkinThickness = st.number_input('Skin Thickness value', min_value=0)
            Insulin = st.number_input('Insulin Level', min_value=0)
            BMI = st.number_input('BMI value', min_value=0.0, step=0.1)
            DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, max_value=2.0, step=0.01)
            Age = st.number_input('Age of the Person', min_value=0)

            if st.form_submit_button('Diabetes Test Result'):
                user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
                validated_input = validate_input(user_input)

                if validated_input:
                    diab_prediction = diabetes_model.predict([validated_input])
                    if diab_prediction[0] == 1:
                        st.success('The person is diabetic')
                    else:
                        st.success('The person is not diabetic')

                    # Calculate and display risk score
                    risk_score = calculate_risk_score(diabetes_model, validated_input)
                    if risk_score is not None:
                        st.info(f'Diabetes Risk Score: {risk_score:.2f}')

                    # Provide personalized recommendations
                    recommendations = provide_recommendations(diabetes_model, diab_prediction[0], validated_input)
                    if recommendations:
                        st.info(recommendations)

        # Back to main page button
        if st.button('Back to Main Page'):
            st.session_state['page'] = 'Main'

    elif selected == 'Heart Disease':
        st.subheader('Heart Disease Prediction')

        # Input fields
        with st.form(key='heart_disease_form'):
            age = st.number_input('Age', min_value=0)
            sex = st.selectbox('Sex', ['Male', 'Female'])
            cp = st.selectbox('Chest Pain types', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
            trestbps = st.number_input('Resting Blood Pressure', min_value=0)
            chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0)
            fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['True', 'False'])
            restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'])
            thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0)
            exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
            oldpeak = st.number_input('ST depression induced by exercise relative to rest', min_value=0.0, step=0.1)
            slope = st.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])
            ca = st.number_input('Major vessels colored by flourosopy', min_value=0, max_value=4, step=1)
            thal = st.selectbox('Thalium Stress Test Result', ['Normal', 'Fixed defect', 'Reversible defect'])

            if st.form_submit_button('Heart Disease Test Result'):
                # Mapping categorical inputs to numerical values
                sex_mapping = {'Male': 1, 'Female': 0}
                cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
                fbs_mapping = {'True': 1, 'False': 0}
                restecg_mapping = {'Normal': 0, 'ST-T wave abnormality': 1, 'Probable or definite left ventricular hypertrophy': 2}
                exang_mapping = {'Yes': 1, 'No': 0}
                slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
                thal_mapping = {'Normal': 0, 'Fixed defect': 1, 'Reversible defect': 2}

                user_input = [
                    age, 
                    sex_mapping[sex], 
                    cp_mapping[cp], 
                    trestbps, 
                    chol, 
                    fbs_mapping[fbs], 
                    restecg_mapping[restecg], 
                    thalach, 
                    exang_mapping[exang], 
                    oldpeak, 
                    slope_mapping[slope], 
                    ca, 
                    thal_mapping[thal]
                ]

                validated_input = validate_input(user_input)

                if validated_input:
                    heart_disease_prediction = heart_disease_model.predict([validated_input])
                    if heart_disease_prediction[0] == 1:
                        st.success('The person has heart disease')
                    else:
                        st.success('The person does not have heart disease')

                    # Calculate and display risk score
                    risk_score = calculate_risk_score(heart_disease_model, validated_input)
                    if risk_score is not None:
                        st.info(f'Heart Disease Risk Score: {risk_score:.2f}')

                    # Provide personalized recommendations
                    recommendations = provide_recommendations(heart_disease_model, heart_disease_prediction[0], validated_input)
                    if recommendations:
                        st.info(recommendations)

        # Back to main page button
        if st.button('Back to Main Page'):
            st.session_state['page'] = 'Main'

    elif selected == 'Parkinsons':
        st.subheader("Parkinson's Disease Prediction")

        # Input fields
        with st.form(key='parkinsons_form'):
            fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, max_value=300.0, step=0.1)
            fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, max_value=300.0, step=0.1)
            flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, max_value=300.0, step=0.1)
            Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, max_value=1.0, step=0.01)
            Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, max_value=0.1, step=0.001)
            RAP = st.number_input('MDVP:RAP', min_value=0.0, max_value=1.0, step=0.01)
            PPQ = st.number_input('MDVP:PPQ', min_value=0.0, max_value=1.0, step=0.01)
            DDP = st.number_input('Jitter:DDP', min_value=0.0, max_value=3.0, step=0.01)
            Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, max_value=1.0, step=0.01)
            Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, max_value=2.0, step=0.1)
            APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, max_value=1.0, step=0.01)
            APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, max_value=1.0, step=0.01)
            APQ = st.number_input('MDVP:APQ', min_value=0.0, max_value=1.0, step=0.01)
            DDA = st.number_input('Shimmer:DDA', min_value=0.0, max_value=3.0, step=0.01)
            NHR = st.number_input('NHR', min_value=0.0, max_value=1.0, step=0.01)
            HNR = st.number_input('HNR', min_value=0.0, max_value=40.0, step=0.1)
            RPDE = st.number_input('RPDE', min_value=0.0, max_value=1.0, step=0.01)
            DFA = st.number_input('DFA', min_value=0.0, max_value=2.0, step=0.01)
            spread1 = st.number_input('spread1', min_value=-20.0, max_value=0.0, step=0.1)
            spread2 = st.number_input('spread2', min_value=0.0, max_value=0.5, step=0.01)
            D2 = st.number_input('D2', min_value=0.0, max_value=5.0, step=0.01)
            PPE = st.number_input('PPE', min_value=0.0, max_value=1.0, step=0.01)

            if st.form_submit_button("Parkinson's Test Result"):
                user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
                validated_input = validate_input(user_input)

                if validated_input:
                    parkinsons_prediction = parkinsons_model.predict([validated_input])
                    if parkinsons_prediction[0] == 1:
                        st.success("The person has Parkinson's disease")
                    else:
                        st.success("The person does not have Parkinson's disease")

                    # Calculate and display risk score
                    risk_score = calculate_risk_score(parkinsons_model, validated_input)
                    if risk_score is not None:
                        st.info(f"Parkinson's Disease Risk Score: {risk_score:.2f}")

                    # Provide personalized recommendations
                    recommendations = provide_recommendations(parkinsons_model, parkinsons_prediction[0], validated_input)
                    if recommendations:
                        st.info(recommendations)

        # Back to main page button
        if st.button('Back to Main Page'):
            st.session_state['page'] = 'Main'

# Main logic to handle page states
if 'page' not in st.session_state:
    st.session_state['page'] = 'Main'

if st.session_state['page'] == 'Main':
    render_main_page()
elif st.session_state['page'] == 'Diabetes':
    render_disease_prediction('Diabetes')
elif st.session_state['page'] == 'Heart Disease':
    render_disease_prediction('Heart Disease')
elif st.session_state['page'] == 'Parkinsons':
    render_disease_prediction('Parkinsons')
