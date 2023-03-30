import tkinter


class Gui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("250x110")
        self.main_window.title("YouTube Music Downloader")

        # Label:
        self.label = tkinter.Label(self.main_window, text="Enter song name:")
        self.label.pack(anchor="center")

        # User input:
        self.placeholder = "Happy Birthday!"
        self.user_input = tkinter.Entry(fg="gray", insertwidth=1, insertofftime=500)
        self.user_input.pack()
        self.user_input.insert(0, self.placeholder)
        self.user_input.bind("<FocusIn>", self.clear_placeholder)
        self.user_input.bind("<FocusOut>", self.set_placeholder)

        # Version
        self.version = tkinter.Label(self.main_window, text="Version: 0.19")
        self.version.pack(side="right", anchor="se")

    def window_components(self, download_command, browse_command):
        # Download button:
        download_button = tkinter.Button(text="Download", command=download_command)
        download_button.pack()

        # Browse button:
        browse_button = tkinter.Button(text="Browse", command=browse_command)
        browse_button.pack(before=download_button)

    def clear_placeholder(self, event):
        if self.user_input.get() == self.placeholder:
            self.user_input.delete(0, tkinter.END)
            self.user_input.config(fg="black")

    def set_placeholder(self, event):
        if self.user_input.get() == "":
            self.user_input.insert(0, self.placeholder)
            self.user_input.config(fg="gray")

    def start(self):
        self.main_window.mainloop()
