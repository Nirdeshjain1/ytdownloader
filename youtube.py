#creating youtube downloader

from pytube import YouTube

def download_video(link):
    try:
        youtube_object = YouTube(link)
        youtube_object = youtube_object.streams.get_highest_resolution()
        youtube_object.download()
        print("Download completed successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

link = input("Enter the YouTube video URL: ")
download_video(link)
