import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from deta import Deta
import hydralit_components as hc
import bcrypt
from streamlit_option_menu import option_menu
import home, about, contact, dashboard, predict, mimo, logout
import platform

#set page
st.set_page_config(
    page_title="CARDIO INSIGHT",
    page_icon= "img\INSIGHT-removebg-preview.png",
    layout='wide',
    initial_sidebar_state='auto'
)

# to import css file into streamlit
with open('css\style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    

#connecting streamlit to database
DETA_KEY = "a0hmzjsaglk_Nv2e9at6DnRkgcpPSQa7RTthC1aLjGtc"
deta = Deta(DETA_KEY)
db = deta.Base('cvd_prediction')


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
def insert_user(last_name,first_name,email, username, password):
    """
    Inserts Users into the DB
    :param email:
    :param username:
    :param password:
    :return User Upon successful Creation:
    """
    date_joined = str(datetime.datetime.now())
    return db.put({'key': email, 'last_name':last_name, 'first_name':first_name,'username': username, 'password': password, 'date_joined': date_joined})



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




sign1, sign2 = st.columns(2)
with sign1:
    def signup_step_1():
        with st.form(key="signup_step_1", clear_on_submit=True):
            last_name = st.text_input('Last Name', placeholder='Enter Last Name')
            first_name = st.text_input('First Name', placeholder='Enter First Name')
            email = st.text_input("Email", placeholder="Enter Your Email...", value=st.session_state.get('email', ''))
            next_button = st.form_submit_button("Next")
            if next_button:
                st.session_state['signup_step'] = 2
                st.session_state['last_name'] = last_name
                st.session_state['first_name'] = first_name
                st.session_state['email'] = email
                st.rerun()
                
                    
    def signup_step_2():
        with st.form(key="signup_step_2", clear_on_submit=True):
            username = st.text_input("Username", placeholder="Enter Username...", value=st.session_state.get('username', ''))
            password1 = st.text_input("Password", placeholder="Enter Password...", type='password')
            password2 = st.text_input("Confirm Password", placeholder="Confirm Password...", type='password')
            prev_button, next_button = st.columns(2)
            with prev_button:
                if st.form_submit_button("Previous"):
                    st.session_state['signup_step'] = 1
                    st.session_state['username'] = username
                    st.session_state['password1'] = password1
                    st.session_state['password2'] = password2
                    st.rerun()
            with next_button:
                if st.form_submit_button("Submit"):
                    if validate_email(st.session_state['email']):
                        if st.session_state['email'] not in get_user_emails():
                            if validate_username(username):
                                if username not in get_usernames():
                                    if len(username) >= 2:
                                        if len(password1) >= 6:
                                            if password1 == password2:
                                                # Add User to DB
                                                hashed_password = bcrypt.hashpw(password2.encode(), bcrypt.gensalt()).decode()
                                                insert_user(
                                                    st.session_state['last_name'],
                                                    st.session_state['first_name'],
                                                    st.session_state['email'],
                                                    username,
                                                    hashed_password
                                                )
                                                st.success('Account created successfully!!')
                                                st.balloons()
                                                st.session_state['show_signup'] = False
                                                st.session_state['signup_step'] = 1
                                                st.rerun()
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

    
    #signin    
    def login():
        a,b = st.columns(2)
        with a:
            st.markdown("<h5 style='text-align:center; font-family:system-ui; font-size:25px; margin-left:5pc; color:white'>Welcome Back</h5>",unsafe_allow_html=True)
            st.write("<p style='font-size:10px; text-align:center; margin-left:5pc; color:white '>Signin into your Account</p>",unsafe_allow_html=True)
            with st.form("Login", clear_on_submit=True,border=False):
                login_name = st.text_input("Username", placeholder="Enter Username...")
                login_password = st.text_input("Password", placeholder="Enter Password...", type='password')
                login_btn = st.form_submit_button('Login',use_container_width=True)
                # st.markdown("Forgot Password?",help="Click here if you have forgotten your password. We will guide you through the steps to reset it and recovering your account.",unsafe_allow_html=True)
                if login_btn:
                    if check_user_credentials(login_name, login_password):
                        st.session_state['logged_in'] = True
                        st.rerun()
                    else:
                        st.error("Invalid username or password")
            signup_btn = st.button("Don't have an account? Sign up")
            if signup_btn:
                st.session_state['show_signup'] = True
                st.session_state['signup_step'] = 1
                st.rerun()

#main app logic
def main():
    if 'show_signup' not in st.session_state:
        st.session_state['show_signup'] = False
        
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        
    if st.session_state['logged_in']:
        nav1,nav2 = st.columns(2)
        with nav1:
        # Navigation
            with st.sidebar:
                selected = option_menu(None,["Home", "About Us", "Dashboard", "Prediction", "Contact Us", "Mimo","Logout"],
                                        icons=['house', 'info-circle', 'bar-chart', 'activity', 'envelope','robot', 'box-arrow-right'],
                                        menu_icon="cast", default_index=0,
                                        styles={
                                            "container": { "background-color": "black"},
                                            "icon": {"color": "#003853", "font-size": "15px"}, 
                                            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                            "nav-link-selected": {"background-color": "green"}
                                        }
                                    )
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
            elif selected == "Mimo":
                mimo.mimo_page()
            elif selected == "Logout":
                logout.logout_page()
                st.session_state['logged_in'] = False
                st.rerun()
    elif st.session_state['show_signup']:
        step = st.session_state.get('signup_step', 1)
        if step == 1:
            signup_step_1()
        elif step == 2:
            signup_step_2()
    else:
        login()
        

if __name__ == "__main__":
    main()
    