import streamlit as st
import os
from PIL import Image

from utils.styling import image_column_widths


ASSETS_DIR = os.path.join(os.getcwd(), 'assets')
THESIS_NAME = 'Exploring Visible Decay Scenarios In The Light Dark Matter eXperiment'
THESIS_FILE_NAME = THESIS_NAME.lower().replace(' ', '_') + '.pdf'
THESIS_FILE_PATH = os.path.join(ASSETS_DIR, THESIS_FILE_NAME)
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

            The Standard Model of particle physics is one of the most complete
            and succesful models we have to describe our universe on the
            smallest distance scales, but it is incomplete. Likewise, general
            relativity has been extremely succesful from planetary to
            cosmological scales, but is also an incomplete theory. However,
            general relativity may be providing one of the best clues for a
            missing piece in the Standard Model. There are a few discrepancies
            between the behavior of matter in some galaxies and the predictions
            general relativity makes based on the observable matter in those
            galaxies. Below is an example of one such case: the Bullet Cluster
            which suggests there is a significant amount of matter which we can
            only detect through its gravitational effects.
            """,
            unsafe_allow_html=True
        )
        st.image(
            'https://chandra.harvard.edu/photo/2006/1e0657/1e0657_420.jpg',
            caption="""
                An X-ray map (pink) showing the heated matter as a result of
                the colliding clusters that now make up galaxy cluster
                1E0657-56 and gravitational lensing map (blue) indicating the
                distribution of mass superimposed on a visible light image of
                the same part of the sky. This suggests most matter, which is
                only detectable through gravatational lensing, had little or no
                interaction in the collision. Source:
                https://chandra.harvard.edu/photo/2006/1e0657/index.html
            """
        )
        st.markdown("""
            Through cosmological observations and modeling, it is estimated
            that this matter that interacts very weakly, if at all, with the
            electromagnetic force, and which we have come to call dark matter,
            makes up about 5 times more of the energy density or "stuff" in
            the universe than does familiar Standard Model matter. Discovering
            what dark matter is exactly, would therefore be a huge leap forward
            in our understanding of the universe.

            There have been several different models of different classes
            proposed for the form dark matter may take. LDMX will be searching
            for a dark matter in a lower mass range than most past experiments,
            hence the name "light dark matter." It will do this by firing
            electrons at a tungsten target and waiting for the electron to
            radiate a dark matter particle, or more precisely, a new force
            carrier we call a dark photon or $A'$. We will know when this
            happens because the $A'$ should then travel through the detector
            without interacting which we would see that as missing energy and
            momentum.

            In most cases, the electron will produce particles known to the
            Standard Model. Electromagnetically charged particles' energy is
            captured by the electromagnetic calorimeter (ECal) and
            electromagnetically neutral particles' energy is captured by the
            hadron calorimeter (HCal). If these background events can be
            seperated from the events of interest, we can use information from
            the remaining events to reconstruct properties of the new particle
            such its mass.

            Before the development of a particle tracking algorithm in the
            ECal, the seperation process required the following of events:
            1. ECal total energy $\\lt$ 1.5 GeV (Trigger)
            2. Single track in recoil tracker with $p \\lt$ 1.2 GeV
            3. ECal BDT (Boosted Decision Tree) discriminator value $\\gt 0.99$
            4. HCal PE (photoelectrons) $\\lt$ 5

            The ECal BDT, and later the particle tracking algorithm, make use
            of the projected paths of the recoil electron and photon, with the
            assumption that the electron radiated a photon in the target.
            Around each of these paths, we also have radii of containment which
            represent the distance from the path at each layer of the ECal
            within which 68% of secondary (showered) particles are found.
        """)
        ldmx_out_image = Image.open(os.path.join(ASSETS_DIR, 'ldmx_out.jpg'))
        ldmx_in_image = Image.open(os.path.join(ASSETS_DIR, 'ldmx_in.jpg'))
        widths = image_column_widths(
            [ldmx_out_image.size, ldmx_in_image.size],
            500
        )
        ldmx_out, ldmx_in = st.columns(widths)
        with ldmx_out:
            st.image(
                ldmx_out_image,
                use_column_width=True,
                caption="""
                A rendering of the complete LDMX detector. Source:
                https://doi.org/10.1007/JHEP04(2020)003
                """
            )
        with ldmx_in:
            st.image(
                ldmx_in_image,
                use_column_width=True,
                caption="""
                A vertical cross section of LDMX showing its subdetectors. Note
                that the ECal will be rotated 90° from what is shown to gain
                some acceptance of recoil electrons, which will be deflected
                right by the downward magnetic field. Source:
                https://doi.org/10.1007/JHEP04(2020)003
                """
            )
        st.image(
            os.path.join(ASSETS_DIR, 'event_cartoons.jpg'),
            """
            Cartoons of invisible (Left) and visible (Right) DM signatures.
            For our purposes, the LLP (long lived particle) is an A′. Future
            analyses may consider ALPs. The μ suggests a beam option for other
            potential similar experiments, motivated by the possibility of the
            LLP having a stronger coupling to heavier leptons. Source:
            Dark Matter, Millicharges, Axion and Scalar Particles, Gauge Bosons
            and Other New Physics with LDMX, Phys. Rev.D 99 (2019) 075001
            """
        )

def st_particle_tracking():
    st.subheader('Particle Tracking')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            My first foray into LDMX analysis was a collaboration with a
            UCSB graduate student in which we developed a minimum ionizing
            particle (MIP) tracking algorithm. This was necessitated by
            background events where the photon would produce a single neutral,
            possibly soft (low-momentum), hadron. In these cases, there may be
            very few hits around the projected photon path which would be very
            difficult for the ECal BDT to distinguish from a signal ($A'$)
            event. Note that although the ECal will use sophisticated
            technology, it is not immune to noise. Thus, we cannot reject all
            events with any hits near the photon path without losing a
            significant fraction of signal events.

            ...
        """)
        st.image(
            os.path.join(ASSETS_DIR, 'official_mip_tracking.png'),
            """
            Left: visualization of a simulated PN event that survives both the
            ECal BDT and HCal activity vetoes, but is rejected by the ECal
            tracking algorithm. Hits are color-coded according to whether they
            are inside or outside the electron and photon containment radii,
            and the black line indicates the reconstructed track. Right:
            number of ECal tracks detected per event in a sample of 10,000
            events each for signal and PN background after ECal vetoes;
            normalized to unit area. Source:
            A high efficiency photon veto for the Light Dark Matter eXperiment
            Akesson, T., Blinov, N., Lazaro, J., et al. (2020)
            | Journal of High Energy Physics, 3, 1-29
            """
        )
        st.markdown("""
        """)
        st.image(
            os.path.join(ASSETS_DIR, 'official_cut_table.jpg'),
            """
            The estimated levels of photo-nuclear and muon conversion
            backgrounds after applying the successive background rejection cuts.
            Here, the total events simulated corresponds to the total electrons
            fired on target in the simulation. The biasing factor passed to the
            Geant4 occurrence biasing toolkit is used to scale the total events
            simulated to the electron on target (EoT) equivalent. Source:
            A high efficiency photon veto for the Light Dark Matter eXperiment
            Akesson, T., Blinov, N., Lazaro, J., et al. (2020)
            | Journal of High Energy Physics, 3, 1-29
            """
        )
        st.markdown("""
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
            to the Standard Model, dark matter, and LDMX. I cover the generation of the new visible
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
        '### Contents\n'
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
