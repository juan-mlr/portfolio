import streamlit as st


def st_about():
    st.subheader('About:')
    st.markdown("""
        Interested in data science, machine learning, and their applications,
        especially in climate, energy, and finance.
    """)

def st_bio():
    st.subheader('Bio:')
    st.markdown("""
        I am an innately curious person. Around the 8th grade, I was introduced
        to high energy physics and decided that is what I wanted to do.....
        ccs -> mit
    """)

def st_interests():
    ...

def st_all():
    st_about()
    st_bio()
