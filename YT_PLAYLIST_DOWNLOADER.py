from pytube import Playlist
import re

def download_playlist(url, download_path):
    playlist = Playlist(url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print(f"Downloading {len(playlist)} videos...")

    for video in playlist.videos:
        try:
            video.streams.get_highest_resolution().download(download_path)
            print(f"Downloaded: {video.title}")
        except Exception as e:
            print(f"Error downloading {video.title}: {e}")

if __name__ == "__main__":
    print('\n\nDownload any playlist from youtube: \n')
    playlist_url = input("Enter the URL of the YouTube playlist: ")
    download_path = input("Enter the download path: ")

    download_playlist(playlist_url, download_path)
