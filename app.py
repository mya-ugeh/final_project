import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from deta import Deta
import streamlit.components.v1 as components
import time
import bcrypt
from streamlit_option_menu import option_menu
import pickle
import pandas as pd
import home, about, contact, dashboard, predict, logout

#set page
st.set_page_config(
    page_title="CARDIO INSIGHT",
    page_icon= "img\INSIGHT-removebg-preview.png",
    initial_sidebar_state='collapsed',
    layout='wide'
)


#.........................DESIGN BEGINS ............................
#to add picture from local computer
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{encoded_string}');
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local('img\green_bg.png')


# to import css file into streamlit
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


#connecting streamlit to database
DETA_KEY = "a0hmzjsaglk_Nv2e9at6DnRkgcpPSQa7RTthC1aLjGtc"
deta = Deta(DETA_KEY)
db = deta.Base('disease_prediction')


#fetch user details from db
def fetch_users():
    """
    Fetch Users
    :return Dictionary of Users:
    """
    users = db.fetch()
    return users.items


#get user email
def get_user_emails():
    """
    Fetch User Emails
    :return List of user emails:
    """
    users = db.fetch()
    emails = []
    for user in users.items:
        emails.append(user['key'])
    return emails


#get users' names
def get_usernames():
    """
    Fetch Usernames
    :return List of user usernames:
    """
    users = db.fetch()
    usernames = []
    for user in users.items:
        usernames.append(user['key'])
    return usernames


#verify password
def verify_password(password,hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

#verify login credentials
def check_user_credentials(username, password):
    users = fetch_users()
    for user in users:
        if user["username"] == username and verify_password(password, user["password"]):
            return True
    return False


#insert user detail into db
def insert_user(last_name,first_name,age,country,state,city,phone_no,address,email, username, password):
    """
    Inserts Users into the DB
    :param email:
    :param username:
    :param password:
    :return User Upon successful Creation:
    """
    date_joined = str(datetime.datetime.now())
    return db.put({'key': email, 'last_name':last_name, 'first_name':first_name, 'age':age, 'country':country, 'state':state, 'city':city, 'phone_no':phone_no , 'address':address,'username': username, 'password': password, 'date_joined': date_joined})



#email validation
def validate_email(email):
    """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com
    if re.match(pattern, email):
        return True
    return


#username validation
def validate_username(username):
    """
    Checks Validity of userName
    :param username:
    :return True if username is valid else False:
    """
    pattern = "^[a-zA-Z0-9]*$"
    if re.match(pattern, username):
        return True
    return False


#signup function
def signup():
    with st.form(key="signup", clear_on_submit=True):
        lname,fname = st.columns(2)
        col1,col2 = st.columns(2)
        col3,col4 = st.columns(2)
        with lname:
            last_name = st.text_input('Last Name', placeholder='Enter Last Name')
        with fname:
            first_name = st.text_input('First Name',placeholder='Enter First Name')
        with col1:
            age = st.number_input('Age', min_value=10,max_value=200,placeholder='Enter Age')
        with col2:
            country = st.text_input('Country')
        with col3:
            state = st.text_input('State')
        with col4:
            city = st.text_input("Town/City", placeholder="Enter town or city")
        address = st.text_area("Address", placeholder='Enter Address')
        phone_no = st.text_input('Phone Number', placeholder="Enter Phone Number")
        email = st.text_input("Email", placeholder="Enter Your Email...")
        username = st.text_input("Usename", placeholder="Enter Username...")
        password1 = st.text_input("Password", placeholder="Enter Password...", type='password')
        password2 = st.text_input("Confirm Password", placeholder="Confirm Password...", type='password')
        b1,b2,b3,b4,b5 = st.columns(5)
        with b3:
            signup_button = st.form_submit_button("Sign Up")
        #form validation
        if signup_button:
            if validate_email(email):
                if email not in get_user_emails():
                    if validate_username(username):
                        if username not in get_usernames():
                            if len(username) >= 2:
                                if len(password1) >= 6:
                                    if password1 == password2:
                                        # Add User to DB
                                        hashed_password = bcrypt.hashpw(password2.encode(), bcrypt.gensalt()).decode()
                                        insert_user(last_name, first_name, age, country, state, city, phone_no, address, email, username, hashed_password)
                                        st.success('Account created successfully!!')
                                        st.balloons()
                                    else:
                                        st.warning('Passwords Do Not Match')
                                else:
                                    st.warning('Password is too Short')
                            else:
                                st.warning('Username Too short')
                        else:
                            st.warning('Username Already Exists')
                    else:
                        st.warning('Invalid Username')
                else:
                    st.warning('Email Already exists!!')
            else:
                st.warning('Invalid Email')               


#login function
def login():
    with st.form("Login", clear_on_submit=True):
        login_name = st.text_input("Username", placeholder="Enter Username...")
        login_password = st.text_input("Password", placeholder="Enter Password...", type='password')
        if st.form_submit_button("Login"):
            if check_user_credentials(login_name, login_password):
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Invalid username or password")
                
                
                
#login_signup
def login_signup_page():
    on = st.toggle("Login/SignUp")
    
    if on:
        signup()
    else:
        login()



#main app logic
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        
    if st.session_state['logged_in']:
        # Navigation sidebar
        with st.sidebar:
            selected = option_menu("Main Menu", ["Home", "Contact Us", "About Us", "Dashboard", "Prediction", "Logout"],
                                icons=['house', 'envelope', 'info-circle', 'bar-chart', 'activity', 'box-arrow-right'],
                                menu_icon="cast", default_index=0)

        if selected == "Home":
            home.home_page()
        elif selected == "Contact Us":
            contact.contact_us_page()
        elif selected == "About Us":
            about.about_us_page()
        elif selected == "Dashboard":
            dashboard.dashboard_page()
        elif selected == "Prediction":
            predict.prediction_page()
        elif selected == "Logout":
            logout.logout_page()
            st.session_state['logged_in'] = False
            st.rerun()
    else:
        login_signup_page()

if __name__ == "__main__":
    main()
    