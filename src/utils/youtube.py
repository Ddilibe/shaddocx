from pytube import YouTube, Playlist
from bs4 import BeautifulSoup
from typing import Union
import requests
import re


class YouTubeDownLoad:
    """
    Class for controlling the downloading of youtube videos

    Args:
        url[str]: The url for the download
        audio_only[bool]: This determines whether the media will be downloaded with audio or without audio
        file_extension[str]: different file extensions for the file to be saved
        resolution[str]: resolution of the media to be choosen
        save_directory[str]: The directory to save it
        itag: this is the itag for the video download
        filename: This is the option to change the name of the file
    """

    def __init__(
        self,
        url: str,
        audio_only: bool = False,
        progressive: bool = True,
        file_extension: str = "MP4",
        resolution: str = "360p",
        save_directory: str = "C:\\Users\\Dilibe\\Downloads",
        itag: int = 22,
        filename: Union[str, None] = None,
    ) -> None:
        self.url, self.audio_only, self.progressive = url, audio_only, progressive
        self.file_extension, self.resolution = file_extension, resolution
        self.save_directory, self.itag, self.filename = save_directory, itag, filename
        self.get_data()

    def get_data(self) -> None:
        print("[+] - Getting Data")
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.soup = BeautifulSoup(self.response.text, "html.parser")
            print("[+] - Redirecting To Download Function")
            self.redirect_to_download_function()
        else:
            print(
                f"[-] - Failed to retrieve the webpage. Status code: {self.response.status_code}"
            )

    def redirect_to_download_function(self) -> None:
        print("[+] - Checking", self.soup.find("title").getText())
        if "YouTube" in self.soup.find("title").text:
            video_pattern = re.compile(
                r"https://www\.youtube\.com/watch\?v=([a-zA-Z0-9_-]+)"
            )
            playlist_pattern = re.compile(
                r"https://www\.youtube\.com/playlist\?list=([a-zA-Z0-9_-]+)"
            )
            if video_pattern.match(self.url):
                self.single_youtube()
            elif playlist_pattern.match(self.url):
                self.playlist_youtube()

    def playlist_youtube(self) -> None:
        """Method for downloading Playlist"""
        play = Playlist(self.url)
        print(f"[+] - Downloading Playlist: {play.title}")
        for vids in play.video_urls:
            print("\n")
            self.url = vids
            self.single_youtube()
        print(f"[+] - Done downloading Playlist: {play.title}")

    def single_youtube(self) -> None:
        """Function for downloading the videos"""
        yt = YouTube(self.url)
        print(f"[+] - Downloading Video {yt.title}")
        if self.audio_only:
            yt.streams.filter(only_audio=self.audio_only)
        if not (self.progressive):
            yt.streams.filter(progressive=self.progressive)
        yt.streams.filter(file_extension=self.file_extension)
        yt.streams.filter(resolution=self.resolution)
        streams = yt.streams.get_by_itag(self.itag)
        name = (
            f"{self.filename}.{self.file_extension}"
            if self.filename
            else f"{yt.title}.{self.file_extension}"
        )
        streams.download(self.save_directory, name)
