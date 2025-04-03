import streamlit as st
import youtube_dl  # Switch to youtube-dl

st.title("YouTube Video Downloader")

url = st.text_input("Enter YouTube Video URL:")

if url:
    try:
        # Set options for youtube-dl
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save to downloads folder
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'Unknown Title')

            st.write(f"**Title:** {video_title}")
            st.write(f"Downloading {video_title}...")

            ydl.download([url])
            st.success(f"Download Complete! The video '{video_title}' has been saved.")

    except Exception as e:
        st.error(f"Error: {e}")
