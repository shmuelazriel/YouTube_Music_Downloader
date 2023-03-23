import pytube
from tkinter import filedialog

# from GUI import finish_message

path = "./Downloaded"


def text_to_url(name):
    song = pytube.Search(name).results[0]
    return song.watch_url


def download_button_clicked(name):
    print(f'Downloading "{name}"')
    url = text_to_url(name)
    yt = pytube.YouTube(url)
    audio_file = yt.streams.filter(only_audio=True).first()
    audio_file.download(output_path=path, filename=f'{yt.title}.mp3')
    # finish_message.pack()
    print("\nFinished")


def browse_button_clicked():
    directory = filedialog.askdirectory()
    print("Path: ", directory + "/")
    global path
    path = directory + "/"
