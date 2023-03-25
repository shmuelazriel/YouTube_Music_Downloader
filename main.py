from gui import Gui
from engine import Engine

engine = Engine()


def browse_clicked():
    engine.browse_button()


def download_clicked(event=None, song_name="I miss you"):
    try:
        engine.download_button(youtube_downloader.user_input.get())
    except:
        engine.download_button(song_name)


youtube_downloader = Gui()
youtube_downloader.window_components(youtube_downloader.user_input.bind("<Return>", download_clicked), browse_clicked)
youtube_downloader.start()
