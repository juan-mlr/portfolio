import streamlit as st
import os


THESIS_NAME = 'Exploring Visible Decay Scenarios In The Light Dark Matter eXperiment'
THESIS_FILE_NAME = THESIS_NAME.lower().replace(' ', '_') + '.pdf'
THESIS_FILE_PATH = os.path.join(os.getcwd(), 'assets', THESIS_FILE_NAME)
LDMX_HOME_URL = 'https://confluence.slac.stanford.edu/display/MME/Light+Dark+Matter+Experiment'
LDMX_COLLAB_IMAGE_URL = 'https://confluence.slac.stanford.edu/download/attachments/210534721/LDMX_institution_logos_aug2022.png?version=1&modificationDate=1661352351000&api=v2'

def st_download_thesis(key: str):
    with open(THESIS_FILE_PATH, 'rb') as file:
        st.download_button(
            label=f'Download "{THESIS_NAME}" (PDF)',
            data=file,
            file_name=THESIS_FILE_NAME,
            mime="application/pdf",
            key=key
        )

def st_exec_summary():
    st.subheader('Executive Summary')
    st.markdown(f"""
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
        $2 \\times 10^{{14}}$ electrons on target. Provided dark matter exists
        and interacts with Standard Model particles according to the operating
        model, this was evidence that LDMX's physical design and the
        accompanying series of analysis methods were capable of formally
        discovering dark matter.

        As a WAVE Fellow at the California Institute of Technology (Caltech),
        I began exploring how LDMX's machine learning model for an invisible
        dark matter search could be modified to work for a visible dark matter
        search. I generated new simulations with Geant4, extracted relevant
        data, and performed feature engineering to minimize decay length bias.

        For my senior thesis "{THESIS_NAME}," I expanded greatly on the work I
        started during my WAVE fellowship. I made more accurate simulations of
        visible signal, combined data from more subdetectors, and completely
        redesigned the framework we had around XGBoost to facilitate developing
        new models for feature selection. Ultimately, I provided the first
        large statistical evidence of LDMX's sensitivity to visible dark
        matter.
    """)
    st_download_thesis('thesis_download_exec')

def st_experiment_background():
    st.subheader('Experiment Background')
    with st.expander('Show/Hide', expanded=True):
        st.markdown(
            f"""
            This section provides just as much background information as is
            required to understand my work in LDMX. As stated above, this page
            does not represent LDMX. For official documents, see
            [here]({LDMX_HOME_URL}).

            ...
            """,
            unsafe_allow_html=True
        )

def st_particle_tracking():
    st.subheader('Particle Tracking')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            My first foray into LDMX analysis was developing a particle
            tracking algorithm. I did this in partnership with a graduate
            student at the time...

            __Tools used:__
            - Python (NumPy, Matplotlib)
            - IBM Spectrum LSF
            - Git/Github
            - Bash
            - ROOT Data Analysis Framework
        """)

def st_vd_at_caltech():
    st.subheader('Visible Decay Search with ML Beginnings at Caltech')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            This was made more difficult due to the need to avoid decay
            length bias...

            __Tools used (*New):__
            - Python (NumPy, Matplotlib, __XGBoost*__)
            - IBM Spectrum LSF
            - Git/Github
            - Bash
            - ROOT Data Analysis Framework
            - __Geant4*__
            - __$\\LaTeX$*__
        """)

def st_senior_thesis():
    st.subheader('Formalizing Search and Expanding ML Framework for Senior Thesis')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            Coming soon.

            __Tools used (*New):__
            - Python (NumPy, Matplotlib, XGBoost)
            - IBM Spectrum LSF, __Slurm Workload Manager*__
            - Git/Github
            - Bash
            - ROOT Data Analysis Framework
            - Geant4, __MadGraph5*__
            - $\\LaTeX$
            - __Docker*__

            #### Abstract:
            The Light Dark Matter eXperiment (LDMX) will use a fixed-target approach to search
            for dark matter in the sub-GeV mass range. LDMX has demonstrated the effectiveness of an
            ECal-based boosted decision tree (BDT) for achieving sensitivity to the invisible signal of a
            dark photon. I propose to study the effectiveness of expanding our current machine learning
            models to use the HCal and other subdetectors to extend sensitivity to visibly decaying dark
            photons and axion-like particles, as well as to improve invisible signal efficiency.

            This document outlines the first steps towards these goals. I begin with introductions
            to the standard model, dark matter, and LDMX. I cover the generation of the new visible
            signal samples needed for this study, followed by descriptions of the extended BDTs designed
            to separate said signal from its backgrounds. An analysis of these BDTs is carried out for
            invisible dark photon signal as well. Results are promising for invisible signal, as one new
            BDT increases the efficiency of the lowest signal mass point from ∼88% with an ECal BDT
            to over 99% at the same, $10^{−4}$ , background efficiency. Similarly, signal efficiencies for visible
            signal at a background efficiency of $10^{−4}$ are above 99% in the phase space surveyed thus
            far.
        """)
        st_download_thesis('thesis_download_thesis')

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
