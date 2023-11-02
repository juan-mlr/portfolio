import streamlit as st
import resume


def main():

    st.set_page_config(
        #layout='wide',
        initial_sidebar_state='auto',
        menu_items=None
    )

    st.title('Juan Manuel Lazaro Ruiz')
    resume_tab, bird_class_tab = st.tabs([
        'Resume :page_facing_up:',
        'bird-class :penguin:'
    ])

    with resume_tab:
        resume.show_technical_skills()
        resume.show_education()

if __name__ == "__main__":
    main()

