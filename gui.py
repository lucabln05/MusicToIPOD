
import customtkinter
from tkinter import filedialog
from downloader import *

#initialisierung
global folder
folder = ''


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        def mp3_check():
            if mp3_var.get() == 'mp3':
                tag_checkbox.configure(state='normal')
                quality.configure(state='normal')
                res.configure(state='disabled')
            else:
                tag_checkbox.configure(state='disabled')
                artist_entry.configure(state='disabled')
                album_entry.configure(state='disabled')
                genre_entry.configure(state='disabled')
                quality.configure(state='disabled')
                tag_var.set('off')

        def tag_check():
            if tag_var.get() == 'on':
                artist_entry.configure(state='normal')
                album_entry.configure(state='normal')
                genre_entry.configure(state='normal')

            else:
                artist_entry.configure(state='disabled')
                album_entry.configure(state='disabled')
                genre_entry.configure(state='disabled')


        def change_folder():
            global folder
            folder = filedialog.askdirectory()

        def download(): 
            if folder == '':
                change_folder()
            download_playlist(folder, entry.get(), res.get(), mp3_var.get())
            if mp3_var.get() == 'mp3':
                convert_mp3(folder, quality.get())
            if tag_var.get() == 'on':
                tag_mp3(folder, artist_entry.get(), album_entry.get(), genre_entry.get())



        self.title("MusicToIPOD - Youtube Downloader")
        self.geometry("500x400")
        self.grid_columnconfigure(0, weight=1)

        entry = customtkinter.CTkEntry(self, placeholder_text="Playlist URL")
        entry.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        download_button = customtkinter.CTkButton(self, text='Download', command=download)
        download_button.grid(row=0, column=3, padx=10, pady=10)

        mp3_var = customtkinter.StringVar(value='mp4')
        mp3_checkbox = customtkinter.CTkCheckBox(self, text="MP3", command=mp3_check, variable=mp3_var, onvalue='mp3', offvalue='mp4')
        mp3_checkbox.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="w")

        tag_var = customtkinter.StringVar(value='off')
        tag_checkbox = customtkinter.CTkCheckBox(self, text="Tag MP3", command=tag_check, variable=tag_var, onvalue='on', offvalue='off', state='disabled')
        tag_checkbox.grid(row=1, column=1, padx=20, pady=(0, 10), sticky="w")

        folder_button = customtkinter.CTkButton(self, text='Folder', command=change_folder)
        folder_button.grid(row=1, column=3, padx=10, pady=10)

        artist_entry = customtkinter.CTkEntry(self, placeholder_text="Artist")
        artist_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        album_entry = customtkinter.CTkEntry(self, placeholder_text="Album")
        album_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
        genre_entry = customtkinter.CTkEntry(self, placeholder_text="Genre")
        genre_entry.grid(row=5, column=1, padx=10, pady=10, sticky="ew")
        quality = customtkinter.CTkComboBox(self, values=["128k", "320k"])
        quality.grid(row=6, column=1, padx=10, pady=10, sticky="ew")
        quality.set("320k")

        artist_entry.configure(state='disabled')
        album_entry.configure(state='disabled')
        genre_entry.configure(state='disabled')
        quality.configure(state='disabled')
        res = customtkinter.CTkComboBox(self, values=["High Res", "Low Res"])
        res.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        res.set("Low Res")
        res.configure(state='normal')
                

app = App()
app.mainloop()
