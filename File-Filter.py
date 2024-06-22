import tkinter as tk
from tkinter import ttk, StringVar
import os
import shutil

file_types = {
    'audio_files': ('.mp3', '.m4a', '.MP3', '.mpeg'),
    'video_files': ('.mp4', '.mkv', '.MOV', '.MP4', '.webm'),
    'photo_files': ('.png', '.jpg', '.PNG', '.JPG', '.jpeg'),
    'pdf_files': ('.pdf', '.pptx', '.docx'),
    'zip_files': ('.zip', '.rar', '.7z'),
    'executable_files': ('.exe', '.bat', '.sh'),
    'text_files': ('.txt', '.md', '.log'),
    'spreadsheet_files': ('.xls', '.xlsx', '.csv'),
    'presentation_files': ('.ppt', '.pptx'),
    'document_files': ('.doc', '.docx', '.odt'),
    'database_files': ('.db', '.sql', '.sqlite'),
    'code_files': ('.py', '.java', '.c', '.cpp', '.js', '.html', '.css', '.php', '.rb', '.swift'),
    'image_files': ('.gif', '.bmp', '.tiff', '.svg', '.ico'),
    'compressed_files': ('.tar', '.gz', '.bz2', '.xz', '.rar', '.7z'),
    'torrent_files': ('.torrent',)
}

def file_filter(path, file_types):
    for types, extensions in file_types.items():
        folder_name, _ = types.split('_')
        folderpath = os.path.join(path, folder_name)
        print(folderpath)
        for file in os.listdir(path):
            for ex in extensions:
                if file.endswith(ex):  
                    if not os.path.exists(folderpath):
                        os.mkdir(folderpath)
                    print(f"{ex} ==> {folderpath}")
                    shutil.move(file,f'{folderpath}/')


def clear_message():
    message_label.config(text="")

root = tk.Tk()
root.title('File Filter')
root.geometry('600x600')
root.minsize(350, 300)
# root.maxsize(400, 300)
root.configure(bg='#252525')  # Set background color

win = ttk.Frame(root, padding=10)
win.grid(sticky=(tk.W, tk.E, tk.N, tk.S))
win.configure(style='My.TFrame')

def click(event):
    current_path = path.get().strip()
    if not os.path.isdir(current_path):
        message_label.config(text=f"The specified path '{current_path}' does not exist or is not a directory.")
    else:
        os.chdir(current_path)
        file_filter(current_path, file_types)
        message_label.config(text="Files filtered successfully.")
        root.after(3000, clear_message)  # Clear the message after 3 seconds

# Configure the grid to expand and center the widgets
win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=1)

ttk.Style().configure('My.TFrame', background='#252525')
ttk.Style().configure('My.TLabel', background='#252525', foreground='white')
ttk.Style().configure('My.TEntry', fieldbackground='#252525', foreground='black')
ttk.Style().configure('My.TButton', background='#252525', foreground='black')  # Set button text to black

ttk.Label(win, text="Enter path:", style='My.TLabel').grid(column=0, row=0, columnspan=3, pady=(0, 10), sticky='n')

path = StringVar()
path.set('')
box = ttk.Entry(win, textvariable=path, font="lucida 15 bold", style='My.TEntry')
box.grid(row=1, column=0, columnspan=3, padx=5, pady=10, ipady=5, sticky=(tk.W, tk.E))

btn = ttk.Button(win, text='Filter Files', style='My.TButton')
btn.grid(row=3, column=1, pady=5, ipady=10, sticky='s')
btn.bind('<Button-1>', click)

# Message label to show status
message_label = ttk.Label(win, text="", foreground="red", style='My.TLabel')
message_label.grid(column=0, row=4, columnspan=3, pady=5, sticky='n')

# Center the frame within the root window
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
win.grid(sticky=(tk.W, tk.E, tk.N, tk.S))

win.mainloop()
