import streamlit as st
import streamlit.components.v1 as components
import json 

from supabase import create_client, Client

st.title("Health Portal")   

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

def login(email, password):
    data = supabase.auth.sign_in_with_password({"email": email, "password": password})
    if data.user:
        st.session_state.user = data.user
        st.switch("pages/home.py")
    else:
        st.warning("Login failed. check your credentials.")

def signup(email, password):  
     data = supabase.auth.sign_up({"email": email, "password": password})
     if data.user:
        st.toast("🎉 Signup successful!")
        time.sleep(.5)
        st.toast("Fill the login form with your credentials")
     else:
        st.warning("Signup failed. Please try again.")

col1, col2 = st.columns(2)
with col1:
        with st.expander('Login'):
            email = st.text_input('Email', key='login_email')
            password = st.text_input('Password', type='password', key='login_password')
            signup_btn = st.button('Login ', on_click=login, args=(email, password))
            
with col2:
        with st.expander('Sign Up'):
            new_email = st.text_input('Email', key='signup_email')
            new_password = st.text_input('Password', type='password', key='signup_password')
            signup_btn = st.button('Sign Up', on_click=signup, args=(new_email, new_password))
            
