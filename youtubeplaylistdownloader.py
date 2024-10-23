import yt_dlp
import os

def download_playlists():
    playlist_urls = []
    print("Enter YouTube playlist URLs one by one (type 'done' when finished):")
    
    while True:
        url = input("Enter playlist URL: ")
        if url.lower() == 'done':
            break
        playlist_urls.append(url)

    # Define yt-dlp options
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s',  # Include playlist index
        'merge_output_format': 'mp4',
        'progress_hooks': [on_progress]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for playlist_url in playlist_urls:
            print(f"Downloading playlist: {playlist_url}")
            ydl.download([playlist_url])

def on_progress(d):
    if d['status'] == 'finished':
        # When the download is complete, log the filename
        print(f"Downloaded: {d['filename']}")

if __name__ == "__main__":
    download_playlists()
