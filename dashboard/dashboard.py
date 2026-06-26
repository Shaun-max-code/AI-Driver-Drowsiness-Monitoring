import json
import tkinter as tk

root = tk.Tk()
root.title("Edge AI Smart Home Dashboard")
root.geometry("600x500")

title = tk.Label(
    root,
    text="🏠 Edge AI Smart Home Dashboard",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

status = tk.Label(
    root,
    font=("Arial", 18),
    justify="left"
)
status.pack(pady=20)

def update():
    try:
        with open("device_state.json", "r") as f:
            data = json.load(f)

        text = (
            f"🖐 Gesture : {data['gesture']}\n\n"
            f"💡 Light   : {data['light']}\n"
            f"🌀 Fan     : {data['fan']}\n"
            f"🚪 Door    : {data['door']}"
        )

        status.config(text=text)

    except Exception as e:
        status.config(text=str(e))

    root.after(1000, update)

update()
root.mainloop()