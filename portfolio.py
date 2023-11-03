import streamlit as st
import resume
#import ldmx

def main():

    st.set_page_config(
        layout='wide',
        initial_sidebar_state='auto',
        menu_items=None
    )

    # layout TBD
    left_col, main_col, right_col = st.columns([0.1, 100, 0.1])

    with main_col:
        st.title('Juan Manuel Lazaro Ruiz')
        st.markdown(
            ':e-mail: [juan.m.lazaro.ruiz@gmail.com](mailto:juan.m.lazaro.ruiz@gmail.com)'
            ' | [![text](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/j-m-lazaro)'
            ' | <a href="https://github.com/jmlazaro25"><img src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" alt="text" width="30rem"></a>',
            unsafe_allow_html=True
        )

        resume_tab, ldmx_tab, bird_class_tab = st.tabs([
            'Resume :page_facing_up:',
            'LDMX :dark_sunglasses:',
            'bird-class :penguin:'
        ])

        with resume_tab:
            st.markdown(
                '### 1. [Education](#education)\n'
                '### 2. [Technical Skills](#technical-skills)\n'
                '### 3. [Experience](#experience)\n'
                '### 4. [Papers](#papers)\n'
            )
            resume.st_education()
            resume.st_technical_skills()
            resume.st_experience()
            resume.st_papers()

    #    with ldmx_tab:
    #        ldmx.st_exec_summary()

if __name__ == "__main__":
    main()

