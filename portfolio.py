import streamlit as st
from tabs import resume
from tabs import ldmx
from tabs import bird_class
from tabs import sss

def main():

    st.set_page_config(
        page_icon=':chart_with_upwards_trend:',
        page_title='Juan Manuel Lazaro Ruiz',
        layout='wide',
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

        resume_tab, ldmx_tab, bird_class_tab, sss_tab = st.tabs([
            ':page_facing_up: Resume',
            ':dark_sunglasses: LDMX',
            ':penguin: Bird Class',
            ':headphones: Special-Song-Search'
        ])

        with resume_tab:
            st.markdown(
                '### Sections:\n'
                '#### 1. [Education](#education)\n'
                '#### 2. [Technical Skills](#technical-skills)\n'
                '#### 3. [Experience](#experience)\n'
                '#### 4. [Papers](#papers)\n',
            unsafe_allow_html=True
            )
            resume.st_education()
            resume.st_technical_skills()
            resume.st_experience()
            resume.st_papers()

        with ldmx_tab:
            ldmx.st_all()

        with bird_class_tab:
            bird_class.st_all()

        with sss_tab:
            sss.st_all()

        st.markdown(
            '[:arrow_up: Go to top](#juan-manuel-lazaro-ruiz)',
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
