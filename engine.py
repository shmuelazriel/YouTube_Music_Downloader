import pytube
from tkinter import filedialog


class Engine:
    def __init__(self):
        self.path = "./Downloaded"

    def browse_button(self):
        directory = filedialog.askdirectory()
        self.path = directory + "/"

    def text_to_url(self, name):
        song = pytube.Search(name).results[0]
        return song.watch_url

    def download_button(self, name):
        print(f'Downloading "{name}"')
        url = self.text_to_url(name)
        yt = pytube.YouTube(url)
        audio_file = yt.streams.filter(only_audio=True).first()
        audio_file.download(output_path=self.path, filename=f'{yt.title}.mp3')
        # finish_message.pack()
        print("\nFinished")
