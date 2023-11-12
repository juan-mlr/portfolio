import streamlit as st
import os


THESIS_FILE_NAME = 'exploring_visible_decay_scenarios_in_ldmx.pdf'
THESIS_FILE_PATH = os.path.join(os.getcwd(), 'assets', THESIS_FILE_NAME)
LDMX_HOME_URL = 'https://confluence.slac.stanford.edu/display/MME/Light+Dark+Matter+Experiment'
LDMX_COLLAB_IMAGE_URL = 'https://confluence.slac.stanford.edu/download/attachments/210534721/LDMX_institution_logos_aug2022.png?version=1&modificationDate=1661352351000&api=v2'

def st_exec_summary():
    st.subheader('Executive Summary')
    st.markdown("""
        On this page, I discuss the work I did as an LDMX collaborator during
        my time as an undergraduate at the University of California, Santa
        Barbara (UCSB). This does ___not___ represent LDMX as a whole. Sections
        are in chronological order and reflect a growing skill set.

        At a high level, LDMX is an experiment looking for evidence of a yet
        undiscovered particle, dark matter. The physical component of LDMX
        consists of an electron beam aimed at a tungsten target with a
        composite detector behind the target. I focused on the analysis of
        interactions in the detector following electron-tungsten interactions,
        collectively reffered to as events. The ultimate goal of this analysis
        was to reliably separate background (caused by particles and
        interactions in the Standard Model of particle physics) events from
        signal (caused by undiscovered dark matter) events.

        First, I helped to develop a particle tracking algorithm that rejected
        the last 10 background events in a set of simulations equivalent to
        $2 \\times 10^{14}$ electrons on target. Provided dark matter exists
        and interacts with Standard Model particles according to the operating
        model, this was evidence that LDMX's physical design and the
        accompanying series of analysis methods were capable of formally
        discovering dark matter.
    """)

def st_experiment_background():
    st.subheader('Experiment Background')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            My first foray into LDMX analysis was developing a particle
            tracking algorithm.
        """)

def st_particle_tracking():
    st.subheader('Particle Tracking')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
        """)

def st_vd_at_caltech():
    st.subheader('Visible Decay Search with ML Beginnings at Caltech')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
        """)

def st_senior_thesis():
    st.subheader('Formalizing Search and Expanding ML Framework for Senior Thesis')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
        """)

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
        '### Sections\n'
        '#### 1. [Experiment Background](#experiment-background)\n'
        '#### 2. [Particle Tracking](#particle-tracking)\n'
        '#### 3. [Visible Decay Search with ML Beginnings at Caltech](#visible-decay-search-with-ml-beginnings-at-caltech)\n'
        '#### 4. [Formalizing Search and Expanding ML Framework for Senior Thesis](#formalizing-search-and-expanding-ml-framework-for-senior-thesis)\n',
        unsafe_allow_html=True
    )
    st.divider()
    st_experiment_background()
    st_particle_tracking()
    st_vd_at_caltech()
    st_senior_thesis()
    st.image(LDMX_COLLAB_IMAGE_URL, caption='Collaborating Institutions')
