import streamlit as st


SSS_URL = 'https://special-song-search.onrender.com'

def st_readme_introduction():
    st.subheader('Introduction', divider=True, anchor='intro')
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            Special-song-search is a web application that allows you to search
            for new songs fitting all of your requirments.

            Rather than using a machine learning model which needs to collect
            your data to make some acceptable recommendations, Special Song
            Search provides several options and relies on you to specify what
            is most important to you. This means:
            1. It doesn't have to store your data.
            2. It can quickly alter its recomendations.
            3. If you like the results, it won't keep re-recommending the same
               small set of songs as some other recomendation engines do.
        """)
        st.image('https://raw.githubusercontent.com/jmlazaro25/special-song-search/main/images/display_example.png')

def st_readme_build():
    st.subheader('Build', divider=True)
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            This is the result of:
            1. Collecting open artist and song (recording) data from
               [MusicBrainz](https://musicbrainz.org/)'s API,
            2. Storing it in a new database using SQLAlchemy for faster access,
            4. And creating a Streamlit app with which users can interact and
               indirectly query the SQL database.
        """)

def st_readme_data_preview():
    st.subheader('Data Preview', divider=True)
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            In the modest data collection that has been done so far, the top 30
            recording tags account for slightly over half of tags used:
        """)
        st.image('https://raw.githubusercontent.com/jmlazaro25/special-song-search/main/images/recording_tag_freq.png')
        st.markdown("""
            Notably, rock has several variations appearing in the top 30
            recording tags: "alternative rock," "pop rock," "indie rock,"
            "classic rock," "hard rock," "folk rock," "progressive rock," and
            "blues rock." This also occurs with other genre tags such pop. This
            begs the question: How much of this is overlap (i.e. recordings
            being labelled "rock" and one or more variations vs. just being
            labelled "rock")?
        """)
        st.image('https://raw.githubusercontent.com/jmlazaro25/special-song-search/main/images/rock_heatmap.png')
        st.markdown(
            """
            This heatmap shows the count of recordings with a tag-pair as a
            fraction of the count of the tag on the diagnol for the tag-pair's
            row. The bright left-most column indicates that recordings tagged
            with any other variation of rock are also likely tagged with rock
            itself. For anyone who likes other forms of rock, but not
            alternative rock, they should rest assured that even though it is
            the most common subset of rock in this dataset, it still only
            accounts for a fifth of all rock and they can search for another
            subgenre with little overlap. Anyone wanting to slowly explore new
            genres or subgenres can choose their favorite tag and search for
            new tags with which it often appears together. data_analysis.ipynb
            in the project's Github repo shows how these plots can be generated
            and goes into more detail about the data.
            """,
        unsafe_allow_html=True
    )

def st_readme():
    st_readme_introduction()
    st_readme_build()
    st_readme_data_preview()

def st_exec_summary():
    st.markdown(
        f"""
        Special Song Search is a song recomendation project I made as I was
        unsatisfied with commercial song recommendation engines. It is
        primarily for individuals who would like fine grained control over
        their recommendations and/or don't want to their data collected and
        used for targeted advertising.

        You can see an example of the web app below and try it
        here: [{SSS_URL}]({SSS_URL}). (Your patience is appreciated as it is
        hosted on Render's free teir.)
        """,
        unsafe_allow_html=True
    )

def st_all():
    st.header('Special Song Search')
    st_exec_summary()
    st.subheader('Contents', divider=True)
    st.markdown(
        '#### 1. [Introduction](#intro)\n'
        '#### 2. [Build](#build)\n'
        '#### 3. [Data Preview](#data-preview)\n',
        unsafe_allow_html=True
    )
    st_readme()
