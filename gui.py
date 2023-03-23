import tkinter

import engine
# from engine im


def download_clicked(event=None):
    engine.download_button_clicked(entry.get())


top_window = tkinter.Tk()
top_window.geometry("500x200")
top_window.title("YouTube Music Downloader")

# Label:
message = tkinter.Label(top_window, text="Enter song name:")
message.pack()

# Input:
entry = tkinter.Entry()
entry.pack()

# Buttons:
download_button = tkinter.Button(text="Download", command=download_clicked)
download_button.pack()

browse_button = tkinter.Button(text="Browse", command=engine.browse_button_clicked)
browse_button.pack()

# Label:
finish_message = tkinter.Label(top_window, text="Finished")
finish_message.pack()

# Start download when press Enter:
entry.bind("<Return>", download_clicked)

top_window.mainloop()
