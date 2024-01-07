from pytube import YouTube
import tkinter as tk
from tkinter import messagebox

def utube_downloader():
    video_url = video_link.get()
    save_path = r'C:\USER\Downloads\Video'

    try:
          yt = YouTube(video_url)
          video_stream = yt.streams.get_highest_resolution()
          video_stream.download(output_path=save_path)
          messagebox.showinfo('download complete','succefully downloaded the video!')
    except Exception as e:
           messagebox.showerror("Error", f"An error occurred: {str(e)}") 



# Window for the application
root = tk.Tk()
root.title('Downloader')
root.geometry('300x150')
root.resizable(width=False, height=False)

video_link = tk.StringVar()

entry = tk.Entry(master=root, textvariable=video_link)
entry.pack(pady=10)

download_button = tk.Button(master=root, text='Download', command=utube_downloader)
download_button.pack(pady=30)

root.mainloop()
