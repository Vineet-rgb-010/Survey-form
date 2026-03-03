import yt_dlp as ytd
import streamlit as st
import os
from time import sleep
import tempfile

def download(video_url):
    temp_dir = tempfile.mkdtemp()

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{temp_dir}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }
    with ytd.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        filename = ydl.prepare_filename(info)
        mp3_file = filename.rsplit(".", 1)[0] + ".mp3"

    return mp3_file
def mp3_downloader():
    url = st.text_input("Paste the URL below", placeholder='URL')
    check_button = st.button("Check availability")
    if check_button and url != '':
        with st.spinner("Checking the availability of the URL..."):
            try:
                file_path = download(url)
                with open(file_path, 'rb') as f:
                    st.success("Ready to download!")
                    st.download_button("Download", data = f, file_name = os.path.basename(file_path), mime = "audio/mpeg")
            except Exception as e:
                st.error("An error occured!")
                sleep(2)
                st.rerun()
    if check_button and url == '':
        st.warning("Enter a URL first.")

if __name__ == "__main__":
    mp3_downloader()
