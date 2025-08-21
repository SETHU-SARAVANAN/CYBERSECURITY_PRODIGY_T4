# app_key_recorder.py
# Logs keys typed in THIS Tkinter window only — not system-wide.
# pip install pynput (NOT required here), this uses stdlib Tkinter.
import tkinter as tk, datetime as dt, pathlib

LOG = pathlib.Path("keylog_app_scoped.txt")

def on_key(event):
    ts = dt.datetime.now().isoformat(timespec="seconds")
    rep = event.keysym if len(event.char)==0 else event.char
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"{ts}\t{rep}\n")
    status.set(f"Last: {rep}")

root = tk.Tk()
root.title("Consent-based Keystroke Recorder")
tk.Label(root, text="Typing here will be recorded to keylog_app_scoped.txt.\n"
                    "This recorder ONLY captures keys in this window.",
         padx=12, pady=12).pack()
status = tk.StringVar(value="Ready")
tk.Label(root, textvariable=status).pack(pady=6)

entry = tk.Text(root, width=60, height=10)
entry.pack(padx=12, pady=12)
entry.bind("<Key>", on_key)
entry.focus_set()
root.mainloop()
