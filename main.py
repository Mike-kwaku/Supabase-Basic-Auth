import streamlit as st
import streamlit.components.v1 as components

from supabase import create_client, Client

st.title("Health Portal")   

# Initialize connection.
# Uses st.cache_resource to only run once.
# @st.cache_resource
#def init_connection():
 #   url = st.secrets["SUPABASE_URL"]
  #  key = st.secrets["SUPABASE_KEY"]
   # return create_client(url, key)

# supabase = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
#@st.cache_resource(ttl=600)
#def run_query():
 #   return supabase.table("health").select("*").execute()

#rows = run_query()

# Print results.
#for row in rows.data:
 #   st.write(f"{row['customer_name']} visited us on :{row['recent_doctor_visit']}:")

col1, col2 = st.columns(2)
with col1:
        with st.expander('Login'):
            email = st.text_input('Email', key='login_email')
            password = st.text_input('Password', type='password', key='login_password')
            
with col2:
        with st.expander('Sign Up'):
            new_email = st.text_input('Email', key='signup_email')
            new_password = st.text_input('Password', type='password', key='signup_password')
            
