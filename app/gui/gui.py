import tkinter as tk
from tkinter import ttk
from app.config.listener import start_listening,stop_listening


def on_play():
    start_listening()

def on_stop():
    stop_listening()

def on_close(root):
    stop_listening()
    root.destroy()

def load_gui():
    root = tk.Tk()
    root.overrideredirect(True)

    root.geometry("280x50+{}+{}".format(root.winfo_screenwidth()-290, root.winfo_screenheight()-100))
    root.attributes('-topmost', True)

    frame = ttk.Frame(root, padding=10, style='Custom.TFrame')
    frame.pack(expand=True, fill=tk.BOTH)

    play_button = ttk.Button(frame, text='▶️', command=on_play)
    play_button.grid(row=0, column=1, padx=5)

    stop_button = ttk.Button(frame, text='⏹️', command=on_stop)
    stop_button.grid(row=0, column=2, padx=5)

    close_btn = ttk.Button(frame, text='❌', style='Custom.TButton', command=lambda: on_close(root))
    close_btn.grid(row=0, column=3, padx=5)

    root.mainloop()



