import streamlit as st


SSS_URL = 'https://special-song-search.onrender.com/'
DISPLAY_EXAMPLE_URL = 'https://raw.githubusercontent.com/jmlazaro25/special-song-search/main/images/display_example.png'

def st_all():
    st.markdown(
        f"""
        ### Special Song Search
        Special Song Search is a song recomendation project I made as I was
        unsatisfied with commercial song recommendation engines. It is
        primarily for individuals who would like fine grained control over
        their recommendations and/or don't want to their data collected and used for
        targeted advertising.

        You can see an example of the web app below and try it
        here: [{SSS_URL}]({SSS_URL}).
        """,
        unsafe_allow_html=True
    )
    st.image(DISPLAY_EXAMPLE_URL)
