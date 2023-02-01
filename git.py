import os
import subprocess
import sys
from datetime import datetime


# ==============================================================

paths = [
    r"a"
]

# ==============================================================
try:
    action = sys.argv[1]
except:
    print("An action must be passed (up/down)")
    exit()

if action == "up":
    for path in paths:
        command = subprocess.run(["git","add", "."])
        command = subprocess.run(["git","status"], stdout=subprocess.PIPE, text=True)

        # (There's) nothing to commit, working tree clean
        if "nothing to commit, working tree clean" in command.stdout:
            continue
        
        today_commit = datetime.now()
        today_commit = today_commit.strftime("%Y-%m-%d %H:%M")
        command = subprocess.run(["git","commit", "-m", today_commit], stdout=subprocess.PIPE, text=True)

        print(command.stdout)

        # command = subprocess.run(["git","push"], stdout=subprocess.PIPE, text=True)
        # print(command.stdout)

elif action == "down":
    for path in paths:
        os.chdir(path)
        subprocess.run(["git", "pull"])


