import streamlit as st
import os


THESIS_FILE_NAME = 'exploring_visible_decay_scenarios_in_ldmx.pdf'
THESIS_FILE_PATH = os.path.join(os.getcwd(), 'assets', THESIS_FILE_NAME)

def st_exec_summary():
    ...

def st_experiment_background():
    ...

def st_particle_tracking():
    ...

def st_vd_at_caltech():
    ...

def st_senior_thesis():
    ...

def st_download_thesis():
    with open(THESIS_FILE_PATH, 'rb') as file:
        st.download_button(
            label=f"Download {THESIS_FILE_NAME}",
            data=file,
            file_name=THESIS_FILE_NAME,
            mime="application/pdf"
        )

def st_all():
    st.header('Light Dark Matter Experiment (LDMX)')
    st_exec_summary()
    st.divider()
    st.markdown(
        '#### 1. [Experiment Background](experiment_background)\n'
        '#### 2. [Particle Tracking](particle_tracking)\n'
        '#### 3. [Visible Decay Search Beginnings at Caltech](vd_at_caltech)\n'
        '#### 4. [Formalizing Search and Expanding ML Framework for Senior Thesis](senior_thesis)\n',
        unsafe_allow_html=True
    )
    st.divider()
    st_experiment_background()
    st_particle_tracking()
    st_vd_at_caltech()
    st_senior_thesis()
