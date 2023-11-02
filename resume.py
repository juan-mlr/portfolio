import streamlit as st


def show_technical_skills():
    st.header('Technical Skills')
    with st.expander('Show/Hide', expanded=True):
        st.subheader('Programming:')
        st.markdown("""
        - __Python__
            - __Numerical__: NumPy, SciPy, Statsmodels
            - __Data__: Pandas, SQLAlchemy, requests, FastAPI
            - __Machine Learning__: Scikit-Learn, PyTorch, TensorFlow, Hyperopt
            - __Distributed computing__: PySpark
            - __Visualizations__: Matplotlib, Seaborn, Jupyter, Streamliti
        - __SQL__: PostgreSQL, MySQL, SQLite
        - __Distributed Computing__: LSF, Slurm
        - __Git/Github__
        - __Linux__
        - __Bash__
        - __Docker__
        - __Other__:
            - Microsoft Excel, Microsoft PowerPoint
        """)
        st.subheader('Data Science and Machine Learning')
        st.markdown("""
        - __Extract, transform, and load (ETL)__
            - __Data Collection__
            - __Data Wrangling__
            - __Data Cleaning__
        - __Data Analysis__
        - __Modeling__
            - Classification
            - Regression
            - Time Series
            - Anomaly Detection
        - __Data Visualization__
        - __Model Deployment__
        """)
        st.subheader('Industry Knowledge')
        st.markdown("""
            - __Research__
            - __Problem Solving__
            - __Experiment Design__
            - __Stakeholder Relations__
            - __Cross-functional Collaboration__
            - __Education__
        """)


def show_education():
    st.header('Education')
    with st.expander('Show/Hide', expanded=True):
        #st.subheader('Programming:')
        st.latex(r"""\small
        \text{The Data Incubator | Fellowship Program | Data Scientist Certification} \hfill \text{Sep 2023}
        """)
