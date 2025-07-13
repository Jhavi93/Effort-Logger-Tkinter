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
    print("Effort logged successfully!")

if __name__ == "__main__":
    print("Effort Logging Tool")
    user = input("Enter your name: ")
    project = input("Enter project name: ")
    task_type = input("Enter task type (e.g., Analysis, Coding, Testing): ")
    hours_spent = float(input("Enter hours spent: "))
    comments = input("Enter any comments (optional): ")
    log_effort(user, project, task_type, hours_spent, comments)
