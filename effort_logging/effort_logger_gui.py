import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), 'data', 'logs.json')

def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_logs(logs):
    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=4)

def log_effort(user, project, task_type, hours_spent, comments=""):
    logs = load_logs()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": user,
        "project": project,
        "task_type": task_type,
        "hours_spent": hours_spent,
        "comments": comments
    }
    logs.append(entry)
    save_logs(logs)

def submit_form():
    user = entry_user.get()
    project = entry_project.get()
    task_type = task_type_var.get()
    try:
        hours_spent = float(entry_hours.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Hours must be a number.")
        return
    comments = entry_comments.get("1.0", tk.END).strip()
    log_effort(user, project, task_type, hours_spent, comments)
    messagebox.showinfo("Success", "Effort logged successfully!")
    root.destroy()

def cancel_form():
    if messagebox.askokcancel("Cancel", "Are you sure you want to cancel?"):
        root.destroy()

# GUI setup
root = tk.Tk()
root.title("Effort Logging System")

frame = tk.Frame(root, padx=15, pady=15)
frame.pack()

tk.Label(frame, text="Effort Logging System", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 10))

tk.Label(frame, text="Name:").grid(row=1, column=0, sticky="e")
entry_user = tk.Entry(frame)
entry_user.grid(row=1, column=1)

tk.Label(frame, text="Project:").grid(row=2, column=0, sticky="e")
entry_project = tk.Entry(frame)
entry_project.grid(row=2, column=1)

tk.Label(frame, text="Task Type:").grid(row=3, column=0, sticky="e")
task_type_var = tk.StringVar()
task_dropdown = ttk.Combobox(frame, textvariable=task_type_var)
task_dropdown['values'] = ("Analysis", "Design", "Coding", "Testing", "Project Management")
task_dropdown.grid(row=3, column=1)

tk.Label(frame, text="Hours Spent:").grid(row=4, column=0, sticky="e")
entry_hours = tk.Entry(frame)
entry_hours.grid(row=4, column=1)

tk.Label(frame, text="Comments:").grid(row=5, column=0, sticky="ne")
entry_comments = tk.Text(frame, height=4, width=30)
entry_comments.grid(row=5, column=1)

button_frame = tk.Frame(frame)
button_frame.grid(row=6, column=0, columnspan=2, pady=10)

submit_btn = tk.Button(button_frame, text="Submit", command=submit_form, width=12)
submit_btn.pack(side="left", padx=5)

cancel_btn = tk.Button(button_frame, text="Cancel", command=cancel_form, width=12)
cancel_btn.pack(side="right", padx=5)

root.mainloop()
