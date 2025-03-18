import streamlit as st
from chatbot import send_prompt, establish_api

# Establish sessions state variable to save conversation history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

message_history = st.session_state['message_history']

st.header("Music to match your mood", divider="rainbow")

tab1, tab2 = st.tabs(
    ["Generate song", "Discover"]
)

with tab1:
    st.subheader("Generate a song")

    # Story premise
    mood = st.text_input(
        "Enter your mood: \n\n", key="mood"
    )

    activity = st.multiselect(
        "What you be doing while you listen to music? (can select multiple) \n\n",
        [
            "working",
            "relaxing",
            "working out",
            "creative activity",
            "hang out with friends",
            "party",
            "traveling",
            "other",
        ],
        key="activity",

    )

    song_genre = st.multiselect(
        "Select a song genre: \n\n",
        ["pop", "rock", "R&B", "hip-hop", "classical", "jazz", "electronic"],
        key="song_genre",

    )

    lyrics_instrumental = st.radio(
        "Select if your song will be mostly lyrics or instrumentals: \n\n",
        ["lyrics", "instrumental", "no preference"],
        key="lyrics_instrumental",
        horizontal=True,
    )

    era = st.radio(
        "Select your favorite era of music: \n\n",
        ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"],
        key="era",
        horizontal=True,
    )
    prompt = f"""Respond with a popular song ( a song that was once on the billboard top 100) that best fits the description below: \n
    mood: {mood} \n
    song genre: {song_genre} \n
    lyrics or instrumental: {lyrics_instrumental} \n
    Activity performed while listening to music: {activity} \n
    Era of music: {era} \n
    
    List the song on a line of it's own in quotation marks followed by the artists name all in bold. 
    Write a short description on how you chose that song. Do not include the song request in your response.
    """
    generate_t2t = st.button("Select my song", key="generate_t2t")
    if generate_t2t and prompt:
        # st.write(prompt)
        with st.spinner(
                 f"Generating your song using AI..."
        ):
            first_tab1, first_tab2 = st.tabs(["Song", "Prompt"])
            with first_tab1:
                response = send_prompt(
                    prompt)

                if response:
                    st.write("Your song:")
                    st.write(response)
            with first_tab2:

                st.text(prompt)
with tab2:
    st.subheader("Discover a New Song")
    # Story premise
    moodfordiscovery = st.text_input(
        "Enter your mood: \n\n", key="moodfordiscovery")
    song_genre_for_discovery = st.multiselect(
        "Select a song genre: \n\n",
        ["pop", "rock", "R&B", "hip-hop", "classical", "jazz", "electronic"],
        key="song_genre_for_discovery",

    )
    lyrics_instrumental_for_discovery = st.radio(
        "Select if your song will be mostly lyrics or instrumentals: \n\n",
        ["lyrics", "instrumental", "no preference"],
        key="lyrics_instrumental_for_discovery",
        horizontal=True,
    )
    prompt = f"""Respond with a non-popular song ( a song that was never on the billboard top 100) that best fits the description below: \n
    mood: {moodfordiscovery} \n
    genre: {song_genre_for_discovery} \n
    lyrics or instrumental:{lyrics_instrumental_for_discovery} \n 
    List the song on a line of it's own in quotation marks followed by the artists name all in bold. 
    Write a short description on how you chose that song. Do not include the song request in your response. 
    """
    generate_t2t = st.button("Generate my song", key="generate_song")
    if generate_t2t and prompt:
        second_tab1, second_tab2 = st.tabs(["Song", "Prompt"])
        with st.spinner(
                f"Generating your song using AI ..."
        ):
            with second_tab1:
                response = send_prompt(
                    prompt)
                if response:
                    st.write("Your song suggestion:")
                    st.write(response)
            with second_tab2:
                st.text(prompt)

# Insert API key to get started
with st.sidebar:
    if "api_key" not in st.session_state:
        st.title("Insert API Key!")
        api_key = st.text_input("")
        if api_key:
            st.session_state["api_key"] = api_key
            st.write(establish_api(api_key))
        st.write("**To get started, you'll need a Gemini API key:**")

        instructions = """
        1. **Go to Google AI Studio:** Login and access the platform.
        2. **Click "Get API Key":** Locate the option to obtain an API key.
        3. **Choose Project:** Select a new or existing project for the API key.
        4. **Copy the Key:** Once generated, copy the API key here and have fun!
        """

        st.markdown(instructions)
    else:
        st.write("API Key already entered. Enjoy :D")
