
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


