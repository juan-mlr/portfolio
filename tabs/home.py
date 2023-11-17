import streamlit as st


def st_about():
    st.subheader('About', divider=True)
    st.markdown("""
        I am an innatley curious and analytical person. I am Interested in data
        science, machine learning, and their applications,
        especially where I can make a positive difference such as in climate,
        energy, medicine, and finance.
    """)

def st_bio():
    st.subheader('Bio', divider=True)
    physics_col, ucsb_col, mit_col, data_ml_col = st.columns(4)
    with physics_col:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/CDF_Top_Event.jpg/1200px-CDF_Top_Event.jpg')
    with ucsb_col:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/UCSB_Henley_Gate.jpg/1920px-UCSB_Henley_Gate.jpg')
    with mit_col:
        st.image('https://iblnews.org/wp-content/uploads/2021/06/mit10yearsasnumberone.jpg')
    with data_ml_col:
        st.image('https://www.frontiersin.org/files/Articles/459874/fneur-10-00869-HTML/image_m/fneur-10-00869-g001.jpg')
    st.markdown("""
        When I was 12 years old, I was introduced to high energy physics. I was
        fascinated by the strange results of quantum mechanics, special
        relativity, and the possibility of multiple universes. I began teaching
        myself calculus with free online recources in my free time so that I
        may understand can contribute to the feild's analytical foundations. By
        the time I started my B.S. in physics at the University of California,
        Santa BarbaraI (UCSB) in prestigious the College of Creative Studies,
        I was working through _Introduction to Tensor Analysis and the Calculus
        of Moving Surfaces_ by Pavel Grinfeld. My initiative combined with my
        ability to learn quickly continued to serve me well as I got involved
        with and contributed to the Light Dark Matter Experiment (LDMX). In
        turn, this finally helped me achieve my long sought-after goal of
        pursuing a Ph.D. in physics at MIT. However, by the time I started the
        program, my interests and priorities had begun to change. I did not
        want to completely pass on a great opportunity I for which I had worked
        so much. Thus, I pivoted to fusion energy reseach where I could not
        only continue to make use of the computing and analysis skills I had
        developed and enjoyed using during my time as an LDMX collaborator, but
        also work towards providing humanity a new reliable source of clean
        energy. In the end I decided that I still needed a break from academia
        and so left the Ph.D. program for the time being.

        Since my departure from MIT, I have continued to refine my skills in
        data science and machine learning engineering with programs from the
        Pragmatic Institute (The Data Incubator) and the University of
        California, San Diego (UCSD) Extended Studies. I look forward to a long
        career innovating and making a positive impact on the world.
    """)

def st_interests():
    ...

def st_all():
    st_about()
    st_bio()
