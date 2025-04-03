import streamlit as st

''' st.title("Nepal Class in 2025")

st.header("Nepal Class in 2025") # primary section
st.subheader("Nepal Class in 2025") # subsection

st.write("Nepal Class in 2025")

st.write("NER identifies and classifies key entities (such as\
people, places, organizations, dates, etc.) within text.\
For example, in the sentence Apple Inc. was founded in 1976, NER would recognize Apple Inc.\
as an organization and 1976 as a date.")

st.button("submit",  type="primary")

st.button("submit",  type="secondary")

st.checkbox("Male", value=True)
st.selectbox("fruits", ["Apple", "Banana", "Cherry"], placeholder="choose a fruit")

#st.write("You can only enter a maximum of 200 characters")
text_var = st.text_input("career summary", value="", max_chars=200, placeholder="You can only enter a maximum of 200 characters")
if len(text_var) != 0:
    st.write("we saw that you wrote this:", text_var)
else:
    print("")


st.number_input("age", min_value=1, max_value=20, placeholder="age between 15 and 60", value=15)
st.slider("year", min_value=2000, max_value=2050, step=2)

data = st.file_uploader("upload file", type=["csv", "txt"])

if data:
    st.write("file uploaded successfully")

'''

import streamlit as st
from pytube import YouTube

st.title("YouTube Video Downloader")

# Input field for video URL
url = st.text_input("Enter YouTube Video URL:")

if url:
    try:
        yt = YouTube(url)
        st.write(f"**Title:** {yt.title}")
        st.image(yt.thumbnail_url, use_column_width=True)

        # Get video streams
        video_streams = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc()

        if video_streams:
            resolutions = [stream.resolution for stream in video_streams]
            selected_resolution = st.selectbox("Select Resolution", resolutions)

            if st.button("Download"):
                video_stream = yt.streams.filter(res=selected_resolution, progressive=True).first()
                video_stream.download()
                st.success("Download Complete! Check your directory.")

    except Exception as e:
        st.error(f"Error: {e}")


