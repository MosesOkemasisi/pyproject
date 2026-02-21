import tkinter as tk
from plyer import notification
import threading
import time

def set_reminder():
    reminder_time = int(entry_time.get())
    message = entry_message.get()


    def notify():
        time.sleep(reminder_time)
        notification.notify(
            title="Desktop Notifier",
            message=message,
            timeout=10
        )
        threading.Thread(target=notify).start()
        window = tk.Tk()
        window.title("Desktop Notifier App")
        window.geometry("400*250")

        tk.Label(window, text="Enter time in seconds:").pack(pady=5)
        entry_time=tk.Entry(window)
        entry_time.pack(pady=5)

        tk.Label(window, text="Enter reminder message:").pack(pady=5)
        entry_message = tk.Entry(window)
        entry_message.pack(pady=5)

        tk.Button(window, text="Set Reminder", command=set_reminder).pack(pady=20)
        window.mainloop()
