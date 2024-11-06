import streamlit as st
from tabs import home
from tabs import resume
from tabs import ldmx
from tabs import bird_class
from tabs import sss


TAB_LABEL_MODULES = {
    ':house_with_garden: Home': home,
    ':page_facing_up: Resume': resume,
    ':dark_sunglasses: LDMX': ldmx,
    ':penguin: Bird Class': bird_class,
    ':headphones: Special-Song-Search': sss,
}

def main():

    st.set_page_config(
        page_icon=':chart_with_upwards_trend:',
        page_title='Juan M. Lazaro Ruiz',
        layout='wide',
    )

    st.markdown("""
        <style>
            .block-container {padding-top: 1rem !important;}
        </style>""",
        unsafe_allow_html=True,
    )

    # layout not final
    left_col, main_col, right_col = st.columns([20, 100, 20])

    with main_col:
        st.title('Juan M. Lazaro Ruiz')
        st.markdown(
            ':e-mail: [juan.m.lazaro.ruiz@gmail.com](mailto:juan.m.lazaro.ruiz@gmail.com)'
            ' | [![text](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/juan-mlr)'
            ' | <a href="https://github.com/juan-mlr"><img src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" alt="text" width="30rem"></a>',
            unsafe_allow_html=True
        )

        tabs = st.tabs(TAB_LABEL_MODULES.keys())
        for tab, tab_module in zip(tabs, TAB_LABEL_MODULES.values()):
            with tab:
                tab_module.st_all()

        st.markdown(
            '[:arrow_up: Go to top](#juan-manuel-lazaro-ruiz)',
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
