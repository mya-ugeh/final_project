import streamlit as st
import base64
import about, contact, dashboard, predict, logout
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.colored_header import colored_header
import json
import requests
from streamlit_lottie import st_lottie

def quiz_app():
    questions = [
        "What is the leading cause of death worldwide?",
        "Which of the following is a symptom of a heart attack?",
        "What is a common risk factor for cardiovascular disease?",
        "How can you reduce the risk of cardiovascular disease?",
        "What is the medical term for high blood pressure?",
        "Which of the following is a modifiable risk factor for cardiovascular disease?",
        "What type of cholesterol is considered 'good' for the heart?",
        "What is a common sign of a stroke?",
        "What lifestyle change can help lower blood pressure?",
        "What dietary component is important for heart health?"
    ]

    options = [
        ["Cancer", "Cardiovascular disease", "Diabetes", "Infectious diseases"],
        ["Sudden severe headache", "Chest pain", "Stomach ache", "Back pain"],
        ["Smoking", "Regular exercise", "Healthy diet", "Normal blood pressure"],
        ["Smoking", "High salt intake", "Obesity", "Regular physical activity"],
        ["Hypotension", "Hypertension", "Hypoglycemia", "Hyperglycemia"],
        ["Age", "Gender", "Family history", "Smoking"],
        ["LDL", "HDL", "VLDL", "Triglycerides"],
        ["Sudden confusion or trouble speaking", "Persistent leg pain", "Frequent headaches", "Chronic fatigue"],
        ["Increased salt intake", "Regular exercise", "Excessive alcohol consumption", "Increased sugar intake"],
        ["High saturated fat", "High trans fat", "High fiber", "High sugar"]
    ]

    answers = [
        "Cardiovascular disease",
        "Chest pain",
        "Smoking",
        "Regular physical activity",
        "Hypertension",
        "Smoking",
        "HDL",
        "Sudden confusion or trouble speaking",
        "Regular exercise",
        "High fiber"
    ]

    st.markdown("<h4>Cardiovascular Disease Quiz</h4>", unsafe_allow_html=True)

    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0

    current_question = st.session_state.current_question

    if current_question < len(questions):
        st.write(questions[current_question])

        option = st.radio("Choose an option", options[current_question])

        if st.button("Submit"):
            if option == answers[current_question]:
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(f"Wrong! The correct answer is {answers[current_question]}.")
            
            st.session_state.current_question += 1

            if st.session_state.current_question < len(questions):
                st.experimental_rerun()
            else:
                st.balloons()
                st.write("Quiz Finished!")
                st.write(f"Your final score is {st.session_state.score} out of {len(questions)}")

    else:
        st.write("Quiz Finished!")
        st.write(f"Your final score is {st.session_state.score} out of {len(questions)}")

    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.experimental_rerun()

def contact_us_page():

    # Add custom CSS
    with open('css\contact.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            
    
    with stylable_container(
        key="contact_container",
        css_styles="""
            {
                background-color: #012034;
                width: 76pc;
                margin-top: -6.1pc;
                margin-left: -14pc;
            }
        """,
    ):
        st.markdown("<h2 style = 'width:76pc; text-align:center; color:white'>GET IN TOUCH</h2>", unsafe_allow_html=True)
        st.markdown("<p style='width:76pc; color:white;text-align:center; font-size: 8px; margin-top: -11px;'>Our team is committed to providing you with the best support possible. Feel free to get in touch with us for any assistance or information regarding our services.</p><br>", unsafe_allow_html=True)
        a,b,c = st.columns(3)
        with a:
            st.markdown("<img src='https://img.icons8.com/?size=40&id=9Deeqjb8MjFH&format=png&color=FFFFFF' style = 'margin-left: 8pc;'>", unsafe_allow_html=True)
            st.markdown("<h4 style='margin-left:6pc; color:white;'>ADDRESS</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; color:white;'>Trinity University City <br>Campus, Off Alara Street,<br> (Near Queens College) <br>Yaba, Lagos.</p>", unsafe_allow_html=True)
        with b:
            st.markdown("<img src='https://img.icons8.com/?size=40&id=53439&format=png&color=FFFFFF' style='margin-left: 8pc;'>", unsafe_allow_html=True)
            st.markdown("<h4 style='margin-left:7pc; color:white;'>PHONE</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; color:white;'> +2347032166707, <br>+2347032167003</p>", unsafe_allow_html=True)
        with c:
            st.markdown("<img src='https://img.icons8.com/?size=40&id=12623&format=png&color=FFFFFF' style = 'margin-left: 8pc;'>", unsafe_allow_html=True)
            st.markdown("<h4 style='margin-left:7pc; color:white;'>E-MAIL</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; color:white;'>info@trinityuniversity.edu.ng</p>", unsafe_allow_html=True)
        
    with stylable_container(
        key="contact2_container",
        css_styles="""
            {
                width: 76pc;
                margin-left: -11pc;
            }
        """,
    ):  
        st.markdown("<br><br>",unsafe_allow_html=True)

  
        f, d,e = st.columns(3)
        with f:
            st.markdown("<h5 style='margin-left:4pc;'>Message Us <img src='https://img.icons8.com/?size=30&id=18628&format=png&color=FFFFFF'></h5>", unsafe_allow_html=True)
            st.markdown("<p style = 'text-align:justify;'>We are here to help you with any questions or concerns you may have about our Cardiovascular Disease Prediction System. Whether you are a patient, healthcare professional, or medical researcher, we welcome your inquiries. Please use the contact information below to reach out to us.</p>",unsafe_allow_html=True)
        with e:
            quiz_app()

            # # Function to load Lottie animation from a local file
            # def load_lottie_file(filepath: str):
            #     with open(filepath, 'r') as f:
            #         return json.load(f)

            # # Load a Lottie animation from a local file
            # lottie_animation = load_lottie_file("img\Animation - 1718071352781.json")

            # # Display the Lottie animation
            # st_lottie(lottie_animation, height=300, width=300, quality='high')

        with d:
            #form
            contact_form = """
            <form action="https://formsubmit.co/85b4b51aa7d6cc3cf6423216a8f6011a" method="POST">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here"></textarea>
                <input type="hidden" name="_template" value="table">
                <input type="hidden" name="_subject" value="New submission!">
                <input type="hidden" name="_autoresponse" value="Hi there, Thanks for reaching out. Please hold on while our team get back to you">
                <button type="submit">Send</button>
            </form>
            """
            st.markdown(contact_form, unsafe_allow_html=True)
    
        