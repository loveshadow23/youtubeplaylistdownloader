import yt_dlp
import os

# Global counter to keep track of the total number of videos downloaded
video_counter = 1

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
    }

    # Process each playlist URL
    global video_counter  # Use the global video_counter variable
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for playlist_url in playlist_urls:
            print(f"Downloading playlist: {playlist_url}")
            
            # Get a list of current files to differentiate new downloads later
            existing_files = set(os.listdir())
            
            # Download the playlist
            ydl.download([playlist_url])
            
            # Get only the new files that were downloaded
            new_files = set(os.listdir()) - existing_files
            
            # Rename only the new files
            video_counter = rename_files(list(new_files), video_counter)  # Pass the new files and current video count

def rename_files(new_files, counter):
    # Only process mp4 files
    mp4_files = [f for f in new_files if f.endswith('.mp4')]

    # Sort the files based on their playlist index (assuming they follow the naming convention)
    mp4_files.sort(key=lambda x: int(x.split(' - ')[0]))  # Sort by playlist index

    for old_filename in mp4_files:
        new_filename = f"{counter:03d} - {old_filename.split(' - ', 1)[1]}"  # Use zero-padded counter
        os.rename(old_filename, new_filename)
        print(f"Renamed '{old_filename}' to '{new_filename}'")
        counter += 1  # Increment counter for the next video

    return counter  # Return the updated counter

if __name__ == "__main__":
    download_playlists()
