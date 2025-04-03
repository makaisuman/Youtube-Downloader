import streamlit as st
import streamlit as st
try:
    import yt_dlp
    st.write("yt-dlp is installed!")
    st.write(f"yt-dlp version: {yt_dlp.__version__}")
except ImportError as e:
    st.error(f"Error: {e}")

st.title("YouTube Video Downloader")

# Input field for video URL
url = st.text_input("Enter YouTube Video URL:")

if url:
    try:
        # Set options for yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Select the best video and audio quality
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Set output template for downloaded files
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'Unknown Title')

            st.write(f"**Title:** {video_title}")
            st.write(f"Downloading {video_title}...")

            # Download the video
            ydl.download([url])
            st.success(f"Download Complete! The video '{video_title}' has been saved.")

    except Exception as e:
        st.error(f"Error: {e}")
