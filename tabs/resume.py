import streamlit as st


def st_left_right_align(left_text: str, right_text: str):
    st.markdown(
        '<div style="display: flex; justify-content: space-between;">'
        f'<div style="font-size: 1.1em;"><b>{left_text}</b></div>'
        f'<div style="font-size: 1.1em;"><b>{right_text}</b></div>'
        '</div>',
        unsafe_allow_html=True
    )

def st_technical_skills():
    st.header('Technical Skills')
    with st.expander('Show/Hide', expanded=True):
        st.subheader('Programming and Software:')
        st.markdown("""
            - __Python__
                - __Numerical__: NumPy, SciPy, Statsmodels
                - __Data__: Pandas, SQLAlchemy, requests, FastAPI
                - __Machine Learning__: Scikit-Learn, PyTorch, TensorFlow, Hyperopt
                - __Distributed computing__: PySpark
                - __Visualizations__: Matplotlib, Seaborn, Jupyter, Streamlit
            - __SQL__: PostgreSQL, MySQL, SQLite
            - __Distributed Computing__: LSF, Slurm
            - __Git/GitHub/GitLab__
            - __Linux__
            - __Bash__
            - __Docker__
            - __Other__:
                - LaTeX ($\LaTeX$)
                - Microsoft Excel, Microsoft PowerPoint
            """)
        st.subheader('Data Science and Machine Learning')
        st.markdown("""
            - __Extract, transform, and load (ETL)__
                - __Data Collection__, __Data Wrangling__, __Data Cleaning__
            - __Data Analysis__
            - __Modeling__
                - Feature Engineering, Feature Selection
                - Classification, Regression, Time Series, Anomaly Detection
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


def st_education():
    st.header('Education')
    with st.expander('Show/Hide', expanded=True):
        st.markdown('#### Degrees')
        st_left_right_align(
            'Coursework toward Ph.D. in Physics | Massachusetts Institute of Technology (MIT)',
            'Feb 2022 - Nov 2022'
        )
        st_left_right_align(
            'B.S. in Physics | University of California, Santa Barbara (UCSB)',
            'Sep 2021'
        )
        st.markdown("""
            - NSF Graduate Research Fellowship Program Honorable Mention
            - California Institute of Technology (Caltech) WAVE Fellowship
            - UCSB McNair Fellowship
            - UCSB Promise Scholar
        """)
        st.markdown('#### Certifications')
        st_left_right_align(
            'The Data Incubator'
            ' | Fellowship Program'
            ' | <a href="https://www.credly.com/badges/fb690af3-ce80-4a53-b6d6-7cb18e93fb8e/linked_in_profile" target="_blank">Data Scientist Certification</a>',
            'Sep 2023'
        )
        st_left_right_align(
            'DataCamp'
            ' | <a href="https://www.datacamp.com/certificate/DS0023881595718" target="_blank">Data Science Professional Certification</a>'
            ' | Valid through Mar 2025',
            'Mar 2023'
        )

def st_experience():
    st.header('Experience')
    with st.expander('Show/Hide', expanded=True):
        st_left_right_align(
            'MASSACHUSETTS INSTITUTE OF TECHNOLOGY',
            '02/2022 – 11/2022'
        )
        st.markdown("""
            ##### Graduate Fellow
            - Studied magnetic field anomalies and their effects in new tokamak simulations to increase fusion efficiency and eventually establish commercial viability.
            - Visualized and analyzed plasma to control instances of magnetic reconnection, optimizing tokamak’s performance.
            - Tutored undergraduate individuals and groups in electromagnetism.
        """)
        st_left_right_align(
            'UNIVERSITY OF CALIFORNIA, SANTA BARBARA',
            '06/2019 – 09/2021'
        )
        st.markdown("""
            ##### Undergraduate Researcher
            - Contributed to rejection of all simulated background in Light Dark Matter eXperiment (LDMX) dark photon search by developing particle tracking algorithm and classification model (XGBoost) in electromagnetic calorimeter (ECal).
            - Achieved 99%+ baseline efficiency for specific class of dark matter in LDMX by generating simulations of visible dark photons and creating new veto pipeline, confirming LDMX is sensitive to multiple classes of dark matter and therefore provides potential cost savings on future high-energy physics experiments.
            - Updated up to 30 stakeholders in person and via Zoom on particle-tracking algorithm (weekly) and ML (every 2-3 weeks).
        """)
        st_left_right_align(
            'CALIFORNIA INSTITUTE OF TECHNOLOGY',
            '02/2020 – 08/2020'
        )
        st.markdown("""
            ##### Undergraduate Research Fellow
            - Spearheaded LDMX’s development of background rejection process for search of new class of dark matter (axion-like particles) by creating new XGBoost model utilizing more subdetectors than existing model for dark photon search.
        """)

def st_papers():
    st.header('Papers')
    with st.expander('Show/Hide', expanded=True):
        st_left_right_align(
            '<a href="https://link.springer.com/article/10.1007/JHEP04(2020)003" target="_blank">A high efficiency photon veto for the Light Dark Matter eXperiment</a>',
            '04/2020'
        )
        st.markdown("""
            Akesson, T., Blinov, N., __Lazaro, J.__, et al. (2020) | Journal of High Energy Physics, 3, 1-29
            - Discusses particle tracking algorithm I helped develop which is the final step in rejecting all simulated background events.
            - Includes visualizations I created.
        """)
