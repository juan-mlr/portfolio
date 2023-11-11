import streamlit as st
import os


THESIS_FILE_NAME = 'exploring_visible_decay_scenarios_in_ldmx.pdf'
THESIS_FILE_PATH = os.path.join(os.getcwd(), 'assets', THESIS_FILE_NAME)
LDMX_HOME_URL = 'https://confluence.slac.stanford.edu/display/MME/Light+Dark+Matter+Experiment'
LDMX_COLLAB_IMAGE_URL = 'https://confluence.slac.stanford.edu/download/attachments/210534721/LDMX_institution_logos_aug2022.png?version=1&modificationDate=1661352351000&api=v2'

def st_exec_summary():
    st.subheader('Executive Summary')
    st.markdown("""
    On this page, I discuss the work I did as an LDMX collaborator during my
    time as an undergraduate at the University of California, Santa Barbara
    (UCSB). It is ___not___ meant as ...
    """)

def st_experiment_background():
    st.subheader('Experiment Background')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            Doloremque dignissimos debitis hic tempora quas quod. Nam vitae iusto ducimus. Nesciunt at labore assumenda laboriosam architecto tempora. Est non laudantium nemo. In voluptatem earum reprehenderit vel nostrum.

            Non repudiandae consectetur aliquam. Sint dolores iste repudiandae delectus eum sapiente aut autem. Eos molestiae dolor officia voluptatem quo voluptas consectetur fugiat.

            Libero nulla in eligendi nam eius est sit. Rerum eos omnis nemo sint. Voluptatibus et rerum laboriosam distinctio voluptatem ut sed magni. Perferendis eum rerum deserunt neque sint atque deleniti ducimus. Nihil eaque sapiente ipsa nam natus. Illum sint quibusdam quia hic esse tempore.

            Non voluptatem et consectetur ipsa qui sint rerum. Enim nostrum qui repudiandae harum incidunt esse. Quia et ea esse ut est nemo sed pariatur.

            Quisquam placeat aut quas ullam deleniti animi. Eos nemo reprehenderit aliquam quam. Fuga unde expedita et consequatur. Excepturi fuga blanditiis expedita architecto.
        """)

def st_particle_tracking():
    st.subheader('Particle Tracking')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            Doloremque dignissimos debitis hic tempora quas quod. Nam vitae iusto ducimus. Nesciunt at labore assumenda laboriosam architecto tempora. Est non laudantium nemo. In voluptatem earum reprehenderit vel nostrum.

            Non repudiandae consectetur aliquam. Sint dolores iste repudiandae delectus eum sapiente aut autem. Eos molestiae dolor officia voluptatem quo voluptas consectetur fugiat.

            Libero nulla in eligendi nam eius est sit. Rerum eos omnis nemo sint. Voluptatibus et rerum laboriosam distinctio voluptatem ut sed magni. Perferendis eum rerum deserunt neque sint atque deleniti ducimus. Nihil eaque sapiente ipsa nam natus. Illum sint quibusdam quia hic esse tempore.

            Non voluptatem et consectetur ipsa qui sint rerum. Enim nostrum qui repudiandae harum incidunt esse. Quia et ea esse ut est nemo sed pariatur.

            Quisquam placeat aut quas ullam deleniti animi. Eos nemo reprehenderit aliquam quam. Fuga unde expedita et consequatur. Excepturi fuga blanditiis expedita architecto.
        """)

def st_vd_at_caltech():
    st.subheader('Visible Decay Search Beginnings at Caltech')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            Doloremque dignissimos debitis hic tempora quas quod. Nam vitae iusto ducimus. Nesciunt at labore assumenda laboriosam architecto tempora. Est non laudantium nemo. In voluptatem earum reprehenderit vel nostrum.

            Non repudiandae consectetur aliquam. Sint dolores iste repudiandae delectus eum sapiente aut autem. Eos molestiae dolor officia voluptatem quo voluptas consectetur fugiat.

            Libero nulla in eligendi nam eius est sit. Rerum eos omnis nemo sint. Voluptatibus et rerum laboriosam distinctio voluptatem ut sed magni. Perferendis eum rerum deserunt neque sint atque deleniti ducimus. Nihil eaque sapiente ipsa nam natus. Illum sint quibusdam quia hic esse tempore.

            Non voluptatem et consectetur ipsa qui sint rerum. Enim nostrum qui repudiandae harum incidunt esse. Quia et ea esse ut est nemo sed pariatur.

            Quisquam placeat aut quas ullam deleniti animi. Eos nemo reprehenderit aliquam quam. Fuga unde expedita et consequatur. Excepturi fuga blanditiis expedita architecto.
        """)

def st_senior_thesis():
    st.subheader('Formalizing Search and Expanding ML Framework for Senior Thesis')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            Doloremque dignissimos debitis hic tempora quas quod. Nam vitae iusto ducimus. Nesciunt at labore assumenda laboriosam architecto tempora. Est non laudantium nemo. In voluptatem earum reprehenderit vel nostrum.

            Non repudiandae consectetur aliquam. Sint dolores iste repudiandae delectus eum sapiente aut autem. Eos molestiae dolor officia voluptatem quo voluptas consectetur fugiat.

            Libero nulla in eligendi nam eius est sit. Rerum eos omnis nemo sint. Voluptatibus et rerum laboriosam distinctio voluptatem ut sed magni. Perferendis eum rerum deserunt neque sint atque deleniti ducimus. Nihil eaque sapiente ipsa nam natus. Illum sint quibusdam quia hic esse tempore.

            Non voluptatem et consectetur ipsa qui sint rerum. Enim nostrum qui repudiandae harum incidunt esse. Quia et ea esse ut est nemo sed pariatur.

            Quisquam placeat aut quas ullam deleniti animi. Eos nemo reprehenderit aliquam quam. Fuga unde expedita et consequatur. Excepturi fuga blanditiis expedita architecto.
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
        '#### 3. [Visible Decay Search Beginnings at Caltech](#visible-decay-search-beginnings-at-caltech)\n'
        '#### 4. [Formalizing Search and Expanding ML Framework for Senior Thesis](#formalizing-search-and-expanding-ml-framework-for-senior-thesis)\n',
        unsafe_allow_html=True
    )
    st.divider()
    st_experiment_background()
    st_particle_tracking()
    st_vd_at_caltech()
    st_senior_thesis()
    st.image(LDMX_COLLAB_IMAGE_URL, caption='Collaborating Institutions')
