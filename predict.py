import streamlit as st
import about, contact, dashboard, predict, logout, mimo
import time
import joblib
import pandas as pd
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.colored_header import colored_header
from sklearn.impute import SimpleImputer

def prediction_page():
    
    data = pd.read_csv('new_cardio.csv', sep=',')
    cvd_model = joblib.load("model.pkl")
    
    # Add custom CSS
    with open('css\predict.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.markdown("<h2 style = 'width:65pc; text-align:center; margin-top:-5pc; color: white; margin-left: 3pc;'>CARDIOVASCULAR RISK DETECTION</h2>", unsafe_allow_html=True)
    st.markdown("<hr style = 'width:65pc; border-width: 3px; margin-top: -1px; background-color: white; margin-left: 3pc;'>", unsafe_allow_html=True)
    
    #objective features
    def map_gender(gender_str):
        if gender_str == "Male":
            return 0
        elif gender_str == "Female":
            return 1
        else:
            return None
        
    def map_chol(chol_str):
        if chol_str == "Normal":
            return 1
        elif chol_str == "Above Normal":
            return 2
        elif chol_str == "High":
            return 3
        else:
            return None
        
    
    def map_glu(glu_str):
        if glu_str == "Normal":
            return 1
        elif glu_str == "Above Normal":
            return 2
        elif glu_str == "High":
            return 3
        else:
            return None
        
    def map_smoke(smoke_str):
        if smoke_str == "No":
            return 0
        elif smoke_str == "Yes":
            return 1
        else:
            return None
        
    def map_alcohol(alcohol_str):
        if alcohol_str == "No":
            return 0
        elif alcohol_str == "Yes":
            return 1
        else:
            return None
        
    def map_active(active_str):
        if active_str == "No":
            return 0
        elif active_str == "Yes":
            return 1
        else:
            return None
    
    with st.form(key="predicting",clear_on_submit=True):
        st.markdown("<h4 style = 'width:65pc; color: white;margin-left:-3pc; margin-top: -2pc'>Objective Features</h4>", unsafe_allow_html=True)
        col1,col2 = st.columns(2, gap="large")
        with col1:
            gender_text = st.selectbox("Gender",["","Male","Female"], placeholder='Choose an option')
            height = st.text_input("Height (cm)", placeholder='Must be between 55-250cm')
        with col2:
            age = st.number_input("Current Age", max_value=200, placeholder="Must be between 20-65")
            weight = st.text_input("Weight (kg)", placeholder="Must be between 10-200kg")

        st.markdown("<hr style = 'width:65pc; border-width: 1px; background-color: white; margin-left:-3pc'>", unsafe_allow_html=True)
        st.markdown("<h4 style = 'width:65pc; color: white; margin-left:-3pc; margin-top: -1pc'>Examination Features</h4>", unsafe_allow_html=True)
        col3,col4 = st.columns(2)
        with col3:
            sys = st.slider("Systolic BP", min_value=90, max_value=200)
            chol_text = st.selectbox("Cholestorol Level",["","Normal","Above normal", "High"])
        with col4:
            dia = st.slider("Diastolic BP", min_value=60, max_value=130)
            glu_text = st.selectbox("Glucose Level",["","Normal","Above normal", "High"])
            
        st.markdown("<hr style = 'width:65pc; border-width: 1px; background-color: white; margin-left:-3pc'>", unsafe_allow_html=True)
        st.markdown("<h4 style = 'width:65pc; color: white; margin-left:-3pc; margin-top:-1pc'>Subjective Features</h4>", unsafe_allow_html=True)
        smoke_text = st.radio("Do you smoke regularly?",["No","Yes"], horizontal=True, index=None)
        alcohol_text = st.radio("Do you often consume alcohol?",["No","Yes"], horizontal=True, index=None)
        active_text = st.radio("Are you physically active?",["No","Yes"], horizontal=True, index=None)
        with stylable_container(
            key="bmi",
            css_styles="""
                {
                    margin-left: -6pc
                }
            """
        ):
            bmi = st.number_input("BMI",help="multiply your height")
        
        st.markdown("<hr style = 'width:65pc; border-width: 1px; background-color: white; margin-left:-3pc'>", unsafe_allow_html=True)
        st.markdown("<h4 style = 'width:65pc; color: white;margin-left:-3pc; margin-top:-1pc'>Prediction Result</h4>", unsafe_allow_html=True)
        submit = st.form_submit_button("Predict")
        
        #code for prediction
        if ((gender_text is not None) and (height is not None) and (age is not None) and (weight is not None) and \
            (sys is not None) and (chol_text is not None) and (dia is not None) and (glu_text is not None) and (smoke_text is not None) and \
            (alcohol_text is not None) and (active_text is not None) and (bmi is not None)):
            
            #map texts to numerical value
            gender = map_gender(gender_text)
            chol = map_chol(chol_text)
            glu = map_glu(glu_text)
            smoke = map_smoke(smoke_text)
            alcohol = map_alcohol(alcohol_text)
            active = map_active(active_text)
            
            cvd_pred = ''
            
            
            if submit:
                progress_text = "Prediction in process... Please wait"
                my_bar = st.progress(0, text=progress_text)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                
                input_table = pd.DataFrame([{'Gender' : gender_text, 'Height':height, 'Age': age, 'Weight': weight, 'Systolic BP': sys,\
                'Cholesterol': chol_text, 'Diastolic BP': dia, 'Glucose': glu_text, 'Smoke': smoke_text, 'Alcohol': alcohol_text, 'Active': active_text, 'BMI': bmi}])
                

                input_var = pd.DataFrame([{'Gender' : gender, 'Height':height, 'Age': age, 'Weight': weight, 'Systolic BP': sys,\
                'Cholesterol': chol, 'Diastolic BP': dia, 'Glucose': glu, 'Smoke': smoke, 'Alcohol': alcohol, 'Active': active, 'BMI': bmi}])
                
                # Impute missing values
                imputer = SimpleImputer(strategy='mean')
                input_data_imputed = imputer.fit_transform(input_var)
                
                tab1, tab2 = st.tabs(["Interpretation", "Result"])
                #interpretation
                with tab1:
                    time.sleep(3)
                    st.write("Your Inputted Data:")
                    st.table(input_table)
                        
                with tab2:
                        st.write("Your Result")
                        cvd_prediction = cvd_model.predict(input_data_imputed)
                        if (cvd_prediction[0] == 0):
                            st.success('You have a low risk of having Cardiovascular Disease')
                        else:
                            st.error('You have a high risk of having Cardiovascular Disease, Please Seek Medical Help Immediately')
                        